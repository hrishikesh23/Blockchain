#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 23:49:37 2018

@author: Arjun
"""


# Library is used to Generate Random unique Numbers
import uuid
import hashlib
"""
    bytes : Returns id in form of 16 byte string.
    int : Returns id in form of 128-bit integer.
    hex : Returns random id as 32 character hexadecimal string

"""
print(uuid.uuid1())
print(uuid.uuid4())

# Lets print the Subfields of UUID object

print("\n UUID Bytes = ", uuid.uuid1().bytes)
print("\n UUID Integer = ", uuid.uuid1().int)
print("\n UUID Hex = ", uuid.uuid1().hex)
print("\n UUID Time Low = ", uuid.uuid1().time_low)

"""
 UUID Bytes =  b"iSU\xc6)F\x11\xe8\xa2\x06\x00'\x10\xc6\x0c\x94"

 UUID Integer =  140008218215774199713941068513339116692

 UUID Hex =  6955ba64294611e8a206002710c60c94

 UUID Time Low =  1767300196
 
"""

"""
Some Other fields to be explored
    time_low : The first 32 bits of id.
    time_mid : The next 16 bits of id.
    time_hi_version : The next 16 bits of id.
    clock_seq_hi_variant : Next 8 bits of id.
    clock_seq_low : Next 8 bits of id.
    node : Last 48 bits of id.
    time : Time component field of id.
    clock_seq : 14 bit sequence number.
"""


print(hashlib.algorithms_available)

"""
Below is the output :
    print(hashlib.algorithms_available)
{'RIPEMD160', 'sha3_512', 'dsaEncryption', 'SHA1', 'SHA384', 'sha1', 
'sha3_256', 'SHA', 'mdc2', 'DSA-SHA', 'sha', 'md4', 'DSA', 'shake_128', 
'SHA256', 'blake2s', 'MD4', 'ecdsa-with-SHA1', 'sha512', 'ripemd160', 
'SHA224', 'blake2b', 'SHA512', 'dsaWithSHA', 'shake_256', 'whirlpool', 
'MD5', 'sha3_384', 'sha384', 'md5', 'MDC2', 'sha224', 'sha3_224', 'sha256'}
"""
print(hashlib.algorithms_guaranteed)

"""
{'sha3_512', 'shake_128', 'blake2b', 'blake2s', 'sha1', 'sha384', 
'sha3_256', 'md5', 'shake_256', 'sha512', 'sha224', 'sha3_224', 
'sha256', 'sha3_384'}
"""

def hash_password(password):
	# uuid is used to generate password
	hex_uid = uuid.uuid4().hex
	return (hashlib.sha256(hex_uid.encode() + password.encode()).hexdigest() + ':' + hex_uid)

def check_password(hashed_password, user_password):
	password, hex_uid = hashed_password.split(':')
	return password == hashlib.sha256(hex_uid.encode() + user_password.encode()).hexdigest()

new_pass = input('Please Enter password')
hashed_password = hash_password(new_pass)
print('The string to store in the DB is:' + hashed_password)
old_pass = input('Now Please enter the Password again to check:')

if check_password(hashed_password,old_pass):
	print('Woaooo That\'s Right')
else:
	print('Password does not match')


