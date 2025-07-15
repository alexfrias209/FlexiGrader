while True:
    name = input('what is you name? - ')
    if len(name) >= 2:
        print(f"{name} welcome to the animal quiz \n")
        break
    else:
        print("incorrect please type your name")
        continue

import random
from skimage import io
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

#animals you want to do is 
#(1)leopoard, (2)cheetah, (3)tiger, (4)lion, (5)raccoon, (6)deer, (7)elk, (8)lemur, (9)capybara, (10)elephant 
#(11)cougar, (12) bobcat, (13)giraffe, (14)swordfish, (15)bull, (16)fox, (17)coyote, (18)wolf, (19)bison, (20)tuna 

score = 0   

while True:
    print('Which one is a deer?')
    
    picture1 = 'https://tse4.mm.bing.net/th?id=OIP.slQl2NIzEwwck_i6yvFh0wHaFj&pid=Api&P=0&h=220'#deer
    picture2 = 'https://tse2.explicit.bing.net/th?id=OIP.bBu0pD1RhnBOBa07ZJ3a5QHaF7&pid=Api&P=0&h=220' #elk

    img1 = io.imread(picture1)
    img2 = io.imread(picture2)
    fig, ax = plt.subplots(1, 2)

    #displays the first and second image
    ax[0].imshow(img1)
    ax[0].axis('off')
    ax[1].imshow(img2)
    ax[1].axis('off')

    plt.show()

    opt1 = input('type RIGHT or LEFT based on the picture \n')
    if opt1.lower() == 'left'.lower():
        print('Correct! Next Question: \n')
        plt.close()
        score += 1
        break
    else:
            print('Incorrect, please try again.')
            score += 1
            
            
while True:
    print('Which animal is a jaguar?')
    
    picture3 = 'https://tse4.mm.bing.net/th?id=OIP.hkBAnw40v9sWUJz5Z_IY3QAAAA&pid=Api&P=0&h=220'#leopard
    picture4 = 'https://tse3.mm.bing.net/th?id=OIP.lJyh_Jb82-v68lmAAXINOwHaE9&pid=Api&P=0&h=220' #jaguar(correct)

    img3 = io.imread(picture3)
    img4 = io.imread(picture4)
    fig, ax = plt.subplots(1, 2)

    #displays the first and second image
    ax[0].imshow(img3)
    ax[0].axis('off')
    ax[1].imshow(img4)
    ax[1].axis('off')

    plt.show()

    opt2 = input('type RIGHT or LEFT based on the picture \n')
    if opt2.lower() == 'right'.lower():
        print('Correct! Next Question: \n')
        plt.close()
        score += 1
        break
    else:
            print('Incorrect, please try again.')
            score += 1

            
while True:
    print('Which animal is a swordfish?')
    
    picture5 = 'https://tse1.mm.bing.net/th?id=OIP.5zbx4e_-QUSzg9Hb8P1KsAHaEK&pid=Api&P=0&h=220'#tuna
    picture6 = 'https://tse4.mm.bing.net/th?id=OIP.yXj1HjKZEsAWpAGApzI6gQHaE8&pid=Api&P=0&h=220' #swordfish

    img5 = io.imread(picture5)
    img6 = io.imread(picture6)
    fig, ax = plt.subplots(1, 2)

    #displays the first and second image
    ax[0].imshow(img5)
    ax[0].axis('off')
    ax[1].imshow(img6)
    ax[1].axis('off')

    plt.show()

    opt3 = input('type RIGHT or LEFT based on the picture \n')
    if opt3.lower() == 'right'.lower():
        print('Correct! Next Question: \n')
        plt.close()
        score += 1
        break
    else:
            print('Incorrect, please try again.')
            score += 1
            
            
