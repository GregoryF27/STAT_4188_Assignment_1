encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here


decrypted_message = list(encrypted_message)
for i in range(1,len(decrypted_message)//2,2):
    j = len(decrypted_message)-i-1
    decrypted_message[i], decrypted_message[j] = decrypted_message[j], decrypted_message[i]
    
    
decrypted_message = ''.join(decrypted_message)
print(decrypted_message)