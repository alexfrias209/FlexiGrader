import matplotlib.pyplot as plt
from skimage import io
restart = True
score_right = 0
score_wrong = 0
while restart:
    plt.rcParams["figure.figsize"] = [5.50, 4.50]
    plt.rcParams["figure.autolayout"] = True
    link = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlhPqhwmLHwXVPEntKK7MfTV0tE7MIp77gHw&usqp=CAU'
    a = io.imread(link)
    plt.imshow(a)
    plt.axis('off')
    plt.draw()
    plt.pause(1)
    game_1 = input("What is the name of this video game: \n")
    if game_1 == "Super Mario Bros":
        print("Correct!")
        score_right += 1
        link ='https://gamingbolt.com/wp-content/uploads/2022/06/Call-of-Duty-Modern-Warfare-2-5.jpg'
        a = io.imread(link)
        plt.imshow(a)
        plt.axis('off')
        plt.draw()
        plt.pause(1) 
        game_2 = input("What is the name of this video game: \n")
    else:
        print("Incorrect!")
        score_wrong += 1
        continue
    if game_2 == "Call of Duty":
        print("Correct!")
        score_right += 1
        link ='https://techcrunch.com/wp-content/uploads/2011/01/minecraft1.jpg'
        a = io.imread(link)
        plt.imshow(a)
        plt.axis('off')
        plt.draw()
        plt.pause(1) 
        game_3 = input("What is the name of this video game: \n")
        if game_3 == "Minecraft":
            print("Correct!")
            score_right += 1
            link ='https://www.redsharknews.com/hubfs/zelda%20tears%20of%20the%20kingdom.jpg'
            a = io.imread(link)
            plt.imshow(a)
            plt.axis('off')
            plt.draw()
            plt.pause(1) 
            game_4 = input("What is the name of this video game: \n")
            if game_4 == "The Legend of Zelda":
                print("Correct!")
                score_right += 1
                link ='https://media.wired.com/photos/5f74d2f4df8a35780989d792/master/w_2240,c_limit/Genshin%20Impact%20_Keyart.png'
                a = io.imread(link)
                plt.imshow(a)
                plt.axis('off')
                plt.draw()
                plt.pause(1) 
                game_5 = input("What is the name of this video game: \n")
                if game_5 == "Genshin Impact":
                    print("Correct!!")
                    score_right += 1
                    link ='https://staticg.sportskeeda.com/editor/2022/07/5f40f-16576134608517-1920.jpg'
                    a = io.imread(link)
                    plt.imshow(a)
                    plt.axis('off')
                    plt.draw()
                    plt.pause(1) 
                    game_6 = input("What is the name of this video game: \n")
                    if game_6 == "Clash of Clans":
                        print("Correct!!")
                        score_right += 1
                        link ='https://assetsio.reedpopcdn.com/roblox_poGuVlz.jpg?width=1920&height=1920&fit=bounds&quality=80&format=jpg&auto=webp'
                        a = io.imread(link)
                        plt.imshow(a)
                        plt.axis('off')
                        plt.draw()
                        plt.pause(1)
                        game_7 = input("What is the name of this video game: \n")
                        if game_7 == "Roblox":
                          print("Correct!!")
                          score_right += 1
                          link ='https://lh3.googleusercontent.com/Zxt9D9UiWW7jBCw_fFvWMCtRAuCx8xeRE63d42eArtBPXXXEfV2a5lIUW4ksTqkagV79zekmVKa4jj1RJlbo-Ivt=w640-h400-e365-rj-sc0x00ffffff'
                          a = io.imread(link)
                          plt.imshow(a)
                          plt.axis('off')
                          plt.draw()
                          plt.pause(1)
                          game_8 = input("What is the name of this video game: \n")
                          if game_8 == "Subway Surfers":
                            print("Correct!!")
                            score_right += 1
                            link ='https://cdn.mos.cms.futurecdn.net/csQgknvLgV4P4ABbFSZdrE-1200-80.jpg.webp'           
                            a= io.imread(link)
                            plt.imshow(a)
                            plt.axis('off')
                            plt.draw()
                            plt.pause(1)
                            game_9 = input("What is the name of this video game: \n")
                            if game_9 == "Fortnite":
                              print("Correct!!")
                              score_right += 1
                              link ='https://s3.amazonaws.com/prod-media.gameinformer.com/styles/body_default/s3/legacy-images/imagefeed/Game%20Freak%20Revitalizes%20A%20Beloved%20Franchise/pokemonwhite610.jpg'
                              a = io.imread(link)
                              plt.imshow(a)
                              plt.axis('off')
                              plt.draw()
                              plt.pause(1)
                              game_10 = input("What is the name of this video game: \n")
                              if game_10 == "Pokemon":
                                print("Correct!!")
                                score_right += 1
                      
    print("Score - Right:", score_right, ", Wrong:", score_wrong)
    restart_input = input("Do you want to restart the program? [yes/no]: ")
    restart = True if restart_input.lower() == "yes" else False
    score_right = 0
    score_wrong = 0