"""
cryptography.py
Author: <your name here>
Credit: Payton, David,

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
quit = false 
while quit==false:
    int1 = input("Enter e to encrypt, d to decrypt, or q to quit:")
    if int1 not in ('e', 'd' 'q'):
        print("Did not understand command, try again.")
        int1 = input("Enter e to encrypt, d to decrypt, or q to quit:")
    if int1== 'e':
        message = input("Message: ")
        key = input("Key: ")
        
        
    

"""
if int1 == 'q':
    print("Goodbye")
elif int1 == 'e' or'd':
   message = input("Message: ") 
else:   
    print("Did not understand command, try again.")
key = input("Key: ")
message = [associations.index(x) for x in message]
print(message)
"""
"""
Enter e to encrypt, d to decrypt, or q to quit: e
Message: Two plus two = Five
Key: Lorem ipsum
+KF;B(CH=NIZ}m;R\Dt
Enter e to encrypt, d to decrypt, or q to quit: d
Message: +KF;B(CH=NIZ}m;R\Dt
Key: Lorem ipsum
Two plus two = Five
Enter e to encrypt, d to decrypt, or q to quit: q
Goodbye!
"""