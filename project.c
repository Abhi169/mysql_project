#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int i,choices,x,a,num,upper,lower;
    srand(time(NULL));
    i=0;
    int score=0;
    start:
    printf("\n THREE TYPES OF NUMBER GUESSING GAME\n");
    printf("\n SELECT FROM THE FOLLOWING CHOICES:-");
    printf("\n");
    printf("\n1. One digit Number To Guess");
    printf("\n2. Two digit Number To Guess");
    printf("\n3. To generate Number within range of your choice");
    printf("\n4. To check Your Scorecard");
    printf("\n5. To EXIT'-' ");
    printf("\n");
    printf("\nEnter your choice:-");
    scanf("%d",&choices);

    if(choices==1)
    {
        printf("\n");
        printf("You Choose One Digit number To Guess");
        printf("\n");
        printf("\nYOU HAVE THREE CHANCES:-)");
        x = rand()%9;

        while(i<3)
        {
            i++;
            printf("\nGuess One digit Number: ");
            scanf("%d",&a);
            if(x==a){
                ++score;
                printf("\n Congratulations YOU GUESSED it Right! ");
                printf("\n BINGO! YOU WIn! ");break;
            }
            else if(x<a)
            printf("\n HINT: The Number is less than what you think");
            else if(x>a)
            printf("\n HINT: The Number is greater than what you think");
            if(i==3)
            {
                printf("\n");
                printf("\n GAME OVER! ");
                printf("\n The number was %d",x);
            }
            
        }
    }


    if(choices==2)
    {
        printf("\n");
        printf("You Choose Two Digit Number");
        printf("\nHINT: The Number is generally generated less than 50 ");
        printf("\n");
        printf("\nYOU HAVE THREE CHANCES:-)");
        again:
        x=rand()%23;
        if(x==0||x==1||x==2||x==3||x==4||x==5||x==6||x==7||x==8||x==9)
        goto again;

        while(i<3)
        {
            i++;
            printf("\n");
            printf("Enter the two digit number: ");
            scanf("%d",&a);
            if(x==a){
                ++score;
                printf("\n Congratulations YOU GUESSED it Right! ");
                printf("\n BINGO! YOU WIN! ");break;
            }
            else if(x<a)
            printf("\n HINT: The number is less than what you think");
            else if(x>a)
            printf("\n HINT: The number is greater than what you think");

            if(i==3){
                printf("\n");
                printf("\n GAME OVER!");
                printf("\n The number was %d",x);
            }

        }
    }


    if(choices==4){
        printf("\n Your score is %d\n",score);
        goto start;
    }

    
    if(choices==3){
        printf("\n");
        printf("Its User Input Game\n");
        printf("It will generate random number between the range provided by you\n ");
        printf("\n Enter The lower limit:- ");
        scanf("%d",&lower);
        printf("\n Enter The upper limit:- ");
        scanf("%d",&upper);
        printf("\nYou Have Three Chances To Guess ");
        num = (rand() % ( upper - lower + 1 ))+ lower;

        while(i<3)
        {
            i++;
            printf("\n");
            printf("\n Guess The Number Between %d to %d : ",lower,upper);
            scanf("%d",&a);
            if(num==a){
                ++score;
                printf("\n Congratulations YOU GUESSED it Right! ");
                printf("BINGO! YOU WIN ");
                break;
            }
            else if(num>a)
            printf("\n HINT: The number is greater than what you think");

            else if(num<a)
            printf("\n HINT: The number is less than what you think");

            if(i==3){
                printf("\n");
                printf("\n GAME OVER!");
                printf("\n The number was %d",num);
            }
        }
    }


    if(choices==5)
    {
        printf("\n");
        printf(" THANKS FOR PLAYING THE GAME \n Made BY ABHISEK \n");
    }


    else if(i==0||choices==0){
        printf("\n You entered the wrong choice\n ");
        goto start;
    }

    getch();

    return 0;
}