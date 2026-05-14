import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    score  = 0;
# Milestone 1

    # step-1
    # generate random numbers

    # step -2
    # print both numbers 
    # print(f"The computer's number is {computer_number}")
    for i in range(NUM_ROUNDS):
        computer_number = random.randint(1, 100)
        your_number = random.randint(1, 100)
        print(f"Round {i+1}")
        print(f"Your number is {your_number}")

# Milestone 2
        choise = input("Do you think your number is higher or lower than the computer's?: ")

        while choise!= "higher" and choise!= "lower":
            choise = input("Please enter either higher or lower number: ")
# Milestone 3 
        higher_and_correct = choise == "higher" and your_number> computer_number
        lower_and_correct = choise == "lower" and your_number< computer_number
        

        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        print(f"Your score is now {score}")
    if score==5:
        print("Wow! You played perfectly!")
    elif score >NUM_ROUNDS//2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time! ")
        print()
    print("Thanks for playing!")
# Milestone 4
    

if __name__ == "__main__":
    main()