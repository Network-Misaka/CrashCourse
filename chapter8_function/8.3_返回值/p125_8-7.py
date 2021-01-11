def make_album(singer_name, album_name, song_count=''):
    album_info = {'singer': singer_name, 'album': album_name}
    if song_count:
        album_info['count'] = song_count
    return album_info


print(make_album('Jay', 'fantasy'))
print(make_album('Lee zongsheng', 'For me'))
print(make_album('Jhon', 'Western','15'))

