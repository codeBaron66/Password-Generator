from cryptography import fernet
from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# print(key)

# file = open('fernet.txt', 'wb')
# file.write(key)
# file.close()

file = open('fernet.txt', 'rb')
key = file.read()
file.close()
# print(key)