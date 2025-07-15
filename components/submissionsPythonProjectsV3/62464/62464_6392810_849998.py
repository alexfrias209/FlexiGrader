# code requires a file with player data to function
infile = "62464_6392809_1479824.csv"

f = open(infile, "r")

total_at_bats = 0
total_walks = 0
total_singles = 0
total_doubles = 0
total_triples = 0
total_home_runs = 0
total_chances1 = 0
total_errors = 0

header = f.readline()

for line in f.readlines():
    columns = line.split(",")

    if len(columns) >= 10:
        at_bats = int(columns[2])
        walks = int(columns[3])
        singles = int(columns[4])
        doubles = int(columns[5])
        triples = int(columns[6])
        home_runs = int(columns[7])
        total_chances = int(columns[8])
        errors = int(columns[9])

        total_at_bats += at_bats
        total_walks += walks
        total_singles += singles
        total_doubles += doubles
        total_triples += triples
        total_home_runs += home_runs
        total_chances1 += total_chances
        total_errors += errors


def hits(single, double, triple, home):
    h = single + double + triple + home
    return h

def ba_avg(hits, atbats):
    avg = hits / atbats
    return avg

def slugging(single, double, triple, home, atbats):
    totl1 = double * 2
    totl2 = triple * 3
    totl3 = home * 4
    totals = single + totl1 + totl2 +totl3
    slugs = totals / atbats
    return slugs

def onbase(hits, walks, atbats):
    bases = hits + walks
    base1 = bases / atbats
    return base1

def ops(onbase, slug):
    opes = onbase + slug
    return opes

def field(errors, chances):
    fel = errors / chances
    fel = 1 - fel
    return fel 
first_choice = ()

print('Welcome to my project on Baseball Player Analysis, which should allow users to input hitter data, which then allows the project output more information about certain player and teams stats.')
print('Developed by Nicolas Perez Yen')
print()
while first_choice != 5:
    print()
    first_choice = input(f'Be sure to import player information prior to determining data. Which stat are you looking for?'
    '\n1. Team Hitting stats'
    '\n2. Player hitting stats'
    '\n3. Team fielding stats'
    '\n4. Player fielding stats'
    '\n5. Exit'
    '\nEnter a number: ')
    first_choice = int(first_choice)

    if first_choice == 1:
        team = input('Pick information you would like to see.'
        '\na. Team Total Hits'
        '\nb. Team Batting Average'
        '\nc. Team Slugging'
        '\nd. Team On Base Percentage'
        '\ne. Team OPS'
        '\nEnter lowercase letter: ')
    elif first_choice == 2:
        fname = input("Enter the first name of the player: ")
    elif first_choice == 3:
        team_field = input('Pick information you would like to see.'
        '\na. Team Fielding Percentage'
        '\nb. Team Total Errors'
        '\nEnter lowercase letter: ')                 
    elif first_choice == 4:
        pname = input("Enter the first name of the player: ")
    elif first_choice == 5:
        exit()
    else:
        print('Please choose one of the options')


    if first_choice == 1:    
        if team == 'a':
            hitter = hits(total_singles, total_doubles, total_triples, total_home_runs)
            print(f'The team has a total of {hitter} hits this season')
        if team == 'b':
            hitter = hits(total_singles, total_doubles, total_triples, total_home_runs)
            batter = ba_avg(hitter, total_at_bats)
            print(f'The team has a batting average of {batter:.3f}')
        if team == 'c':
            sluggers = slugging(total_singles, total_doubles, total_triples, total_home_runs, total_at_bats)
            print(f'The team has a slugging percentage of {sluggers:.3f}')
        if team == 'd':
            hitter = hits(total_singles, total_doubles, total_triples, total_home_runs)
            basers = onbase(hitter, total_walks, total_at_bats)
            print(f'The team has an on base percentage of {basers:.3f}')
        if team == 'e':
            hitter = hits(total_singles, total_doubles, total_triples, total_home_runs)
            basers = onbase(hitter, total_walks, total_at_bats)
            sluggers = slugging(total_singles, total_doubles, total_triples, total_home_runs, total_at_bats)
            opers = ops(basers, sluggers)
            print(f'The team has an OPS (On base plus slugging percentage) of {opers:.3f}')


    if first_choice == 2:
        f.seek(0)  
        for line in f.readlines():
            columns = line.split(",")  
            if len(columns) >= 10:
                first_name = columns[0]
                last_name = columns[1]
                
                if first_name.lower() == fname.lower():
                    at_bats = int(columns[2])
                    walks = int(columns[3])
                    singles = int(columns[4])
                    doubles = int(columns[5])
                    triples = int(columns[6])
                    home_runs = int(columns[7])
                    total_chances = int(columns[8])
                    errors = int(columns[9])
                    hitter1 = hits(singles, doubles, triples, home_runs)
                    batter1 = ba_avg(hitter1, at_bats)
                    basers1 = onbase(hitter1, walks, at_bats)
                    sluggers1 = slugging(singles, doubles, triples, home_runs, at_bats)
                    opers1 = ops(basers1, sluggers1)
                    
                    print(f'\nPlayer: {first_name} {last_name}')
                    pname2 = input(f'Please input which stat you would like to see.'
                                '\na. Player Total Hits'
                                '\nb. Player Batting Average'
                                '\nc. Player Slugging'
                                '\nd. Player On Base Percentage'
                                '\ne. Player OPS'
                                '\nEnter lowercase letter: ')
    if first_choice == 2:
        if pname2 == 'a':
            print(f'{fname} has {hitter1} hits this season')
        elif pname2 == 'b':
            print(f'{fname} has a batting average of {batter1:.3f}')
        elif pname2 == 'c':
            print(f'{fname} has a slugging percentage of {sluggers1:.3f}')
        elif pname2 == 'd':
            print(f'{fname} has an on base percentage of {basers1:.3f}')
        elif pname2 == 'e':
            print(f'{fname} has an OPS (on base plus slugging percentage) of {opers1:.3f}')
        else:
            print('Please choose one of the options')


    if first_choice == 4:
        f.seek(0)
        for line in f.readlines():
            columns = line.split(",")
                    
            if len(columns) >= 10:
                first_name = columns[0]
                last_name = columns[1]

                if first_name.lower() == pname.lower():
                    total_chances = int(columns[8])
                    errors = int(columns[9])
                    errors1 = field(errors, total_chances)

                    print(f'\nPlayer: {first_name} {last_name}')

                    pname3 = input(f'Please input which stat you would like to see.'
                            '\na. Player Fielding Percentage'
                            '\nb. Player Errors'
                            '\nEnter lowercase letter: ')
    if first_choice == 4:
        if pname3 == 'a':
            print(f'{pname} has a fielding percentage of {errors1}')
        elif pname3 == 'b':
            print(f'{pname} has made {errors} errors this season')
        else:
            print('Please choose one of the options')

                        
    if first_choice == 3:
        if team_field == 'a':
            fielders = field(total_errors, total_chances1)
            print(f'The team has a fielding percentage of {fielders:.3f}')
        if team_field == 'b':
            print(f'The team has made a total of {total_errors} errors')

f.close()
