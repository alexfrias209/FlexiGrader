scores = []

with open("59566_6417289_9083822.txt", "r") as file:
    for line in file:
        parts = line.strip().split(',')
        for part in parts:
            #scores.append(int(part(strip())))
            print(part)

#print(f"Current score: computer - {scores[0]}User - {scores[0]}")

#computer_score = 0
#user_score = 0
#with open("mode.txt", "w") as file:
    #file.write("Computer, User\n")
    #file.write(f"{computer_score}, {user_score}\n)
