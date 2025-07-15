########
######## FUNCTIONS RELATED TO SECOND USER PROMPT (Learn about stars) ########
########

#open and read the aspect.txt file
def readAspect(aspectFile):
    with open(aspectFile, "r") as aspect:
        aspectF = aspect.readlines()
    
    characteristics = [] #create empty list
    aspects = {} #create empty dictionary
    nowAspect = ""
    description = ""
    
    for line in aspectF:
        line = line.strip() #remove whitespace
        if line.startswith("Characteristic:"):
            if nowAspect:
                aspects[nowAspect] = description
            nowAspect = line.split(":")[1].strip()
            characteristics.append(nowAspect)
            description = ""
        elif line.startswith("Description:"):
            description = line.split(":")[1].strip()

    return characteristics, aspects

#provide list of characteristics
def listCharacteristics(characteristics):
    print("List of Characteristics:")
    for characteristic in characteristics:
        print(characteristic) #iterate over the previously empty list

#check to see if the user inputted characteristic actually exists in aspect.txt       
def getAspect(aspectName, aspect_descriptions):
    if aspectName in aspect_descriptions:
        print(aspect_descriptions[aspectName])
    else:
        print("blargh")
        #print(aspect_descriptions) used to check what was going on

def mainSequence():
    import pandas
    import matplotlib.pyplot as plt
    data = pandas.read_csv('stars.csv')
    ankh = data
    StarE = ['Radius', 'Mass', 'Temperature', 'Distance', 'Age', 'Apparent', 'Absolute', 'Luminosity']

    for column in ankh:
        ankh[column] = ankh[column].astype(str).str.replace(',', '') #iterate over every cell and remove commas
    ankh[StarE] = ankh[StarE].apply(pandas.to_numeric) #change all the values back to int and floats
    print() #(staro) is the first that absolutely needs to be optimized
    ankh = ankh.sort_values(by=["Temperature"])
    ankh.to_csv("ankh.csv")

        #used in an HR diagram
    luminosities = ankh['Luminosity']
    temperatures = ankh['Temperature']
    spectral_classes = ankh['Spectral']
    radii = ankh['Radius']

    #assign colors to spectral types
    color_map = {
        'W': '#B4A3F8',
        'L': '#1A8EF4',
        'O': '#543ABC',
        'B': '#3844EE',
        'A': '#FFFFFF',
        'F': '#F2E58A',
        'G': '#FAE12F',
        'K': '#FB9E30',
        'M': '#FE4C1F'
    }

    scaled_radii = radii * .6  #sizes of stars in graph

    fig, ax = plt.subplots(figsize=(12, 8))

    #color-code the data points
    for i in range(len(luminosities)):
        spectral_class = spectral_classes[i][0]  #get the spectral type for each star
        color = color_map.get(spectral_class, 'gray')  # Default to gray if not in the color map
        ax.scatter(temperatures[i], luminosities[i], s=scaled_radii[i], color=color, label=spectral_class, alpha=0.5)
    #plt.scatter(temperatures, luminosities, marker='.')#, #color=color, label=spectral_class)

    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Luminosity (L/Sol)')
    ax.set_yscale('log')  #log scale for y axis
    ax.invert_xaxis()  #invert x axis
    ax.set_facecolor("black")
    ax.set_title('Hertzsprung-Russell Diagram of Super Star Catalog') #title
    plt.show()

