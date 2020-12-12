#!/usr/bin/python3

import os
os.system("clear")
banner="""



              A:::A                                    ttt:::t                                                                   i::::i 
             A:::::A                                   t:::::t                                                                    iiii  
            A:::::::A                                  t:::::t                                                                          
           A:::::::::A         nnnn  nnnnnnnn    ttttttt:::::ttttttt   rrrrr   rrrrrrrrr      ooooooooooo   ppppp   ppppppppp   iiiiiii 
          A:::::A:::::A        n:::nn::::::::nn  t:::::::::::::::::t   r::::rrr:::::::::r   oo:::::::::::oo p::::ppp:::::::::p  i:::::i 
         A:::::A A:::::A       n::::::::::::::nn t:::::::::::::::::t   r:::::::::::::::::r o:::::::::::::::op:::::::::::::::::p  i::::i 
        A:::::A   A:::::A      nn:::::::::::::::ntttttt:::::::tttttt   rr::::::rrrrr::::::ro:::::ooooo:::::opp::::::ppppp::::::p i::::i 
       A:::::A     A:::::A       n:::::nnnn:::::n      t:::::t          r:::::r     r:::::ro::::o     o::::o p:::::p     p:::::p i::::i 
      A:::::AAAAAAAAA:::::A      n::::n    n::::n      t:::::t          r:::::r     rrrrrrro::::o     o::::o p:::::p     p:::::p i::::i 
     A:::::::::::::::::::::A     n::::n    n::::n      t:::::t          r:::::r            o::::o     o::::o p:::::p     p:::::p i::::i 
    A:::::AAAAAAAAAAAAA:::::A    n::::n    n::::n      t:::::t    ttttttr:::::r            o::::o     o::::o p:::::p    p::::::p i::::i 
   A:::::A             A:::::A   n::::n    n::::n      t::::::tttt:::::tr:::::r            o:::::ooooo:::::o p:::::ppppp:::::::pi::::::i
  A:::::A               A:::::A  n::::n    n::::n      tt::::::::::::::tr:::::r            o:::::::::::::::o p::::::::::::::::p i::::::i
 A:::::A                 A:::::A n::::n    n::::n        tt:::::::::::ttr:::::r             oo:::::::::::oo  p::::::::::::::pp  i::::::i
AAAAAAA                   AAAAAAAnnnnnn    nnnnnn          ttttttttttt  rrrrrrr               ooooooooooo    p::::::pppppppp    iiiiiiii
                                                                                                             p:::::p                    
                                                                                                             p:::::p                    
                                                                                                            p:::::::p                   
                                                                                                            p:::::::p                   
                                                                                                            p:::::::p                   
                                                                                                            ppppppppp                   
                                                                            İnstagram:Antropifix
                                                                            Discord:Antropi#5923
  
  """
print(banner)
def nmap_target():
  target=input("Hedefiniz Nedir ====>")
  os.system("nmap -sV"+target)
def sql_target():
  target=input("Hedefiniz Nedir ====>")
  os.system("sqlmap -u"+target)
def msf_target():
  target=input("Entere Bas: ")
  os.system("msfconsole"+target)
def wlan_target():
  target=input("Entere Bas: ")
  os.system("sudo airmon-ng start wlan0"+target)
def mon_target():
  target=input("Entere Bas: ")
  os.system("sudo airmon-ng stop wlan0mon"+target)
def discover_target():
  target=input("Entere Bas: ")
  os.system("sudo netdiscover"+target)
def tool_target():
  target=input("Entere Bas: ")
  os.system("sudo setoolkit"+target)
def beef_target():
  target=input("Entere Bas: ")
  os.system("sudo beef-xss"+target)





print("[1] Nmap Taraması Yapmak")
print("[2] Sql Açıklı Site Bulucu")
print("[3] Msfconsole Açar")
print("[4] Monitör Modu Açar")
print("[5] Monitör Modu Kapatır")
print("[6] İnternete Kimler Bağlı Gösterir İpleri Dahil")
print("[7] Social Engineering Toolkit")
print("[8] Beef i Açar")
selection=input("Hangi Seçeneği seçmek istersiniz ====>")
if selection == "1":
  nmap_target()  
elif selection =="2":
  sql_target()
elif selection =="3":
  msf_target()
elif selection =="4":
  wlan_target()
elif selection =="5":
  mon_target()
elif selection =="6":
  discover_target()
elif selection =="7":
  tool_target()
elif selection =="8":
  beef_target()
else:
  input()  
