import random as r

#Number_Guessing Game Using Python
print('''\nNumber Guessing Game
\n CHOICES: 
0.NOTE: Please Run This Choice Only Once On The System(It will Generate Score=0)
1.Guess A Number Between 0-100
2.Guess A Number Between Your Choice Of Range
3.ScoreCard
4.To Exit''')
i=5


choice=int(input("\nEnter your choice 0/1/2/3/4: "))

while ((choice!=0)and(choice != 1)and(choice != 2)and(choice != 3)and(choice != 4)):
    choice=int(input("Please Enter A Valid Choice\nEnter a choice from 0/1/2/3/4: "))

if choice==0:
    print("Thanks,Your Score is initialized to 0")
    f=open("Score.txt","w")
    s=str(0)
    f.write(s)
    f.close()

elif choice==1:
    print('''\nComputer will generate a random number from  0-100
You will get five chances to guess the number''')
    num=int(r.random()*100)
    while i>0:
        g=int(input("\nEnter an integer from 0-100: "))
        if g==num:
            f2=open("Score.txt","r+")
            w=f2.read()
            s=int(w[-1])
            s+=1
            f2.write(str(s))
            f2.close()
            print("\nCongratulations\nYOU WIN")
            print("\nYour Score is:",s)
            break

        
        elif g>num:
            
            if num in range(0,25):
                if i != 1:
                    print("HINT: The number is smaller.")
                    print("HINT: Number is in between the range of 0-25")
            if num in range(25,50):
                if i != 1:
                    print("HINT: The number is smaller.")
                    print("HINT: Number is in between the range of 25-50")
            if num in range(50,75):
                if i != 1:
                    print("HINT: The number is smaller.")
                    print("HINT: Number is in between the range of 50-75")
            if num in range(75,100):
                if i != 1:
                    print("HINT: The number is smaller.")
                    print("HINT: Number is in between the range of 75-100")
        
        elif g<num:
            
            if num in range(0,25):
                if i != 1:
                    print("HINT: The number is greater.")
                    print("HINT: Number is in between the range of 0-25")
            if num in range(25,50):
                if i != 1:
                    print("HINT: The number is greater.")
                    print("HINT: Number is in between the range of 25-50")
            if num in range(50,75):
                if i != 1:
                    print("HINT: The number is greater.")
                    print("HINT: Number is in between the range of 50-75")
            if num in range(75,100):
                if i != 1:
                    print("HINT: The number is greater.")
                    print("HINT: Number is in between the range of 75-100")
        i-=1
        if i==0:
            print("\nYOU LOST\nThe Number was",num)


elif choice==2:
    print('''\nRandom numbers will be generated between the range of your choice\n
You have to enter upperlimit,lowerlimit upto which Random numbers will be generated
You will get five chances to guess the number''')
    a=int(input("\nEnter The Lower Limit: "))
    b=int(input("Enter The Upper Limit: "))
    num=r.randint(a,b)
    while i>0:
        g=int(input("Guess a number between Your Choice: "))
        if g==num:
            f2=open("Score.txt","r+")
            w=f2.read()
            s=int(w[-1])
            s+=1
            f2.write(str(s))
            f2.close()
            print("\nCongratulations\nYOU WIN")
            print("\nYour Score is:",s)
            break
        elif g>num:
            if i != 1:
                print("HINT: The number is smaller")
        elif g<num:
            if i != 1:
                print("HINT: The number is greater")
        i-=1
        if i==0:
            print("\nYOU LOST\nThe number was",num)


elif choice==3:
    print("\n2 CHOICES\n1.TO RESET YOUR SCORE\n2.TO CHECK YOUR SCORE")
    ch=int(input("Enter Your Choice: "))
    if ch==1:
        f=open("Score.txt","w")
        s=str(0)
        f.write(s)
        f.close()

    elif ch==2:
        f1=open("Score.txt","r")
        w=f1.read()
        s=w[-1]
        print("Your score is",s)
        f1.close()

elif choice==4:
    print("Thanks For Playing This Game\nMADE BY ABHISEK")
    
input()