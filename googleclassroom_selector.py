import webbrowser
import os


print('If you have multiple Google Accounts this is meant for you.')
os.title('Google Classroom Selector')
print('')
os.system('pause')
print('[1] Default User / First Google Account Signed In')
print('')
print('[2] Second User / Second Google Account Signed In')
print('')
print('[3] Third User / Third Google Account Signed In')
print('')
print('[4] Fourth User / Fourth Google Account Signed In')
print('')
choice = int(input())

if choice == 1:
    webbrowser.open('https://classroom.google.com/u/0/h')

if choice ==2:
    webbrowser.open('https://classroom.google.com/u/1/h')

if choice ==3:
    webbrowser.open('https://classroom.google.com/u/2/h')

if choice ==4:
    webbrowser.open('https://classroom.google.com/u/3/h')