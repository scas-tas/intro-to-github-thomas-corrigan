import math
import random
import sys
import pygame
import serial
import serial.tools.list_ports

# Configuration
WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT - 50
MAX_DISTANCE_CM = 200
RADIUS = 500

# Colors
BG_COLOR = (10, 20, 10)
GREEN = (0, 255, 65)
DARK_GREEN = (0, 60, 20)
RED = (255, 50, 50)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LIGHT_GRAY = (100, 100, 100)

pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont("Consolas", 14)
LARGE_FONT = pygame.font.SysFont("Consolas", 18, bold=True)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Micro:bit Sonar Visualizer")
clock = pygame.time.Clock()

# Global State
ser = None
connected_port = None
current_angle = 0
current_dist = 0
sweep_points = {}  # {angle: (distance, timestamp)}

# Simulation State (Randomized Demo)
sim_angle = 0.0
sim_dir = 0.5

def generate_random_targets():
    """Generates 2 to 4 random targets formatted as (angle, distance)."""
    count = random.randint(2, 4)
    targets = []
    for _ in range(count):
        center_angle = random.randint(20, 160)
        distance = random.randint(40, 170)
        targets.append((center_angle, distance))
    return targets

sim_targets = generate_random_targets()

def get_serial_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

class DropdownGUI:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.options = []
        self.refresh()
        self.selected_index = -1
        self.is_open = False

    def refresh(self):
        detected = get_serial_ports()
        self.options = ["Demo Mode (Simulation)"] + detected

    def draw(self, surface):
        label = self.options[self.selected_index] if 0 <= self.selected_index < len(self.options) else "Select Port / Demo"
        pygame.draw.rect(surface, GRAY, self.rect)
        pygame.draw.rect(surface, GREEN, self.rect, 1)
        
        txt = FONT.render(label, True, WHITE)
        surface.blit(txt, (self.rect.x + 10, self.rect.y + 8))

        if self.is_open:
            for i, opt in enumerate(self.options):
                opt_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                pygame.draw.rect(surface, GRAY, opt_rect)
                pygame.draw.rect(surface, LIGHT_GRAY, opt_rect, 1)
                opt_txt = FONT.render(opt, True, WHITE)
                surface.blit(opt_txt, (opt_rect.x + 10, opt_rect.y + 8))

    def handle_event(self, event):
        global ser, connected_port
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.refresh()
                self.is_open = not self.is_open
                return

            if self.is_open:
                for i in range(len(self.options)):
                    opt_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                    if opt_rect.collidepoint(event.pos):
                        self.selected_index = i
                        self.is_open = False
                        connected_port = self.options[i]
                        
                        if connected_port == "Demo Mode (Simulation)":
                            if ser and ser.is_open:
                                ser.close()
                            ser = None
                        else:
                            try:
                                if ser and ser.is_open:
                                    ser.close()
                                ser = serial.Serial(connected_port, 115200, timeout=0.1)
                            except Exception as e:
                                print(f"Connection failed: {e}")
                        return
                self.is_open = False

dropdown = DropdownGUI(20, 20, 220, 30)

def draw_radar_grid():
    for r in range(1, 5):
        radius = int(RADIUS * (r / 4))
        pygame.draw.arc(screen, DARK_GREEN, (CENTER_X - radius, CENTER_Y - radius, radius * 2, radius * 2), 0, math.pi, 2)
        dist_lbl = FONT.render(f"{int(MAX_DISTANCE_CM * (r / 4))} cm", True, DARK_GREEN)
        screen.blit(dist_lbl, (CENTER_X + 5, CENTER_Y - radius - 7))

    for a in range(0, 181, 30):
        rad = math.radians(a)
        x = CENTER_X - int(RADIUS * math.cos(rad))
        y = CENTER_Y - int(RADIUS * math.sin(rad))
        pygame.draw.line(screen, DARK_GREEN, (CENTER_X, CENTER_Y), (x, y), 1)
        
        lbl_x = CENTER_X - int((RADIUS + 20) * math.cos(rad))
        lbl_y = CENTER_Y - int((RADIUS + 20) * math.sin(rad))
        lbl = FONT.render(f"{a}°", True, GREEN)
        screen.blit(lbl, (lbl_x - 10, lbl_y - 7))

    pygame.draw.line(screen, GREEN, (CENTER_X - RADIUS, CENTER_Y), (CENTER_X + RADIUS, CENTER_Y), 2)

def read_serial():
    global ser, current_angle, current_dist, sim_angle, sim_dir, sim_targets
    
    # Real Hardware Mode
    if ser and ser.is_open and ser.in_waiting:
        try:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if ',' in line:
                parts = line.split(',')
                current_angle = int(parts[0])
                current_dist = int(parts[1])
                sweep_points[current_angle] = (current_dist, pygame.time.get_ticks())
        except Exception:
            pass

    # Simulation Mode with Random Targets
    elif connected_port == "Demo Mode (Simulation)":
        sim_angle += sim_dir
        if sim_angle >= 180 or sim_angle <= 0:
            sim_dir = -sim_dir
            # Generate new random objects every time the sweep reverses direction
            sim_targets = generate_random_targets()
            
        current_angle = int(sim_angle)
        
        # Check if current angle hits any generated target angle (±5° width)
        current_dist = 0
        for target_angle, target_dist in sim_targets:
            if abs(current_angle - target_angle) <= 5:
                # Add minor distance variation for realism
                current_dist = target_dist + random.randint(-2, 2)
                break

        sweep_points[current_angle] = (current_dist, pygame.time.get_ticks())

# Main Loop
running = True
while running:
    clock.tick(60)
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        dropdown.handle_event(event)

    read_serial()
    draw_radar_grid()

    # Draw Sweeping Beam Line
    rad = math.radians(current_angle)
    sweep_x = CENTER_X - int(RADIUS * math.cos(rad))
    sweep_y = CENTER_Y - int(RADIUS * math.sin(rad))
    pygame.draw.line(screen, GREEN, (CENTER_X, CENTER_Y), (sweep_x, sweep_y), 2)

    # Draw Detected Obstacles with fade-out
    now = pygame.time.get_ticks()
    to_delete = []

    for angle, (dist, timestamp) in list(sweep_points.items()):
        age = now - timestamp
        if age > 6000:
            to_delete.append(angle)
            continue

        if 0 < dist <= MAX_DISTANCE_CM:
            a_rad = math.radians(angle)
            scaled_dist = (dist / MAX_DISTANCE_CM) * RADIUS
            px = CENTER_X - int(scaled_dist * math.cos(a_rad))
            py = CENTER_Y - int(scaled_dist * math.sin(a_rad))

            alpha = max(20, 255 - int((age / 6000) * 235))
            
            dot_surface = pygame.Surface((8, 8), pygame.SRCALPHA)
            pygame.draw.circle(dot_surface, (RED[0], RED[1], RED[2], alpha), (4, 4), 4)
            screen.blit(dot_surface, (px - 4, py - 4))

    for a in to_delete:
        del sweep_points[a]

    # Telemetry text overlay
    telemetry = f"Angle: {current_angle}° | Distance: {current_dist} cm"
    status_txt = LARGE_FONT.render(telemetry, True, GREEN)
    screen.blit(status_txt, (WIDTH - 350, 25))

    dropdown.draw(screen)
    pygame.display.flip()

if ser and ser.is_open:
    ser.close()
pygame.quit()
sys.exit()