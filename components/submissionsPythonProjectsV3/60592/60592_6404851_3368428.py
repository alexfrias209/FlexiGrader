#Barrios_Dani_Final Project
import networkx as nx
import matplotlib.pyplot as plt
#nx and plt are common alias so I dont need to write the whole actual name
#used pip by downloading pip, using file locations to add to my path in enviromental virables and using the command prompt 
# to pip intall ''
G = nx.Graph()
# undirected graph so paths between the nodes can go either way without me needed to write i.e (merced-> modesto) and (modesto->merced)

print()
print('Hello.')
user_name = input('What is your name? \n')
#basic intro and input 
    
print(f'Nice to meet you {user_name}! \n')

print('Traveling Salesman Problem Solver: Write a program to solve the Traveling Salesman Problem using heuristic methods like the nearest neighbor algorithm. You could explore improvements or alternative algorithms. Outputs would include the shortest path and distance\n')
while True:
    #starting my while loop here so it doesnt repeat unnessecary stuff
    print('The city starting points avaliable for this code is:\n Merced\n Fresno\n San Jose\n Stockton\n Modesto\nPlease be mindful of spelling.\n')
    
    G.add_edge('Merced', 'Fresno', weight=56.2)
    G.add_edge('Merced', 'San Jose', weight=115)
    G.add_edge('Merced', 'Stockton', weight=70.2)
    G.add_edge('Merced', 'Modesto', weight=39.7)
    G.add_edge('Fresno', 'San Jose', weight=150)
    G.add_edge('Stockton', 'Fresno', weight=126)
    G.add_edge('Modesto', 'Fresno', weight=95)
    G.add_edge('Stockton', 'San Jose', weight=79.9)
    G.add_edge('Modesto', 'San Jose', weight=86.1)
    G.add_edge('Stockton', 'Modesto', weight=31.5)
    #my G edge list makes the nodes, weight means distance in this case

    G.add_node('Merced',pos=(10,10))
    G.add_node('Fresno',pos=(12,8))
    G.add_node('Modesto',pos=(8,11))
    G.add_node('Stockton',pos=(6,13))
    G.add_node('San Jose',pos=(5,10))
    #with my previously made nodes I am giving them cordinates in a pos function to group it and I made to resemble 
    # the city locations to google maps
    
    
    while True: 
        starting_city = input('Enter the starting city: ').strip().title()
        if starting_city in G.nodes:            
            break
        else:
            print('Invalid city. Please choose from available cities.')

    print()

    while True:
        end_city = input('Enter the end city: ').strip().title()
        if end_city in G.nodes:
            break
        else:
            print('Invalid city. Please choose from available cities.')
    #I made another while loop so users can ONLY input correct cities not mattering spaces or capitilization, if they make a spelling
    #error or input a not avaliable city it sends the user back to the input line so they can put in a correct city

    path = nx.shortest_path(G,source = starting_city, target = end_city, weight = 'weight')
    length = nx.shortest_path_length(G, source = starting_city, target = end_city, weight = 'weight')
    #the nx.shortest path is from the networkx import where I specify that within the G graph the source is the starting_city and the 
    #target is the end_city and weight is taken from the 'weight'= from above
    print()
    print('Shortest path:','->'.join(path))
    #takes the iterable from the path (starting_city and end_city)and joins them into a single string
    print()
    print('Shorthest path length:',length,'miles') 
    #this takes the lenth variable previously made and places it here
    print() 

    #creating the visuals: 
    user_path = [(path[i],path[1+i]) for i in range(len(path)-1)]
    #path[i],path[1+i] = is two elements where it takes position i from the path list (staring_city)
    #and i+1 from the second element which is end_city


    pos=nx.get_node_attributes(G,'pos')
    #this just gets the nodes from G and pos function and labels it as pos so I can put it
    #into the nx.draw
    nx.draw(G,pos,with_labels=True)
    #draws my graph with the edges, node location, and labels the nodes as the city names
    nx.draw_networkx_edges(G, pos, edgelist=user_path, edge_color = 'red')
    #draws the line between edges specified from user_path
    plt.show()
    #shows the graph


    repeat_code = input('Do you want to check another route? yes/no: ')  
    if repeat_code.lower() != 'yes':
        print(f'Have a great day, {user_name}.')
        break
