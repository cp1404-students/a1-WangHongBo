"""
Name:Wang Hongbo
Date started: 21/12/2023
GitHub URL:https://github.com/cp1404-students/a1-WangHongBo
"""

LEARNED_STATUS = 'l'
UNLEARNED_STATUS = 'u'
CSV_FILE_PATH = 'songs.csv'


def main():
    print("Song List 1.0 - by Lindsay Ward")

    songs = read_songs(CSV_FILE_PATH)
    print(f"{len(songs)} songs loaded.")

    choice = ''
    while choice != 'q':
        print("\nMenu:\nD - Display songs\nA - Add new song\nC - Complete a song\nQ - Quit")
        choice = input(">>> ").lower()

        if choice == 'd':
            display_songs(songs)
        elif choice == 'a':
            print("Enter details for a new song.")
            add_song(songs)
        elif choice == 'c':
            mark_song_as_learned(songs)
        elif choice == 'q':
            write_songs(CSV_FILE_PATH, songs)
            print(f"{len(songs)} songs saved to {CSV_FILE_PATH}\nMake some music!")
        else:
            print("Invalid menu choice")


def read_songs(file_path):
    songs = []
    try:
        file = open(file_path, 'r')
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                songs.append([parts[0], parts[1], int(parts[2]), parts[3].strip().lower()])
        file.close()
    except FileNotFoundError:
        print(f"No existing file found at {file_path}. Starting with an empty list.")
    return songs


def write_songs(file_path, songs):
    in_file = open(file_path, 'w')
    for song in songs:
        line = f"{song[0]},{song[1]},{song[2]},{song[3]}\n"
        in_file.write(line)
    in_file.close()


def display_songs(songs):
    learned_count = sum(1 for song in songs if song[3] == LEARNED_STATUS)
    unlearned_count = sum(1 for song in songs if song[3] == UNLEARNED_STATUS)

    max_title_length = max(len(song[0]) for song in songs)
    max_artist_length = max(len(song[1]) for song in songs)
    max_year_length = max(len(str(song[2])) for song in songs)

    for i, song in enumerate(songs, 1):
        status = '*' if song[3] == UNLEARNED_STATUS else ''
        title = song[0].ljust(max_title_length)
        artist = song[1].ljust(max_artist_length)
        year = str(song[2]).rjust(max_year_length)
        print(f"{i}. {status:>1}{title} - {artist} ({year})")

    print(f"{learned_count} songs learned, {unlearned_count} songs still to learn.")


def get_valid_input(prompt, error_message):
    user_input = input(prompt)
    while user_input.strip() == "":
        print(error_message)
        user_input = input(prompt)
    return user_input


def get_valid_year(prompt, error_message):
    year_input = input(prompt)
    while not (year_input.isdigit() and int(year_input) > 0):
        print(error_message)
        year_input = input(prompt)
    return int(year_input)


def add_song(songs):
    title = get_valid_input("Title: ", "Input cannot be blank.")
    artist = get_valid_input("Artist: ", "Input cannot be blank.")
    year = get_valid_year("Year: ", "Invalid input; enter a valid number.")

    songs.append([title, artist, year, UNLEARNED_STATUS])
    print(f"{title} by {artist} ({year}) added to song list.")


def mark_song_as_learned(songs):
    unlearned_songs = [song for song in songs if song[3] == UNLEARNED_STATUS]
    if not unlearned_songs:
        print("No more songs to learn!")
        return

    for i, song in enumerate(unlearned_songs, 1):
        print(f"{i}. {song[0]} - {song[1]} ({song[2]})")

    valid_choice = False
    while not valid_choice:
        choice = input("Enter the number of a song to mark as learned.\n>>> ")
        if not choice.isdigit():
            print("Invalid input; please enter a valid number.")
        else:
            choice_number = int(choice)
            if choice_number <= 0:
                print("Number must be > 0.")
            elif choice_number > len(unlearned_songs):
                print("Invalid song number")
            else:
                valid_choice = True
                chosen_song = unlearned_songs[choice_number - 1]
                if chosen_song[3] == LEARNED_STATUS:
                    print(f"You have already learned {chosen_song[0]}")
                else:
                    chosen_song[3] = LEARNED_STATUS
                    print(f"{chosen_song[0]} by {chosen_song[1]} learned")


if __name__ == '__main__':
    main()
