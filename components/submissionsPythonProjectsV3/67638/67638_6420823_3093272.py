#each one of these dictionaries represents the internal wiring of one of the enigma's rotors, copied from their real life configurations.
#The rotors are labeled IV, V, and VI as the scrambling wiring is based off those particular real-life rotors, and not because of the order in which they occur.
rotorIV = {
  0:4,
  1:18,
  2:14,
  3:21,
  4:15,
  5:25,
  6:9,
  7:0,
  8:24,
  9:16,
  10:20,
  11:8,
  12:17,
  13:7,
  14:23,
  15:11,
  16:13,
  17:5,
  18:19,
  19:6,
  20:10,
  21:3,
  22:2,
  23:12,
  24:22,
  25:1
}
rotorV = {
  0:21,
  1:25,
  2:1,
  3:17,
  4:6,
  5:8,
  6:19,
  7:24,
  8:20,
  9:15,
  10:18,
  11:3,
  12:13,
  13:7,
  14:11,
  15:23,
  16:0,
  17:22,
  18:12,
  19:9,
  20:16,
  21:14,
  22:5,
  23:4,
  24:2,
  25:10
}

rotorVI = {
  0:9,
  1:15,
  2:6,
  3:21,
  4:14,
  5:20,
  6:12,
  7:5,
  8:24,
  9:16,
  10:1,
  11:4,
  12:13,
  13:7,
  14:25,
  15:17,
  16:3,
  17:10,
  18:0,
  19:18,
  20:23,
  21:11,
  22:8,
  23:2,
  24:19,
  25:22
}
#The UKW (short for the german "Umkehrwalze") is the reflector drum in the machine, functionally a stationary rotor with inputs and outputs only on one side instead of two, which is what allows the encoding and decoding of a message from the same starting settings.
#This one in particular uses the configurations of the "B" reflector, thus the name "UKWB"
UKWB = {
  0:24,
  1:17,
  2:20,
  3:7,
  4:16,
  5:18,
  6:11,
  7:3,
  8:15,
  9:23,
  10:13,
  11:6,
  12:14,
  13:10,
  14:12,
  15:8,
  16:4,
  17:1,
  18:5,
  19:25,
  20:2,
  21:22,
  22:21,
  23:9,
  24:0,
  25:19
}
#This dict simply converts letters to their corresponding number so the machine can run its calculations, and is also used to convert numbers back into text. It also allows for the use of lowercase letters without any errors.
alphToNum = {
  "A":0,
  "B":1,
  "C":2,
  "D":3,
  "E":4,
  "F":5,
  "G":6,
  "H":7,
  "I":8,
  "J":9,
  "K":10,
  "L":11,
  "M":12,
  "N":13,
  "O":14,
  "P":15,
  "Q":16,
  "R":17,
  "S":18,
  "T":19,
  "U":20,
  "V":21,
  "W":22,
  "X":23,
  "Y":24,
  "Z":25,
  "a":0,
  "b":1,
  "c":2,
  "d":3,
  "e":4,
  "f":5,
  "g":6,
  "h":7,
  "i":8,
  "j":9,
  "k":10,
  "l":11,
  "m":12,
  "n":13,
  "o":14,
  "p":15,
  "q":16,
  "r":17,
  "s":18,
  "t":19,
  "u":20,
  "v":21,
  "w":22,
  "x":23,
  "y":24,
  "z":25,
  0:"A",
  1:"B",  
  2:"C",
  3:"D",
  4:"E",
  5:"F",
  6:"G",
  7:"H",
  8:"I",
  9:"J",
  10:"K",
  11:"L",
  12:"M",
  13:"N",
  14:"O",
  15:"P",
  16:"Q",
  17:"R",
  18:"S",
  19:"T",
  20:"U",
  21:"V",
  22:"W",
  23:"X",
  24:"Y",
  25:"Z",
  }
#the switchboard is a manual "swap" of letters in the code, to make it more difficult to crack.
switchBoard = {
  0:0,
  1:1,
  2:2,
  3:3,
  4:4,
  5:5,
  6:6,
  7:7,
  8:8,
  9:9,
  10:10,
  11:11,
  12:12,
  13:13,
  14:14,
  15:15,
  16:16,
  17:17,
  18:18,
  19:19,
  20:20,
  21:21,
  22:22,
  23:23,
  24:24,
  25:25 
}
num=0
message=""
print ("This script is designed to replicate a German naval M3 enigma with rotors IV, V, and VI in the first, second, and third rotor slots respectively, with a UKW-B type reflector and a configurable plugboard.")
print("To encode a message, configure the starting settings of the machine, then type your message.")
print("To decode, simply run the script again using the same starting settings and plug the previously encoded message in.")
print("There is a log under the file name \"67638_6420824_8334768.txt\" to aid in remembering past configurations.")
try:
  startshift1=int(input("Enter the starting position of the first (rightmost) rotor, as an integer: "))%26
  startshift2=int(input("Enter the starting position of the second(center) rotor, as an integer: "))%26
  startshift3=int(input("Enter the starting position of the third(leftmost) rotor, as an integer: "))%26
