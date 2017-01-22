import webbrowser

class Video():
    def __init__(self, video_title):
        self.title = video_title

class Movie(Video):
    """ This class provides a way to store movie related information """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, video_title, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, video_title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
