import hid
import time

VENDOR_ID = 0x045E   # Microsoft
PRODUCT_ID = 0x09AD  # Surface Slim Pen Charger

try:
    device = hid.device()
    device.open(VENDOR_ID, PRODUCT_ID)
    print("==================================================")
    print("      SURFACE PEN CHARGER FULL TELEMETRY DUMP     ")
    print("==================================================")
    print("Drop your pen in or take it out to watch the buffer shift...\n")

    last_seen_buffer = None

    while True:
        # Read the full raw 64-byte buffer frame
        raw_data = device.read(64)
        
        if raw_data:
            # Convert the raw array into a clean python list
            full_buffer = list(raw_data)
            
            # Only print when something in the entire 64-byte string changes
            if full_buffer != last_seen_buffer:
                timestamp = time.strftime('%H:%M:%S')
                
                print(f"[{timestamp}] CHANGE DETECTED!")
                print("-" * 75)
                
                # Print index headers for easy scanning (00 to 15 per row)
                print("       00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15")
                print("       -----------------------------------------------")
                
                # Chunk the 64 bytes into neat rows of 16 for easy scanning
                for i in range(0, len(full_buffer), 16):
                    chunk = full_buffer[i:i+16]
                    hex_row = " ".join([f"{b:02X}" for b in chunk])
                    dec_row = " ".join([f"{b:03d}" for b in chunk])
                    
                    row_num = f"[{i:02d}]  "
                    print(f"{row_num} HEX: {hex_row}")
                    print(f"      DEC: {dec_row}")
                    print("")
                
                print("=" * 75 + "\n")
                last_seen_buffer = full_buffer
                
        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nExiting buffer scanner.")
except Exception as error:
    print(f"\nHardware Error: {error}")
