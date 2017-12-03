# coding=utf-8

class Movie():

    def __init__(self,title,poster_image_url,trailer_youtube_url):
        '''
        new empty Movie
        :param title: movie title
        :param poster_image_url: movie poster
        :param trailer_youtube_url:A movie url in youtube
        '''
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url