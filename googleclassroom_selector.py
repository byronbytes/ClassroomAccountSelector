import webbrowser
import os


print('This works if you have multiple Google accounts.')
os.title('Google Classroom Account Selector')
print('')
os.system('pause')
print('[1] First account signed in')
print('')
print('[2] Second account signed in')
print('')
print('[3] Third account signed in')
print('')
print('[4] Fourth account signed in')
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
