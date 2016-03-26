class movie(object):
    """ This defines the movie class.

    Args:
        title (str): the title of the movie
        poster_image_url (str): the url of the movie poster image
        trailer_youtube_url (str): the Youtube url of the movie
        movie_year (str): year of the movie

    """

    def __init__(
            self,
            title,
            poster_image_url,
            trailer_youtube_url,
            movie_year):
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url
        self.movie_year = movie_year
