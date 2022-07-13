# Function will take in a name and question and print out a magic eight ball style response
import random

# Variables for the magic eightball to print to console
name = "Charles"
question = "Will dinner be fried chicken?"
answer = ""
random_number = random.randint(1, 9)

# Control flow
if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else:
    answer = "Error"

# print result to console
print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)
