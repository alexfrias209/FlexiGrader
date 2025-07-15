#Personal Athlete Rating Project, Basic inputs, not finished product


#intro to my code
print('Welcome to PAR, your personal athelte rating!')
print('Find out your rating for your desired sport!')
print('\nWhat sport do you play?')
print('\n1. Football\n2. Soccer\n3. Basketball\n4. Volleyball\n5. Baseball\n6. Swim\n7. Tennis\n8. Boxing')
print("\n NOTE: IT'S IMPORTANT YOU ANSWER THESE QUESTIONS HONESTLY FOR THE MOST ACCURATE RESULTS")
#Allows user to choose what sport they play
sport = int(input('Please choose 1 - 8:'))

while sport > 8 or sport < 1:
    print("That's not a sport! Try Again...") # in case the user misinputted their response
    sport = int(input('Please choose 1 - 8:')) # series of questions (5) relevent to the sport will be ask to help code come up with accurate rating
if sport == 1:
    print('You chose Football')
    fspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running a 40 yard dash in 4.8 seconds.'))
    while fspeed > 100:
        print("Try again")
        fspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running a 40 yard dash in 4.8 seconds.'))
    if fspeed >= 75:
        print("You're pretty fast!\nNext question.")
    else:
        print("Next question")
elif sport == 2:
    print('You chose Soccer')
    sspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running a 40 yard dash in 4.8 seconds.'))
    while sspeed > 100:
        print("Try again")
        sspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running a 40 yard dash in 4.8 seconds.'))
    if sspeed >= 75:
        print("You're pretty fast!\nNext question.")
    else:
        print("Next question")
elif sport == 3:
    print('You chose Basketball')
    bspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running the lenght of a basketball court in 4 seconds'))
    while bspeed > 100:
        print("Try again")
        bspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running the lenght of a basketball court in 4 seconds'))
    if bspeed >= 75:
        print("You're pretty fast!\nNext question.")
    else:
        print("Next question")
elif sport == 4:
    print('You chose Volleyball')
    vspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running the entire court in 2.4 seconds.'))
    while vspeed > 100:
        print("Try again")
        vspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running the entire court in 2.4 seconds'))
    if vspeed >= 75:
        print("You're pretty fast!\nNext question.")
    else:
        print("Next question")
elif sport == 5:
    print('You chose Baseball')
    qspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running to first base in 4.3 seconds.'))
    while qspeed > 100:
        print("Try again")
        qspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running to first base in 4.3 seconds.'))
    if qspeed >= 75:
        print("You're pretty fast!\nNext question.")
    else:
        print("Next question")
elif sport == 6:
    print('You chose Swim')
    wspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like swimming a 50m in 28 seconds.'))
    while wspeed > 100:
        print("Try again")
        wspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like swimming a 50m in 28 seconds.'))
    if wspeed >= 75:
        print("You're pretty fast!\nNext question.")
    else:
        print("Next question")
elif sport == 7:
    print('You chose Tennis')
    tspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running the width of a tennis court back and forth in 3 seconds.'))
    while tspeed > 100:
        print("Try again")
        tspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running the width of a tennis court back and forth in 3 seconds.'))
    if tspeed >= 75:
        print("You're pretty fast!\nNext question.")
    else:
        print("Next question")
elif sport == 8:
    print('You chose Boxing')
    xspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running a mile in 6 minutes.'))
    while xspeed > 100:
        print("Try again")
        xspeed = int(input('On a scale of 1-100, how fast are you?\nFor reference, a 75 is like running a mile in 6 minutes.'))
    if xspeed >= 75:
        print("You're pretty fast!\nNext question.")
    else:
        print("Next question")
else:
    print()

# Question #2 

if sport == 1:
    fstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 245 max benchpress.'))
    while fstr > 100:
        print("Try again")
        fstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 245 max benchpress.'))
    if fstr >= 75:
        print("That's impressive!\nNext question.")
    else:
        print("Next question")
elif sport == 2:
    sstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 275 max squat.'))
    while sstr > 100:
        print("Try again")
        sstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 275 max squat.'))
    if sstr >= 75:
        print("That's impressive!\nNext question.")
    else:
        print("Next question")
elif sport == 3:
    bstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 215 max benchpress.'))
    while bstr > 100:
        print("Try again")
        bstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 215 max benchpress.'))
    if bstr >= 75:
        print("That's impressive!\nNext question.")
    else:
        print("Next question")
elif sport == 4:
    vstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 275 max squat.'))
    while vstr > 100:
        print("Try again")
        vstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 275 max squat.'))
    if vstr >= 75:
        print("That's impressive!\nNext question.")
    else:
        print("Next question")
elif sport == 5:
    bbstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 275 max squat.'))
    while bbstr > 100:
        print("Try again")
        bbstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 275 max squat.'))
    if bbstr >= 75:
        print("That's impressive!\nNext question.")
    else:
        print("Next question")
