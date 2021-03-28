

music_genres = []

#print('')

#print(len(music_genres))

#print('')

#Visiting every item in a list 

#for i in range(len(music_genres)):
    #print(music_genres[i])
    #print('')


#for genre in music_genres: 
    #print(genre)
    #print('')


#Adding values to a list 

#print('')
#music_genres.append('progressive')
#print(music_genres)

def print_items(itms): 
    for i in range(len(itms)):
        print(itms[i])
        print('')






go_again = 0




while go_again != 1:

    new_genre = input('What genre do you want to add to the list?')
    print('')
    music_genres.append(new_genre)
    print('')
    #print(music_genres)
    print("1: I'm finished")
    print('')
    try:
        go_again = int(input('Type "1" if finished and a different integer if not: '))
    except:
        print('')
        print('Input is invalid - try again')
    print('')
    

print_items(music_genres)

    
