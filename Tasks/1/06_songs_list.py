violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

newSongs = violator_songs_list[3][0] + ', ' + violator_songs_list[5][0] + ', ' + violator_songs_list[8][0]
theTime = violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1]
theTime = round(theTime, 2)
print(f"{newSongs} sound {theTime} minutes")

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

key_list = list(violator_songs_dict.keys())
values_list = list(violator_songs_dict.values())
newSongsDict = key_list[values_list.index(4.43)] + ", " \
               + key_list[values_list.index(4.88)] + ", " + key_list[values_list.index(4.18)]
theTimeDict = violator_songs_dict['Sweetest Perfection'] \
              + violator_songs_dict['Policy of Truth'] + violator_songs_dict['Clean']
theTimeDict = round(theTimeDict, 2)
print(f"{newSongsDict} sound {theTimeDict} minutes")