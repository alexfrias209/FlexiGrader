#function calls csv file
import csv
import matplotlib.pyplot as plt

#function to update the original csv file with the new data from input of the code
def append_to_csv(steak, doneness):
    with open('61676_6418621_6866897.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([steak, doneness])

#function to read the csv file and return the data in the form of a graph, creates graph
def plot_frequency(data, title, xlabel):
  print(data.keys(), data.values())
  plt.bar(data.keys(), data.values())
  plt.title(title)
  plt.xlabel(xlabel)
  plt.ylabel('Frequency')
  plt.xticks(rotation=45)  
  plt.tight_layout() 
  plt.show()

#dictionary function to read csv file to list count of steak and steak doneness
def get_frequencies(column_index):
    frequencies = {}
    with open('61676_6418621_6866897.csv', 'r') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for row in csvFile:
            if row[column_index] in frequencies:
                frequencies[row[column_index]] += 1
            else:
                frequencies[row[column_index]] = 1
    return frequencies


# main code begins on line 37
print("Hello! Welcome to the Steak Cooker.")
print("Order by making a selection from the menu!")
print("You can order 1 of 6 types of steak and at the following doneness levels below.")

while True:
    print("\nWhat doneness level would you like your steak to be cooked?")
    print("1) Rare")
    print("2) Medium Rare")
    print("3) Medium")
    print("4) Medium Well")
    print("5) Well Done")
    print("6) Exit")

    done_choice = int(input("\nEnter your choice (1-6): "))

    done = ['Rare', 'Medium Rare', 'Medium', 'Medium Well', 'Well Done']
    if 1 <= done_choice <= 5:
        doneness = done[done_choice - 1]
        print(f"You have chosen {doneness}.")
    elif done_choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    print("\n1) New York\n2) Rib Eye\n3) Flat Iron\n4) Porterhouse\n5) Filet Mignon\n6) Top Sirloin")
    steak_choice = int(input("\nChoose the type of steak that you want? (1-6): "))

    steaks = ['New York', 'Rib Eye', 'Flat Iron', 'Porterhouse', 'Filet Mignon', 'Top Sirloin']
    if 1 <= steak_choice <= 6:
        steak = steaks[steak_choice - 1]
        print(f"You chose {steak} steak. Thanks for ordering! Enjoy your meal! Come again!")
        append_to_csv(steak, doneness)    
        break
  
    else:
        print("Invalid choice. Please try again.")
        continue

print("\nFinally, you have the option to see 2 bar graphs with the frequency of steaks or doneness.")
print("\nThe graphs take in information from previous customers and their preferred choices.")
print("1. Press 1 for frequency of steaks")
print("2. Press 2 for frequency of doneness")

graph_choice = int(input("\nChoose (1/2): "))

if graph_choice == 1:
    steak_frequencies = get_frequencies(0)
    print('frequency of steak types', steak_frequencies)
    plot_frequency(steak_frequencies, "Frequency of Steak Types", "Steak Type")

elif graph_choice == 2:
    done_frequencies = get_frequencies(1)
    print('frequency of steak doneness', done_frequencies)
    plot_frequency(done_frequencies, "Frequency of Steak Doneness", "Doneness")
else:
    print("Invalid choice. Exiting.")
    exit()
  
print("\nThank you for using the Steak Cooker. Come again soon!")
plt.close()
exit()
# end of main code