elif sport == 6:
    swstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is being able to bench your body weight \nand squat 1.5x your body weight.'))
    while swstr > 100:
        print("Try again")
        swstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is being able to bench your body weight \nand squat 1.5x your body weight.'))
    if swstr >= 75:
        print("That's impressive!\nNext question.")
    else:
        print("Next question")
elif sport == 7:
    tstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 225 max squat.'))
    while tstr > 100:
        print("Try again")
        tstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is like a 225 max squat.'))
    if tstr >= 75:
        print("That's impressive!\nNext question.")
    else:
        print("Next question")
elif sport == 8:
    bxstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is being able to bench 1.5x your body weight \nand squat 2x your body weight.'))
    while bxstr > 100:
        print("Try again")
        bxstr = int(input('On a scale of 1-100, how strong are you?\nFor reference, a 75 is being able to bench 1.5x your body weight \nand squat 2x your body weight.'))
    if bxstr >= 75:
        print("That's impressive!\nNext question.")
    else:
        print("Next question")
else:
    print()

#Question #3

if sport == 1:
    fend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is being able to last an entire football game on offense, \n a 100 can last an entire game on offense and defense.'))
    while fend > 100:
        print("Try again")
        fend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is being able to last an entire football game on offense, \n a 100 can last an entire game on offense and defense.'))
    if fend >= 75:
        print("Crazzzzyy!\nNext question.")
    else:
        print("Next question")
elif sport == 2:
    send = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to play an entire game,\n a 100 can play an entire game as a fullback.'))
    while send > 100:
        print("Try again")
        send = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to play an entire game,\n a 100 can play an entire game as a fullback.'))
    if send >= 75:
        print("Crazzzzyy!\nNext question.")
    else:
        print("Next question")
elif sport == 3:
    bend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to play an entire game,\n a 100 can play multiple games back to back.'))
    while bend > 100:
        print("Try again")
        bend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to play an entire game,\n a 100 can play multiple games back to back.'))
    if bend >= 75:
        print("Crazzzzyy!\nNext question.")
    else:
        print("Next question")
elif sport == 4:
    vend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to play an entire game,\n a 100 can play multiple games back to back.'))
    while vend > 100:
        print("Try again")
        vend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to play an entire game,\n a 100 can play multiple games back to back.'))
    if vend >= 75:
        print("Crazzzzyy!\nNext question.")
    else:
        print("Next question")
elif sport == 5:
    bbend = int(input('On a scale of 1-100, how well is your muscular endurance?\nFor reference, a 75 is able to play an entire game,\n a 100 can play an entire game as a pitcher.'))
    while bbend > 100:
        print("Try again")
        bbend = int(input('On a scale of 1-100, how well is your muscular endurance?\nFor reference, a 75 is able to play an entire game,\n a 100 can play an entire game as a pitcher.'))
    if bbend >= 75:
        print("Crazzzzyy!\nNext question.")
    else:
        print("Next question")
elif sport == 6:
    swend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to swim a 400m under 4 minutes 30 seconds at a steady pace,\n a 100 can swim a 800m in under 9 minutes.'))
    while swend > 100:
        print("Try again")
        swend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to swim a 400m under 4 minutes 30 seconds at a steady pace,\n a 100 can swim a 800m in under 9 minutes.'))
    if swend >= 75:
        print("Crazzzzyy!\nNext question.")
    else:
        print("Next question")
elif sport == 7:
    tend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to play an entire game with ease,\n a 100 can play multiple games back to back.'))
    while tend > 100:
        print("Try again")
        tend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to play an entire game with ease,\n a 100 can play multiple games back to back.'))
    if tend >= 75:
        print("Crazzzzyy!\nNext question.")
    else:
        print("Next question")
elif sport == 8:
    bxend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to box steadily for a couple rounds,\n a 100 can box steadily for all 12 rounds.'))
    while bxend > 100:
        print("Try again")
        bxend = int(input('On a scale of 1-100, how well is your endurance?\nFor reference, a 75 is able to box steadily for a couple rounds,\n a 100 can box steadily for all 12 rounds.'))
    if bxend >= 75:
        print("Crazzzzyy!\nNext question.")
    else:
        print("Next question")
else:
    print()

#Question #4

if sport == 1:
    fech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to successfully run a route.'))
    while fech > 100:
        print("Try again")
        fech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to successfully run a route.'))
    if fech >= 75:
        print("Great technique!\nNext question.")
    else:
        print("Next question")
elif sport == 2:
    sech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to successfully dribble under pressure.'))
    while sech > 100:
        print("Try again")
        sech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to successfully dribble under pressure.'))
    if sech >= 75:
        print("Great technique!\nNext question.")
    else:
        print("Next question")
elif sport == 3:
    bech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to successfully score 4 free throws in a row.'))
    while bech > 100:
        print("Try again")
        bech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to successfully score 4 free throws in a row.'))
    if bech >= 75:
        print("Great technique!\nNext question.")
    else:
        print("Next question")
