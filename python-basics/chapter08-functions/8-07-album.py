def make_album(artist_name, album_title, num_songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_songs:
        album['tracks'] = num_songs
    return album

record = make_album('Lorde', 'Melodrama', 12)
print(record)

record = make_album('Green Day', 'Dookie')
print(record)

record = make_album('Megan Thee Stallion', 'Good News')
print(record)
