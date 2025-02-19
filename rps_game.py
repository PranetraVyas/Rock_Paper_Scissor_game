import random

print('Welcome to the Rock paper scissor game')

while True:
    print('Enter a choice :\n1-Rock\n2-Paper\n3-Scissor:')
    user = int(input())
    
    while user > 3 or user < 1:
        print('Wrong choice ! Please try again .\n choose numbers between 1 and 3')
    
    if user == 1:
        user_choice = 'Rock'
    elif user == 2:
        user_choice = 'Paper'
    elif user == 3:
        user_choice = 'Scissor'
                        
    comp = random.randint(1,3)
        
    if comp == 1:
        comp_choice = 'Rock'
    elif comp == 2:
        comp_choice = 'Paper'
    elif comp == 3:
        comp_choice  = 'Scissor' 
        
    print('computer choice is :',comp_choice)
    print(user_choice,'vs',comp_choice)
        
    if user == comp:
        output = 'd'
    elif (user == 1 and comp == 3) or (comp == 1 and user == 3):
        output = 'Rock'
    elif (user == 2 and comp == 1) or (comp == 2 and user == 1):
        output = 'Paper'        
    elif (user == 3 and comp == 2) or (comp == 3 and user == 2):
        output = 'Scissor'
            
    if output == 'd':
        print('Its a draw')
    elif output == user_choice:
        print('You win')
    else:
        print('You lose :(')
            
    print('Do you want to play again ?(N/Y)')
    ans = input().lower()
    if ans == 'n':
        break
        

print("Thanks for playing!")                
         
        
                  
            
    
      
            
