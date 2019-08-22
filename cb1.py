import random
from datetime import *
def randnum(ch):
    if(ch==1):
        dig=2
        flag=0
        level='EASY'
        while(flag==0):
            k=random.randint(10,99)
            if(len(set(str(k)))==2):
                flag=1
    elif(ch==2):
        dig=3
        flag=0
        level='MEDIUM'
        while(flag==0):
            k=random.randint(100,999)
            if(len(set(str(k)))==3):
                flag=1
    else:
        dig=4
        flag=0
        level='HARD'
        while(flag==0):
            k=random.randint(1000,9999)
            if(len(set(str(k)))==4):
                flag=1
    return k
def single():
    print("Enter your name")
    name=input()
    p='y'
    while(p=="y" or p=='Y'):
        file=open("game.txt","a+")
        print("select your level")
        print("1.EASY   2.MEDIUM   3.HARD")
        ch=int(input())
        k=randnum(ch)
        dig=len(str(k))
        if ch==1:
            level='EASY'
        elif ch==2:
            level='MEDIUM'
        else:
            level='HARD'
        #print(k)
        ran=str(k)
        count=0
        f=0
        l=list(ran)
        while(f==0):
            cows=0
            bulls=0
            g=0
            if(count%(dig*3)==0 and count!=0):
                print("Do u want to see the answer press Y else N")
                op=input()
                if op=='Y' or op=='y':
                    g=1
                    print("Secret Number is ",k)
                    print(name," do u want to play again press Y else N")
                    p=input()
                    break
            print("enter ",dig," digit number")
            n=input()
            if n=='-1':
                print("Are u sure to quit game?[y or n]")
                qu=input()
                if qu=='y' or qu=='Y':
                    print("ur secreat number is ",k)
                    p='n'
                    break
            elif len(n)!=dig:
                print("please enter ",dig," digits number only!!!")
            else:
                count+=1
                if n==ran:
                    f=1
                    file.write("Name:%s" % name)
                    file.write("\t")
                    file.write("score:%d" % count)
                    file.write("\t")
                    file.write("level:%s" % level)
                    file.write("\t")
                    file.write("time:%s" % datetime.now())
                    file.write("\n")
                    print("Hurrah!!! u got it ",name)
                    print(name," u guess it in ",count," chances")
                    file.close()
                    f=open('game.txt','r')
                    line=f.readlines()
                    f.close()
                    m=[]
                    k=[]
                    #print(line)
                    for i in line:
                        k.append(i.split('\t'))
                    #print(k)
                    for i in range(len(k)):
                        m.append(k[i][1].split(':'))
                    #print(m)
                    #print(len(k),len(m))
                    s=[]
                    for i in m:
                        s.append(int(i[1]))
                    #s.sort()
                    #print(s)
                    for i in range(len(m)):
                        for j in range(0,len(m)-i-1):
                            if int(s[j])>int(s[j+1]):
                                temp1=s[j]
                                s[j]=s[j+1]
                                s[j+1]=temp1
                                temp=k[j]
                                k[j]=k[j+1]
                                k[j+1]=temp
                    #for i in k:
                        #print(i)
                    l=k[0][0].split(':')
                    d=k[0][1].split(':')
                    print(d[1])
                    if l[1]==name and int(d[1])==count:
                        print("congrats!!! ",name," u r the fastest player to guess")
                    f=open("game.txt","w+")
                    for i in k:
                        for j in range(len(i)-1):
                            f.write(i[j])
                            f.write("\t")
                        f.write(i[-1])
                    f.close()
                    g=1
                else:
                    a=list(n)
                    for i in a:
                        if i in l:
                            if (a.index(i)==l.index(i)):
                                bulls+=1
                            else:
                                cows+=1
                    print("cows are ",cows)
                    print("bulls are ",bulls)
            if g==1:
                    print("\n",name," do u want to play again press Y else N")
                    p=input()
        if p=='n' or p=='N':
                game()
def multi():
    name=[]
    print("Enter player 1 name")
    name.append(input())
    print("Enter player 2 name")
    name.append(input())
    p='y'
    while(p=="y" or p=='Y'):
        print("select your level")
        print("1.EASY   2.MEDIUM   3.HARD")
        ch=int(input())
        k=randnum(ch)
        #print(k)
        dig=len(str(k))
        ran=str(k)
        count=0
        f=0
        l=list(ran)
        while(f==0):
            g=0
            if(count%(dig*3)==0 and count!=0):
                print("Do u want to see the answer press Y else N")
                op=input()
                if op=='Y' or op=='y':
                    g=1
                    print("Secret Number is ",k)
                    break
            for i in name:
                cows=0
                bulls=0
                print(i," enter ",dig," digit number")
                n=input()
                if len(n)!=dig:
                    print("please enter ",dig," digits number only!!! u lost your chance")
                else:
                    count+=1
                    if n==ran:
                        f=1
                        print("Hurrah!!! ",i," got it ")
                        print(i," u guess it in ",count," chances")
                        print(i," u r the winner.")
                        print("\n")
                        g=1
                        break
                    else:
                        a=list(n)
                        for i in a:
                            if i in l:
                                if (a.index(i)==l.index(i)):
                                    bulls+=1
                                else:
                                    cows+=1
                        print("cows are ",cows)
                        print("bulls are ",bulls)
            if g==1:
                print(name[0]," and ",name[1]," do u want to play again press Y else N")
                p=input()
        if p=='n' or p=='N':
                game()
                
def game():
    print('''
          1.START GAME
          2.INSTRUCTIONS
          3.SHOW SCORES
          4.EXIT''')
    choice=int(input())
    file=open("game.txt","a+")
    file.close()
    if choice==1:
        print('''
              1. SINGLE PLAYER
              2. MULTI PLAYER''')
        player=int(input())
        if player==1:
            single()
        else:
            multi() 
            
    elif(choice==2):
        print('''
                                      COWS AND BULLS
             ---------------------------------------------------------------------
                cows and bulls game is a simple number guessing game.The game
                may be played by two friends or two teams with 2-3 members each.
                Here you are playing with system.

                The instructions are:
                 --> With each NEW GAME the app will randomly generate a number
                  based on the level you select.(2-digit or 3-digit or 4-digit).
                  
                 -->The digit will non-repetative.
                 
                 -->Then player tries to guess the number.

                 --> Then the system will gives u the hints in the form of
                     COWS and BULLS.

                     COWS--> If the matching digits in your number and the system
                             generated number are in different positions.
                     BULLS-->If the matching digits in your number and the system
                             generated number are in same positions.

                EXAMPLE:
                 - secret number: 9254
                 - your number  : 9452
                 - Answer : cows are 2 (2,4 are not in correct positions)
                            Bulls are 2 (9,5 are in correct positions)

                ---> Press '-1' whenever you want to quit from game''')
        print("\n")
        print("Press OK to go back to menu")
        ok=input()
        if ok=='ok' or ok=='OK':
            game()
    elif(choice==3):
        fp=open("game.txt","r")
        content=fp.read()
        print(content)
        if(content==""):
            print("No records to display")
        print("Go back to menu press OK")
        flag=0
        while(flag!=1):
            back=input()
            if back=='ok' or back=='OK':
                flag=1
                game()
            else:
                print("please press OK!!!!")
    else:
        exit(1)
print("\n\n")
print("******************************COWS AND BULLS**************************************")
game()
                        
             
            
        
