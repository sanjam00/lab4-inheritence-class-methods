class Song():
	# Class attributes
	count = 0
	genres = []
	artists = []
	genre_count = {}
	artists_count = {}

	def __init__(self, name, artist, genre):
		self.name = name
		self.artist = artist
		self.genre = genre
		Song.count += 1 # increment when a song is added

	# @classmethod
	# def add_song_to_count(cls):
	# 	cls.count += 1

	@classmethod
	def add_to_genres(cls, genre):
		pass

	@classmethod
	def add_to_artists(cls):
		pass

	@classmethod
	def add_to_genre_count(cls):
		pass

	@classmethod
	def add_to_artists_count(cls):
		pass

song1 = Song("A Long Walk", "Jill Scott", "R&B")
print(Song.count)