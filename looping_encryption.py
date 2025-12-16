#Previous code iterations that I'm not ready to delete yet
#copy of Encryption.py to see if I can clean this up with the def() function

alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 8

#print (len (alphabet))

#print (alphabet [:shift])

shifted_alphabet = alphabet [shift:] + alphabet [:shift]

#print (shifted_alphabet)

encryption_table = str.maketrans (alphabet, shifted_alphabet)


def encryption():
    password = input ('please type password ')
    confirmation = input ('please retype password ')

    def confirmation_check ():
        if password == confirmation:
            print ('Password successfully created')
            encrypted_password = password.translate(encryption_table)
            print (encrypted_password)
        else:
            print ('Passwords do not match, try again')
            encryption()
    confirmation_check ()

encryption()

# :)


