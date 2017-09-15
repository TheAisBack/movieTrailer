import webbrowser

"""Creating a movie class to store the title, storyline, poster and url link"""
class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	"""Opening the youtube trailer once clicked"""
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
	"""Opening the poster image for the movie"""
	def show_poster(self):
		webbrowser.open(self.poster_image_url)