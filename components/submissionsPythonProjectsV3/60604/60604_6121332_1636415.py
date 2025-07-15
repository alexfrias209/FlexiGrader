import os
import random
import matplotlib.pyplot as plt
print('This code can only simulate gacha result for games listed uder this sentence:',"(only avaliable for Arknight)")
print('Genshin/Honkai: star rail')
print('Arknight')
print('Azur lane')
print('Umamusume: Pretty Derby')
game_name = str(input('Select your game: '))
print('')
if game_name == 'Genshin':
    print('character or weapon')
elif game_name == 'Honkai: star rail':
    print('character or weapon')
elif game_name == 'Arknight' or game_name == 'arknight':
    total_roll=0
    rolled = []
    characteryouget = []
    characteryougot = []
    charactersyouget = []
    sixstarnum = 0
    fivestarnum = 0
    fourstarnum = 0
    threestarnum = 0
    start_roll = str(input('Start rolling? '))
    while start_roll.lower() != 'no':
        arc_roll = int(input('How many rolls: '))
        print('')
        total_roll= total_roll + arc_roll
        filesixstar = open('1.txt')
        contents = filesixstar.read()
        six_star = contents.split(',')
        filefivestar = open('5stararknights.txt')
        fivestar = filefivestar.read()
        five_star = fivestar.split(',')
        filefourstar = open('fourstararknight.txt')
        fourstar = filefourstar.read()
        four_star = fourstar.split(',')
        filethreestar = open('threestararknights.txt')
        threestar = filethreestar.read()
        three_star = threestar.split(',')
        characterlist=['sixstars','fivestars','fourstars','threestars']
        i=0
        while i <= arc_roll:
          rolled = random.choices(characterlist, weights = [0.02891,0.08948,0.4999,0.3817])
          i+=1
          characteryouget.append(rolled)
          sixstarcharacteryouget = 'sixstars'
          fivestarcharacteryouget = 'fivestars'
          fourstarcharacteryouget = 'fourstars'
          threestarcharacteryouget = 'threestars'
          for index, string in enumerate(rolled):
              if string == sixstarcharacteryouget:
                  sixstars = random.choices(six_star)
                  characteryougot.append(sixstars)
                  sixstarnum+=1
              elif fivestarcharacteryouget in rolled:
                  fivestars = random.choices(five_star)
                  characteryougot.append(fivestars)
                  fivestarnum+=1 
              elif fourstarcharacteryouget in rolled:
                  fourstars = random.choices(four_star)
                  characteryougot.append(fourstars)
                  fourstarnum+=1
              elif threestarcharacteryouget in rolled:
                  threestars = random.choices(three_star)
                  characteryougot.append(threestars)
                  threestarnum+=1
        print(characteryougot)
        file_name = "result.txt"
        delimiter = ","
        with open("result.txt", "a") as file:
          text_to_append = str(characteryougot)
          file.write(text_to_append)
        keep_rolling = str(input('Keep rolling? '))
        characteryougot = []
        if keep_rolling == 'no':
          print('You have rolled',total_roll,'time')
          file_name ='result.txt'
          with open(file_name, "r") as file:
              file_content = file.read()
              print('You get: ',file_content)
          categories = ['six stars', 'five stars', 'four stars','three stars']
          values = [sixstarnum,fivestarnum,fourstarnum,threestarnum]
          plt.bar(categories, values)
          plt.xlabel('Categories')
          plt.ylabel('Values')
          plt.title('character you get in this roll')
          plt.show()
          file_path = 'result.txt'

          with open(file_path, 'r') as file:
              file_contents = file.readlines()
          content_to_remove = "delete"
          new_file_contents = [line for line in file_contents if content_to_remove not in line]
          with open(file_path, 'w') as file:
              file.writelines(new_file_contents)
          break
elif game_name == 'Azur lane':
    print('There are three pools, light(1), heavy(2), special(3), and current event(4)')
    al_pool = str(input('Which pool? '))
    print('')
    if al_pool == 'light':
        start_roll = str(input('Start rolling? '))
        while start_roll !='No' or start_roll !='no':
            arc_roll = int(input('How many rolls: '))
            print('')
            total_roll= total_roll + arc_roll
            ssr = ['a1','b1','c1']
            sr = ['d1','e1','f1']
            r = ['g1','h1']
            C = ['i1','j1']
            characterlist = [random.choice(ssr),random.choice(sr),random.choice(r),random.choice(c)]
            print(random.choices(characterlist, weights = [7,12,51,30],k = arc_roll))
            keep_rolling = str(input('Keep rolling? '))
            if keep_rolling == 'no':
                print('You have rolled',total_roll,'time')
                break
    elif al_pool == 'heavy':
        start_roll = str(input('Start rolling? '))
        while start_roll !='No' or start_roll !='no':
            arc_roll = int(input('How many rolls: '))
            print('')
            total_roll= total_roll + arc_roll
            ssr = ['a','b','c']
            sr = ['d','e','f']
            r = ['g','h']
            C = ['i','j']
            characterlist = [random.choice(ssr),random.choice(sr),random.choice(r),random.choice(c)]
            print(random.choices(characterlist, weights = [2,8,50,40],k = arc_roll))
            keep_rolling = str(input('Keep rolling? '))
            if keep_rolling == 'no':
                print('You have rolled',total_roll,'time')
                break
    elif al_pool == 'special':
        start_roll = str(input('Start rolling? '))
        while start_roll !='No' or start_roll !='no':
            arc_roll = int(input('How many rolls: '))
            print('')
            total_roll= total_roll + arc_roll
            ssr = ['a','b','c']
            sr = ['d','e','f']
            r = ['g','h']
            C = ['i','j']
            characterlist = [random.choice(ssr),random.choice(sr),random.choice(r),random.choice(c)]
            print(random.choices(characterlist, weights = [7,12,51,30],k = arc_roll))
            keep_rolling = str(input('Keep rolling? '))
            if keep_rolling == 'no':
                print('You have rolled',total_roll,'time')
                break
    elif al_pool == 'current event':
        start_roll = str(input('Start rolling? '))
        while start_roll !='No' or start_roll !='no':
            arc_roll = int(input('How many rolls: '))
            print('')
            total_roll= total_roll + arc_roll
            ur = ['z']
            ssr = ['a','b','c']
            sr = ['d','e','f']
            r = ['g','h']
            C = ['i','j']
            characterlist = [ur,random.choice(ssr),random.choice(sr),random.choice(r),random.choice(c)]
            print(random.choices(characterlist, weights = [2,5,12,51,30],k = arc_roll))
            keep_rolling = str(input('Keep rolling? '))
            if keep_rolling == 'no':
                print('You have rolled',total_roll,'time')
                break
elif game_name == 'Umamusume: Pretty Derby':
    print('How many rolls: ')
else:
    print('invaild input')
