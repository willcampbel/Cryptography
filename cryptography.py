"""
cryptography.py
Author: <your name here>
Credit: David, Payton, Morgan

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
quit = False 
while quit==False:
    int1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if int1 not in ('e', 'd', 'q'):
        print("Did not understand command, try again.")
    elif int1== 'e':
        message = input("Message: ")
        message = [associations.index(x) for x in message]
        key = input("Key: ")
        key = [associations.index(x) for x in key]
        m=len(message)
        k=len(key)
        let=[]
        kelt=[]
        comb =[]
        if m>k:
            count = key * int((m-(m%k))/k)
            trun = key[0:(m%k)]
            newkey = count + trun
        elif k>m:
            newkey = key[0:m]
        else:
            newkey = key
        apple = [sum(x) for x in list(zip(newkey, message))]
        orange = ''.join([associations[x%len(associations)] for x in apple])
        print(orange)
    elif int1== 'd':
        message = input("Message: ")
        message = [associations.index(x) for x in message]
        key = input("Key: ")
        key = [associations.index(x) for x in key]
        m=len(message)
        k=len(key)
        let=[]
        kelt=[]
        comb =[]
        if m>k:
            count = key * int((m-(m%k))/k)
            trun = key[0:(m%k)]
            newkey = count + trun
        elif k>m:
            newkey = key[0:m] 
        apple = [sum(x) for x in list(zip([x*-1 for x in newkey], message))]
        orange = ''.join([associations[x%len(associations)] for x in apple])
        print(orange)
    elif int1=='q':
        quit=True
        print("Goodbye!")
        
        

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