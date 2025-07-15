import datetime
from datetime import date
from datetime import datetime

print('Hello I am the developer')

league = input('What is your favorite soccer league:')
leagues = ['Premier League', 'La Liga', 'Serie A', 'MLS', 'Ligue one', 'Liga Mx', 'Bundesliga']

if leagues[0] == league:
    print('one of the best leagues if not the best one')
elif leagues[1] == league:
    print('Oh the spanish league is amazing, Visca Barca')
elif leagues[2] == league:
    print('The italian league has some good players')
elif leagues[3] == league:
    print('You must love watching Messi huh')
elif leagues[4] == league:
    print('France is alright I guess, you have Mbappe')
elif leagues[5] == league:
    print('Chivas or nothing else')
elif leagues[6] == league:
    print('Bayern wins every year watch something else, yabba dabba dooo')
else:
    print('Oh no at the moment we do not have that league in our system')

team = input('What is your favorite team from that league:')
great = 'Barcelona'
score = 0
while team != great:
    score += 1
    print("That's a pretty great team but I prefer Barca,", score, "")
    break
else:
    score += 1
    print('I like Barca too amazing choice,', score)


def main():
    today = datetime.today()
    print('Thank you for taking this short questionare on', today)


today = date.today()
print('Today:', today.day, 'Month: ', today.month)
if __name__ == "__main__":
    main()
