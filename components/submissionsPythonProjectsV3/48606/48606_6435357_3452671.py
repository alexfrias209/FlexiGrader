# The following is the python midterm project

# Project idea: A book recommendation app: The program will ask what
# kind of genre of books the user likes to read. Then it will provide
# popular authors of that genre, when the user types in the author’s
# name, the top 3 sold books of that author will show.

Question_1=input('What is your goal for the ME021 project?   \n')
Question_2=input('What are the inputs and outputs of the project?   \n')
Question_3=input('What will your project take as inputs?   \n')
Question4=input('Did you meet with Alex to discuss your project? Yes or No.   \n')
if Question4=='Yes':
        print('Project work')
if Question4=='No':
        print('Your proposal did not answer all questions')


Print('Hi, this is the presentation of the ME_021 python project.')
Print('In this project, we will help you select a book that you want to read based on your give data.')
# Data: 
Books={'Fiction': {'J.K. Rowling':{ {'book':'Harry Potter and the Sorcerer’s Stone','book page':223},
                                    {'book':'Harry Potter and the Goblet of Fire', 'book page':636},
                                    {'book':'Harry Potter and the Order of the Phoenix', 'book page':766},},
                  'F. Scott Fitzgerald':{ {'book':'The Great Gatsby','book page':208},
                                          {'book':'This side of paradise','book page':320},
                                          {'book':'Tender is the night','book page':320},},
       },
      'Horror': {'Stephen King':{ {'book':'The Shining','book page':505},
                                   {'book':'Pet Semetary','book page':416},
                                   {'book':'It','book page':1168},},

                 'Jack Ketchum':{ {'book':'The girl next door','book page':320},
                                  {'book':'Off season','book page':324},
                                  {'book':'Red','book page':270},},
      }
      }
#      Fiction:{'J.K. Rowling': {'Harry Potter and the Sorcerer’s Stone':'223','Harry Potter and the Goblet of Fire':'636','Harry Potter and the Order of the Phoenix':'766'}},
#              J.K._Rowling: {'Harry Potter and the Sorcerer’s Stone':'223','Harry Potter and the Goblet of Fire':'636','Harry Potter and the Order of the Phoenix':'766'}},
#              {'F. Scott Fitzgerald': {'The Great Gatsby':'208','This side of paradise':'320','Tender is the night':'320'}}
#              
#       Horror:{'Stephen King': {'The Shining':'505','Pet Semetary':'416','It':'1168'}}
#              {'Jack Ketchum': {'The girl next door':'320','Off season':'324','Red':'270'}}
#        book_page = input('Do you want to read books with more than 500 pages? Please answer yes or no.')
#        if 
        
def genre_searched():
        genre=input('What genre of books do you like to read? ')
        if genre in Books:
            return genre
        else:
            print('The genre you input is not in the data, please choose from given genres.')
def author_searched(genre):
        author = input('Choose an author given in the genre youve selected: ')
        if author in Books(genre):
            return author
        else:
            print('The author you input is not in the data. please choose from given authors corresponding to its genre.')
def book_page_wanted():
        book_page = input('Do you want to read books with more than 500 pages? Please answer yes or no.')
        if book_page=='Yes':
                book_page>500
                print('The book recommended for you is 'Books)
        if book_page=='No':
                book_page<500
                print('The book recommended for you is 'Books)
def 


