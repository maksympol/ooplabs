"""Визначити ієрархію музичних композицій. Записати на диск альбом. Порахувати тривалість альбому.
   Провести перестановку композицій диска на основі приналежності до стилю.
   Знайти композицію, що відповідає заданому діапазону довжини треків."""


class Main:
    def __init__(self, songs):
        self.songs = songs

    def sort_songs(self):
        for _ in self.songs:
            self.songs = sorted(all_songs, key=lambda i: i.genre)

        print("List of all songs:")
        c = 1
        for j in self.songs:
            print(c, ")", j.name, sep="")
            c += 1

        print("Sorting a songs by genre: ")
        for k in self.songs:
            print(k.name, k.genre, end=", ")


class Forester:
    def __init__(self, name, genre, musical_group, length):
        self.name = name
        self.genre = genre
        self.musical_group = musical_group
        self.length = length


class Holiday(Forester):
    pass


class BloodType(Forester):
    pass


class Believer(Forester):
    pass


forester = Forester("Forester", "punk rock", "KAC", 6)

holiday = Holiday("Holiday", "punk rock", "Green Day", 5)

blood_type = BloodType("BloodType", "punk rock", "Cinema", 4)

believer = Believer("Believer", "pop rock", "Imagine Dragons", 3)

all_songs = [forester, holiday, blood_type, believer]

songs_all = Main(all_songs)
print(songs_all.sort_songs())

start_length = int(input("Enter the initial song length: "))
finish_length = int(input("Enter the final length of the song: "))
user_length = range(start_length, finish_length + 1)

for song in all_songs:
    if song.length in user_length:
        print("{} - ideal song for you!".format(song.name))
