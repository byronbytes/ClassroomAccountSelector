import webbrowser
import os


print('This is useful for the people who have more than 1 Google Account.')
print('If you only have 1 account this will not make a difference.')
print('')
os.system('pause')
print('[1] Default User / First Google Account Signed In')
print('')
print('[2] Second User / Second Google Account Signed In')
print('')
print('[3] Third User / Third Google Account Signed In')
print('')
print('')
choice = int(input())

if choice == 1:
    webbrowser.open('https://classroom.google.com/u/0/h')

if choice ==2:
    webbrowser.open('https://classroom.google.com/u/1/h')

if choice ==3:
    webbrowser.open('https://classroom.google.com/u/2/h')