elif sport == 4:
    vech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to perfectly pass a free ball, set a clean ball, and make a good strong serve.'))
    while vech > 100:
        print("Try again")
        vech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to perfectly pass a free ball, set a clean ball, and make a good strong serve.'))
    if vech >= 75:
        print("Great technique!\nNext question.")
    else:
        print("Next question")
elif sport == 5:
    bbech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to hit a home run.'))
    while bbech > 100:
        print("Try again")
        bbech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to hit a home run.'))
    if bbech >= 75:
        print("Great technique!\nNext question.")
    else:
        print("Next question")
elif sport == 6:
    swech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to do a 50m butterfly.'))
    while swech > 100:
        print("Try again")
        swech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to do a 50m butterfly.'))
    if swech >= 75:
        print("Great technique!\nNext question.")
    else:
        print("Next question")
elif sport == 7:
    tech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to slice a ball.'))
    while tech > 100:
        print("Try again")
        tech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to slice a ball.'))
    if tech >= 75:
        print("Great technique!\nNext question.")
    else:
        print("Next question")
elif sport == 8:
    bxech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to do the Philly Shell.'))
    while bxech > 100:
        print("Try again")
        bxech = int(input('On a scale of 1-100, how is your technique?\nFor reference, a 75 is being able to do the Philly Shell.'))
    if bxech >= 75:
        print("Great technique!\nNext question.")
    else:
        print("Next question")
else:
    print()

#Question 5#

if sport == 1:
    fexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    while fexp > 100:
        print("Try again")
        fexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    if fexp >= 75:
        print("Woahhh!\nHere's your results!")
    else:
        print("Here's your results!")
elif sport == 2:
    sexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    while sexp > 100:
        print("Try again")
        sexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    if sexp >= 75:
        print("Woahhh!\nHere's your results!")
    else:
        print("Here's your results!")
elif sport == 3:
    bexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    while bexp > 100:
        print("Try again")
        bexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    if bexp >= 75:
        print("Woahhh!\nHere's your results!")
    else:
        print("Here's your results!")
elif sport == 4:
    vexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    while vexp > 100:
        print("Try again")
        vexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    if vexp >= 75:
        print("Woahhh!\nHere's your results!")
    else:
        print("Here's your results!")
elif sport == 5:
    bbexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    while bbexp > 100:
        print("Try again")
        bbexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    if bbexp >= 75:
        print("Woahhh!\nHere's your results!")
    else:
        print("Here's your results!")
elif sport == 6:
    swexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    while swexp > 100:
        print("Try again")
        swexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    if swexp >= 75:
        print("Woahhh!\nHere's your results!")
    else:
        print("Here's your results!")
elif sport == 7:
    texp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    while texp > 100:
        print("Try again")
        texp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    if texp >= 75:
        print("Woahhh!\nHere's your results!")
    else:
        print("Here's your results!")
elif sport == 8:
    bxexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    while bxexp > 100:
        print("Try again")
        bxexp = int(input('On a scale of 1-100, how long have you been playing?\nFor reference, a 75 has played for over 4 years.'))
    if bxexp >= 75:
        print("Woahhh!\nHere's your results!")
    else:
        print("Here's your results!")
else:
    print()

#Final calculation to determine player's overall rating
if sport == 1:
   fsum = (2 * fspeed + 2* fstr + fend + fech + fexp)/7
   print("Your overall rating as a Football player is ", f'{fsum:.2f}')
elif sport == 2:
    fsum = (2 * sspeed + sstr + 2 * send + sech + sexp)/7
    print("Your overall rating as a Soccer player is ", f'{fsum:.2f}')
elif sport == 3:
    fsum = (2 * bspeed + bstr + 2 * bend + 2 * bech + bexp)/8
    print("Your overall rating as a Basketball player is ", f'{fsum:.2f}')
elif sport == 4:
    fsum = (vspeed + vstr + vend + 2 * vech + 2 * vexp)/7
    print("Your overall rating as a Volleyball player is ", f'{fsum:.2f}')
elif sport == 5:
    fsum = (2 * qspeed + bbstr + fend + 2 * bbech + bbexp)/7
    print("Your overall rating as a Baseball player is ", f'{fsum:.2f}')
elif sport == 6:
    fsum = (2 * wspeed + swstr + 2 * swend + 2 * swech + swexp)/8
    print("Your overall rating as a Swimmer is ", f'{fsum:.2f}')
elif sport == 7:
    fsum = (2 * tspeed + tstr + tend + 2 * tech + texp)/7
    print("Your overall rating as a Tennis player is ", f'{fsum:.2f}')
elif sport == 8:
    fsum = (2 * xspeed + 2 * bxstr + 2 * bxend + 2 * bxech + 2 * bxexp)/10
    print("Your overall rating as a Boxer is ", f'{fsum:.2f}')
else:
    print()
