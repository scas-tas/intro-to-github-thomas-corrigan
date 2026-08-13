# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# def encode(message, shift):
#   result = ""
#   for char in message:
#     lower_char = char.lower()

#     if lower_char in alphabet:
#       old_index = alphabet.index(lower_char)
#       new_index = (old_index + shift) % len(alphabet)
#       new_char = alphabet[new_index]

#       if char.isupper():
#         result += new_char.upper()
#       else:
#         result += new_char
#     else:
#       result += char 

#   return result


# def decode(message, shift):
#   return encode(message, -shift)



# print(encode("Hello", 3))
# print(encode("Hello, World!", 3))
# print(decode("Khoor", 3)) 
# print(encode("Hello WoRlD", 3))  


def encode(message, shift):
  result = ""

  for char in message:
    if char.isupper():
      shifted_code = (ord(char) - ord("A") + shift) % 26 + ord("A")
      result += chr(shifted_code)
    elif char.islower():
      shifted_code = (ord(char) - ord("a") + shift) % 26 + ord("a")
      result += chr(shifted_code)
    else:   
      result += char

  return result


def decode(message, shift):
  return encode(message, -shift)


print(encode('Hello', 3))
print(encode('Hello, World!', 3))
print(decode('Khoor', 3))
print(encode('xyz', 3))