except ValueError:
  print("please restart and enter a valid starting position for the rotor (Integer).")
  exit()
  
shift1=startshift1 #the startshift series of variables represent the starting positions of their respective enigma rotors and thus remains static, whereas the shift series of variables represents the current position of the enigma rotors as the machine operates, and thus change as the machine operates.
shift2=startshift2  
shift3=startshift3

plugBoardSet=1
while plugBoardSet==1: #the plugboard is a part of the enigma machine that swaps two given letters in the alphabet manually, thus giving even more compmplexity to the code. 
  if input("Are there any letters you want to swap on the switchboard?(Y/N)")=="Y":
    try:
      switchBoard1=alphToNum[input("Enter the first letter: ")]
      switchBoard2=alphToNum[input("Enter the second letter: ")]
      switchBoard[switchBoard1] = switchBoard2
      switchBoard[switchBoard2] = switchBoard1
    except KeyError:
      print("please enter only valid inputs (single letters).")
    
  else:
    plugBoardSet=0
    
def encode(letter,message): #this funcion has a lot of steps, as this is where the encoding happens. It could technically be one line, but for the sake of my sanity, it is not.
    global shift1,shift2,shift3 #these if statements here are responsible for "turning" the rotors for each keypress (letter) that goes through the machine, which is what made it so hard to decode. Notice everything is mod. 26, corresponding to the letters of the alphabet.
    shift1=(shift1+1)%26
    if shift1==15:
        shift2=(shift2+1)%26
        if shift2==0:
            shift3=(shift3+1)%26
    num= (alphToNum[letter]) #converts input letter to number
    num= (switchBoard[num]) #passes number through the switchboard, swapping numbers if applicable.
    num= ((26-shift1)+num)%26 #"rotates" the first rotor and passes from the switchboard to the first rotor .
    num= rotorIV[num] #travels through the first rotor.
    num= ((26-(((26+shift2)-shift1)%26))+num)%26 #"rotates" the second rotor and passes from the first to second rotor by calculating the difference in rotation between the two.
    num= rotorV[num]#travels through the second rotor.
    num= ((26-(((26+shift3)-shift2)%26))+num)%26#"rotates" the third rotor and passes from the second to third rotor by calculating the difference in rotation between the two.
    num= rotorVI[num] #travels through the third rotor.
    num=((26-shift3)+num)%26 #passes from the third rotor to reflector by calculating the difference in rotation between the two.
    num= UKWB[num]#travels through the UKB (stationary reflector drum).
    num= ((26+shift3)+num)%26 #passes from the reflector to the third rotor by calculating the difference in rotation between the two.
    num=(list(rotorVI.keys())[list(rotorVI.values()).index(num)])#travels through the 3rd rotor, in reverse.  
    num= ((26-(((26+shift2)-shift3)%26))+num)%26#"rotates" the second rotor and passes from the third to second rotor by calculating the difference in rotation between the two.
    num=(list(rotorV.keys())[list(rotorV.values()).index(num)]) #travels through the second rotor, in reverse.
    num= ((26-(((26+shift1)-shift2)%26))+num)%26 #"rotates" the first rotor and passes from the second to first rotor by calculating the difference in rotation between the two.
    num=(list(rotorIV.keys())[list(rotorIV.values()).index(num)]) #travels through the first rotor, in reverse.
    num=((26+shift1)+num)%26#travels out of the first rotor, and removes the rotation.
    num=switchBoard[num] #travels one last time into the switchboard
    return (alphToNum[num])#converts the final output number back into a letter.
  
toencode=input("Enter message to encode/decode, using only letters: ")#this is the starting message you want to encode, thus, "toencode".
if toencode.isalpha()==False:
  print("please try again using only the alphabet(A-Z and a-z) when writing messages. Numbers, special characters, and spaces are not encodable.")#as the scrambling can only be done one letter at a time, this script simply passes the messages through the encode function, letter by letter.
  exit()
for char in range (0,len(toencode)):
  letter=toencode[char]
  message+=encode(letter,message)
print ("The encoded/decoded message is: "+message)

f=open("67638_6420824_8334768.txt","a")#from here on, this code writes a file named "enigmalog.txt", then writes (or appends, if the file exists) the starting and ending conditions of the machine, the origional and encoded message, and whether or not there was a mishap in the rotor stepping.
f.writelines("The original message was "+toencode+" and the encoded message was "+message)
f.writelines("\nThe starting rotors were set at the postions "+str(startshift1)+", "+str(startshift2)+", and "+str(startshift3)+", and the switchboard swapped the following letters: \n")
for i in range (len(switchBoard)):
  if i!=switchBoard[i]:
    f.writelines("\n"+str(alphToNum[i])+":"+str(alphToNum[switchBoard[i]]))
f.write("\n[Debug only] During operation, the rotors stepped to the postions "+str(shift1)+", "+str(shift2)+", and "+str(shift3)+" , which is ")
if (startshift1+len(message))%26==shift1:
  f.write("NOMINAL")
else:
  f.write("OFF-NOMINAL")
f.writelines("\n\n* * *\n\n")
f.close()

