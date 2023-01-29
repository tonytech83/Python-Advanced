def add_songs(*args):
    song_creator = {}
    for song, strings_line in args:
        if song not in song_creator:
            song_creator[song] = []
        for line in strings_line:
            song_creator[song].append(line)

    result = []

    for song, lyrics in song_creator.items():
        result.append(f'- {song}')
        for lyric in lyrics:
            result.append(lyric)

    return '\n'.join(result)


# Test code 1
print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))

# Test code 2
print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))

# Test code 3
print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
