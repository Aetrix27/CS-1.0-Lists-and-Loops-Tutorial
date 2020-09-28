songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0])
print(songs[2])
print(songs[1:2])

# update the first element
songs[2] = "Party Rock Anthem"
# print the list
print(songs)

songs.extend(["Sicko Mode", "24K Magic", "Keanu Reeves"])
print(songs)

del songs[2]
print(songs)