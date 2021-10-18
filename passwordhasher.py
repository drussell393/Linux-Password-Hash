#!/usr/bin/env python3
# Password Hashing Module for Linux
# Author: Dave Russell Jr (drussell393)

from getpass import getpass
import crypt

# If you like Python 2, please to be importing.
#import os
#import binascii

password = getpass('Enter your desired password, Harry: ')
passwordConfirm = getpass('Confirm your password: ')

if (password == passwordConfirm):
    # Python 2 alternative, os.urandom()
    #passwordHash = crypt.crypt(password, '$6$' + binascii.hexlify(os.urandom(4)))

    # Python 3 likes my crypt (mksalt doesn't work in Python 2)
    passwordHash = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))

    print('You\'re a wizard, Harry: ' + passwordHash)
else:
    print('Dobby has heard of your greatness, sir. But of your goodness, Dobby never knew.')
    print('Your confirmation password didn\'t match, Oh Great One.')
