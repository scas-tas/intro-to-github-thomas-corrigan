def encode(message, shift):
  result = ""
  for char in message:
    if char.isalpha():
      base = ord("A") if char.isupper() else ord("a")
      new_code = (ord(char) - base + shift) % 26 + base
      result += chr(new_code)
    else:
      result += char
  return result

def decode(message, shift):     # Do Reverse of encode function
  return encode(message, -shift)



print(encode("Hello", 3))
print(encode("Hello, World!", 3))
print(decode("Khoor", 3))
print(encode("xyz", 3))