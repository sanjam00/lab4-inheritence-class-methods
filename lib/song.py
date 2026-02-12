class Song():
	# Class attributes
	count = 0
	genres = []
	artists = []
	genre_count = {}
	artist_count = {}

	def __init__(self, name, artist, genre):
		self.name = name
		self.artist = artist
		self.genre = genre
		Song.count += 1 # increment when a song is added
		Song.artists.append(artist)
		Song.genres.append(genre)
		Song.add_to_genre_count(genre)
		Song.add_to_artists_count(artist)

	# @classmethod
	# def add_song_to_count(cls):
	# 	cls.count += 1

	# @classmethod
	# def add_to_genres(cls):
	# 	pass

	# @classmethod
	# def add_to_artists(cls):
	# 	pass

	@classmethod
	def add_to_genre_count(cls, genre):
		if genre in cls.genre_count:
			cls.genre_count[genre] += 1
		else:
			cls.genre_count.update( {genre: 1} )

	@classmethod
	def add_to_artists_count(cls, artist):
		if artist in cls.artist_count:
			cls.artist_count[artist] += 1
		else:
			cls.artist_count.update( {artist: 1} )

song1 = Song("A Long Walk", "Jill Scott", "R&B")
song2 = Song("The Truth", "India Arie", "Soul")
song3 = Song("Untitled", "D'Angelo", "R&B")
song4 = Song("Voodoo", "D'Angelo", "R&B")

print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.genre_count)
print(Song.artist_count)
