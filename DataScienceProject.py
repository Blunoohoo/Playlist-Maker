import random

# array that holds all songs inputted by user
songs = []

# function that prints songs array
def printSongs():
    index = 0
    for i in range(len(songs)):
        print(songs[index])
        index = index + 1
# function that prints invalid response
def invalidResponse():
    print("")
    print("Invalid Response, but I'll print your playlist anyways...")
    print("")
    printSongs()

# user input that gets song then is added to the songs playlist
songInput = input("Input a song for your playlist: ")
songs.append(songInput)

# makes an infinite loop
while (1 == 1):
    # asks user if they want to input another song
    # if answer is YES, the program loops
    # if answer is NO, you are prompted to name the playlist
    addSongInput = input("Do you want to input another song: YES or NO: ")
    if addSongInput == "YES":
        songInput = input("Input a song for your playlist: ")
        songs.append(songInput)
    elif addSongInput == "NO":
        # asks user if they would like to name their playlist
        # if answer is YES, the songs array is printed with
        # the users name on top of it
        # if answer is NO, songs array is printed
        # if response is invalid, songs array is printed
        print("")
        namePlaylistInput = input("Do you want to name your playlist?: YES or NO: ")
        if namePlaylistInput == "YES":
            namePlaylistInput = input("Enter the name for your playlist: ")
            print("")
            print(str(namePlaylistInput) + ":")
            printSongs()
            break
        elif namePlaylistInput == "NO":
            print("")
            print("This is your new playlist!:")
            printSongs()
            break
        else:
            invalidResponse()
            break
    else:
        invalidResponse()
        break

# if the songs array has more than one song, the user will be
# asked to listen to a random song using the random function
# from the math library
if (len(songs)) > 1:
    print("")
    randomSongInput = input("Would you like to listen to a random song on your playlist?: YES or NO: ")
    if randomSongInput == "YES":
        randomSongInteger = random.randint(0, len(songs))
        print("Now listening to... " + str(songs[randomSongInteger]))
    elif randomSongInput == "NO":
        print("Goodbye!")
    else:
        randomSongInteger = random.randint(0, len(songs))
        print("Invalid Response, but I'll give you a random song anyways...")
        print("Now listening to... " + str(songs[randomSongInteger]))