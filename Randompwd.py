#The Random library
import random
letters = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "#$%&/()=°|¿'}+[*]_-*@"

join = f' {letters} {numbers} {symbols} '
length = 19
password = random.sample (join, length)
password_final = "".join (password)
print (password_final)

print ("author MrScr1pt3r")

print ("strong password generated thanks for using this script")