while True:
    print('Which animal is a bull?')
    
    picture7 = 'https://tse4.mm.bing.net/th?id=OIP.94r_1vgXnXNfD5qT9Zn2kwHaE6&pid=Api&P=0&h=220'#bull
    picture8 = 'https://tse3.mm.bing.net/th?id=OIP.PEBNwpcnVn3fl4m4DLaPaQHaEr&pid=Api&P=0&h=220' #heifer

    img7 = io.imread(picture7)
    img8 = io.imread(picture8)
    fig, ax = plt.subplots(1, 2)

    #displays the first and second image
    ax[0].imshow(img7)
    ax[0].axis('off')
    ax[1].imshow(img8)
    ax[1].axis('off')

    plt.show()

    opt4 = input('type RIGHT or LEFT based on the picture \n')
    if opt4.lower() == 'left'.lower():
        print('Correct! Next Question: \n')
        plt.close()
        score += 1
        break
    else:
            print('Incorrect, please try again.')
            score += 1
            
while True:
    print('Which picture is a wolf?')
    
    picture9 = 'https://tse1.mm.bing.net/th?id=OIP.ddc3kpchqvwYXk5VO67rbgHaGD&pid=Api&P=0&h=220'#coyote
    picture10 = 'https://tse2.mm.bing.net/th?id=OIP.EFeun5LFPyqXpnTjm41kjQHaE5&pid=Api&P=0&h=220' #wolf

    img9 = io.imread(picture9)
    img10 = io.imread(picture10)
    fig, ax = plt.subplots(1, 2)

    #displays the first and second image
    ax[0].imshow(img9)
    ax[0].axis('off')
    ax[1].imshow(img10)
    ax[1].axis('off')

    plt.show()

    opt5 = input('type RIGHT or LEFT based on the picture \n')
    if opt5.lower() == 'right'.lower():
        print('Correct! Next Question: \n')
        plt.close()
        score += 1
        break
    else:
            print('Incorrect, please try again.')
            score += 1
            
while True:
    print('which animal is a cougar?')
    
    picture11 = 'https://tse2.mm.bing.net/th?id=OIP.bm2EAboVxmFwSqMXNaVSSgHaEz&pid=Api&P=0'#cougar
    picture12 = 'https://tse2.mm.bing.net/th?id=OIP.GIZDUhOeK-EUo78d9rzICgHaE6&pid=Api&P=0&h=220' #lion

    img11 = io.imread(picture11)
    img12 = io.imread(picture12)
    fig, ax = plt.subplots(1, 2)

    #displays the first and second image
    ax[0].imshow(img11)
    ax[0].axis('off')
    ax[1].imshow(img12)
    ax[1].axis('off')

    plt.show()

    opt6 = input('type RIGHT or LEFT based on the picture \n')
    if opt6.lower() == 'left'.lower():
        print('Correct! Next Question: \n')
        plt.close()
        score += 1
        break
    else:
            print('Incorrect, please try again.')
            score += 1
            
while True:
    print('Which animal is a Bobcat (Double Points!)?')
    
    picture13 = 'https://tse3.mm.bing.net/th?id=OIP.O_xkafi1PgD2TOE9IS0mvgHaHa&pid=Api&P=0&h=220'#Eurasian lynx
    picture14 = 'https://tse2.mm.bing.net/th?id=OIP.XY44DRDwvxrM3lCLbr-Y5wHaE8&pid=Api&P=0&h=220' #bobcat

    img13 = io.imread(picture13)
    img14 = io.imread(picture14)
    fig, ax = plt.subplots(1, 2)

    #displays the first and second image
    ax[0].imshow(img13)
    ax[0].axis('off')
    ax[1].imshow(img14)
    ax[1].axis('off')

    plt.show()

    opt7 = input('type RIGHT or LEFT based on the picture \n')
    if opt7.lower() == 'right'.lower():
        print('Correct! Next Question: \n')
        plt.close()
        score += 2
        break
    else:
            print('Incorrect, please try again.')
            score += 1
            
