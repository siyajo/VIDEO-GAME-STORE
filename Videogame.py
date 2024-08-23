import pickle as pic
import os

def MainMenu():
    print('!************************************!')
    print('!  >>>>>>>>VIDEO GAME STORE<<<<<<<<  !')
    print('!                                    !')
    print('!             MAINTENANCE            !')
    print('! 1-VIEW                             !')
    print('! 2-ADD                              !')
    print('! 3-MODIFY                           !')
    print('! 4-DELETE                           !')
    print('!************************************!')
    print('!             TRANSACTION            !')
    print('! 5-RETAIL                           !')
    print('! 6-WHOLESALE                        !')
    print('!************************************!')
    print('! 7-EXIT                             !')
    print('!************************************!')
    
while True:
    MainMenu()
    ch=int(input('Enter your choice : '))
    
    if ch==1:
        def view():
            g=open('Videogame.dat','rb')
            sn=int(input('Enter sno :'))
            found=0
            try:
                while True:
                    r=pic.load(g)
                    if sn==r[0]:
                        print('Name of Game : ',r[1])
                        print('Price : ',r[2])
                        print('Availability : ',r[3])
                        found=1
                        break
            except:
                g.close()
            if found==0:
                print('Please enter the appropriate game choice.')
        view()
            
    elif ch==2:
        def add():
            h=open('Videogame.dat','ab')
            r=[]
            asn=int(input('Enter sno.(10 and above): '))
            aname=input('Enter Name of Game : ')
            aprice=int(input('Enter Price : '))
            aavail=input('Enter Availability : ')
            r=[asn,aname,aprice,aavail]
            pic.dump(r,h)
            h.close()
        add()
                      
    elif ch==3:
        m=int(input('Enter the item number:'))
        def modify(n):
            f1=open('Videogame.dat','rb')
            f2=open('Temp.dat','wb')
            
            try:
                found=0
                while True:
                    r=pic.load(f1)
                    gno=r[0]
                    gname=r[1]
                    npri=r[2]
                    ava=r[3]
                    if gno==m:
                            found=1
                            print('Name of the game:',r[1])
                            print('Price of game:',r[2])
                            print('Availability:',r[3])
                            a=input('Modify game name(y/n)?:')
                            if a=='y':
                                gname=input('Enter modified name:')
                            b=input('Modify price(y/n)?:')
                            if b=='y':
                                npri=int(input("Enter new price:"))
                            c=input('Modify availability(y/n)?:')
                            if c=='y':
                                ava=input('Enter the availability(Y or N):')
                            r=[gno,gname,npri,ava]
                            pic.dump(r,f2)
                            print('Record Modified')
                            if a=='n' and b=='n' and c=='n':
                                print('Record not modified')
            except:
                pass
            
            if found==1:
                f1.close()
                f2.close()
            else:
                print('Record not found')
        modify(m)
    elif ch==4:
        s=int(input('Enter the item number:'))
        def delete(t):
            v1=open('Videogame.dat','rb')
            v2=open('Tempp.dat','wb')
            try:
                found=0
                while True:
                    r=pic.load(v1)
                    gno=r[0]
                    gname=r[1]
                    npri=r[2]
                    ava=r[3]
                    if gno==t:
                            found=1
                            print('Name of the game:',r[1])
                            print('Price of game:',r[2])
                            print('Availability:',r[3])
                            ask=input('Delete game(y/n)?:')
                            if ask=='y':
                                ld=[gno,gname,npri,ava]
                            pic.dump(ld,v2)
                            print('Record Deleted')
                            if ask=='n':
                                print('Record not Deleted')
            except:
                pass
            if found==1:
                v1.close()
                v2.close()
            else:
                print('Record not found')        
        delete(s)
    elif ch==5:
        def retail():
            l=open('Videogame.dat','rb')
            n=int(input('Enter item number :'))
            found=0
            try:
                while True:
                    r=pic.load(l)
                    gno=r[0]
                    gname=r[1]
                    npri=r[2]
                    ava=r[3]
                    if n==gno:
                        print('Name of Game : ',gname)
                        print('Price : ',npri)
                        print('Availability : ',ava)
                        found=1
                        m=int(input('Enter the quantity:'))
                        if m < 10:
                            dis=0
                            print('Total Price:',npri*m)
                            print('Discount Amount:',dis)
                            print('Payable Amount:',(npri*m)+dis)
                            print('Thank You!')
                        else:
                            print('Quantity more than 9-please choose wholesale option')
                        
            except:
                pass
            if found==0:
                print('Record Not Found')
            
        retail()
    elif ch==6:
         def wholesale():
            k=open('Videogame.dat','rb')
            sw=int(input('Enter the item number:'))
            found=0
            try:
                while True:
                    r=pic.load(k)
                    if sw==r[0]:
                        print('Name of Game : ',r[1])
                        print('Price : ',r[2])
                        print('Availability : ',r[3])
                        found=1
                        break
            except:
                k.close()
            pw=int(input('Enter price : '))
            qw=int(input('Enter the quantity : '))
            if qw>=10:
                print('Total price : ',pw*qw)
                disc=(0.1)*(pw*qw)
                discamt=(pw*qw)-disc
                print('Discount amount(10%) : ',disc)
                print('Payable amount : ',discamt)
            else:
                print('Quantity less than 10 - please choose retail option.')
            if found==0:
                print('Please enter the appropriate game choice.')
         wholesale()
    elif ch==7:
        break
