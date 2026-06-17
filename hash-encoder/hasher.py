import hashlib

file_path = input("Enter file path: ")
hash = hashlib.sha256() # The initial SHA256 object so data can be added to it for final hash.

try:
  with open(file_path,'rb') as file: # So file is opened as variable: 'file'. 'r' is read mode and 'b' is binary mode.
    chunk = 0
    while True:
      chunk = file.read(1024) # In order to load file in smaller sections which is better for large files.
      if not chunk: # If end of file is reached b'' will be returned. In python b'' is empty so is boolean False.
        break
      hash.update(chunk) # Update the hash object incrementally with the sections.

  print(hash.hexdigest()) # To convert the hash into a readable hexadecimal string.

except FileNotFoundError: # Catch any errors so neat error handling message is outputted.
  print("Error: file not found")