while True:
    print('Which animal is the Golden Eagle?')
    
    picture15 = 'https://tse1.mm.bing.net/th?id=OIP.qrmKHIQm6_kBaTdwSWpOnQHaJQ&pid=Api&P=0&h=220'#red tailed hawk
    picture16 = 'https://tse4.mm.bing.net/th?id=OIP.qegHjIc1S6QhWpPBLRxoLAHaIN&pid=Api&P=0&h=220' #golden eagle

    img15 = io.imread(picture15)
    img16 = io.imread(picture16)
    fig, ax = plt.subplots(1, 2)

    #displays the first and second image
    ax[0].imshow(img15)
    ax[0].axis('off')
    ax[1].imshow(img16)
    ax[1].axis('off')

    plt.show()

    opt8 = input('type RIGHT or LEFT based on the picture \n')
    if opt8.lower() == 'right'.lower():
        print('Correct! Next Question: \n')
        plt.close()
        score += 1
        break
    else:
            print('Incorrect, please try again.')
            score += 1
            
while True:
    print('Which animal is the African Elephant?')
    
    picture17 = 'https://tse3.mm.bing.net/th?id=OIP.2bRSTDo3Fhw8Oo3Voz7ZaQHaD8&pid=Api&P=0&h=220'#Asian Elephant
    picture18 = 'https://tse4.mm.bing.net/th?id=OIP.OExNct9RMdPE3dck0_jwWgHaE8&pid=Api&P=0&h=220' #African Elephant

    img17 = io.imread(picture17)
    img18 = io.imread(picture18)
    fig, ax = plt.subplots(1, 2)

    #displays the first and second image
    ax[0].imshow(img17)
    ax[0].axis('off')
    ax[1].imshow(img18)
    ax[1].axis('off')

    plt.show()

    opt9 = input('type RIGHT or LEFT based on the picture \n')
    if opt9.lower() == 'right'.lower():
        print('Correct! Next Question: \n')
        plt.close()
        score += 1
        break
    else:
            print('Incorrect, please try again.')
            score += 1
        
while True:
    print('Which Animal is a crocodile?')
    
    picture19 = 'https://tse2.mm.bing.net/th?id=OIP.3yZvdU9aFKTsLQqZ8b5cBAHaE3&pid=Api&P=0&h=220'#crocodile
    picture20 = 'https://tse4.mm.bing.net/th?id=OIP.TpqqU040v7nANuXaLGvWPQHaEo&pid=Api&P=0&h=220' #alligator

    img19 = io.imread(picture19)
    img20 = io.imread(picture20)
    fig, ax = plt.subplots(1, 2)

    #displays the first and second image
    ax[0].imshow(img19)
    ax[0].axis('off')
    ax[1].imshow(img20)
    ax[1].axis('off')

    plt.show()

    opt10 = input('type RIGHT or LEFT based on the picture \n')
    if opt10.lower() == 'left'.lower():
        print('Correct! You have completed the animal quiz: \n')
        plt.close()
        score += 1
        break
    else:
            print('Incorrect, please try again.')
            score += 1

        
print(f"Thank you {name}, for playing the Animal Quiz!")
print(f"Yout total amount of tries were {score} out of 10 minimum tries.")

animal = {'cougar': picture11, 'lion': picture12, 'deer': picture1, 'elk': picture2, 'leopard': picture3, 'jaguar': picture4, 'tuna': picture5,
          'swordfish': picture6, 'bull': picture7, 'heifer': picture8, 'coyote': picture9, 'wolf': picture10, 'cougar': picture11, 'lion': picture12, 'Eurasian Lynx': picture13, 
          'bobcat': picture14, 'red-tailed hawk': picture15,
           'golden eagle': picture16, 'asian elephant': picture17, 'african elephant': picture18, 'crocodile': picture19, 'alligator': picture20}



animal_of_day = random.choice(list(animal.values()))

image = io.imread(animal_of_day)
 
plt.imshow(image)
plt.axis('off')
plt.draw()
plt.pause(1) 
plt.show()

print('your animal of the day is: \n', list(animal.keys())[list(animal.values()).index(animal_of_day)]) 

plt.close()  
