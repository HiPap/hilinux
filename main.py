import os
import pyfiglet
import time


from colorama import Fore

asciibanner = pyfiglet.figlet_format('HILINUX!')

def main():

 print(Fore.GREEN + asciibanner)
 choice = input(Fore.GREEN + ''' 
 --CATEGORIES--
 1)Cover your tracks!
 2)Change root password!
 3)Install all libraries (MAIN FILE NEEDS TO BE ON DESKTOP)

 -------------- 
 ==> ''')
 if choice == '1':
     print('''
     --COVER YOUR TRACKS!--
     1)Kill current session
     2)Clear session history
     3)Disable history logging (YOU NEED TO LOGOUT AND RESTART!)
     4)Set history max lines to 0!
     5)Go back to main menu!
     ''')
     covertrack = input('==> ')
     
     if covertrack == '1':
        os.system('kill -9 $$')
        main()
    
     if covertrack == '2':
         os.system('history -c')
         main()
    
     if covertrack == '3':
         os.system('unset HISTFILE')
         main()
     
     if covertrack == '4':
         os.system('export HISTFILESIZE=0')
         main()

     if covertrack == '5':
         main()
 
 if choice == '2':
     os.system('sudo su') 
     print('You have 5 seconds to change your password!')
     time.sleep(5)
     os.system('passwd')
     main()

 if choice == '3':
    os.system('cd Desktop')
    os.system('cd hilinux')
    os.system('pip install -r requirements')
    main() 
main()
 





