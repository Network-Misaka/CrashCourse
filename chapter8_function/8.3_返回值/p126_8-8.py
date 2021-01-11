def make_album(singer_name, album_name, song_count=''):
    album_info = {'singer': singer_name, 'album': album_name}
    if song_count:
        album_info['count'] = song_count
    return album_info


while True:
    singerName = input('tell me the singer name \n')
    albumName = input('tell me yhe album name \n')
    print(make_album(singer_name=singerName, album_name=albumName))
