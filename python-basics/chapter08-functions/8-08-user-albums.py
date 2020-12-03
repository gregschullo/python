def make_album(artist_name, album_title, num_songs=None):
    """function will take input and create an album dictionary"""
    album = {'artist': artist_name, 'title': album_title}
    if num_songs:
        album['tracks'] = num_songs
    return album

while True:
    print("\nPlease enter information about your favorite album? ")
    print("(enter 'q' at any time to quit)")
    
    artist = input("Artist: ")
    if artist == 'q':
        break
    
    album = input("Album: ")
    if album == 'q':
        break

    tracks = input("Tracks: ")
    if tracks == 'q':
        break

    record = make_album(artist, album, tracks)
    print(record)
