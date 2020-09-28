#Accesses and updates the song list
songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0])
print(songs[2])
print(songs[1:3])
songs[2] = "Party Rock Anthem"
print(songs)

#Adds three new songs to the list
songs.append("Sicko Mode")
songs.extend(["24K Magic", "Keanu Reeves"])
print("Three New songs have been added!")
print(songs)

#Deletes song 3
print(f"{songs[2]} has been deleted!")
del songs[2]
print(songs)

#Edits animal list
animals = ["Hamster", "Ferret", "Chinchilla"]
animals.append("Kangaroo")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)