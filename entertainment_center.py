# coding=utf-8
import media
import fresh_tomatoes

movieList = []
movie = media.Movie("Spider-Man: Homecoming",
                    "https://i.ytimg.com/vi_webp/vaYRC8mIusY/movieposter.webp",
                    "https://www.youtube.com/watch?v=vaYRC8mIusY&amp;list=PLHPTxTxtC0iawUW7gxiulmZRsd_uRvZ3T")
movieList.append(movie)
movie = media.Movie("Doctor Strange (2016)",
                    "https://i.ytimg.com/vi_webp/SPD0fSV4qJ8/movieposter.webp",
                    "https://www.youtube.com/watch?v=SPD0fSV4qJ8&amp;list=PLHPTxTxtC0iawUW7gxiulmZRsd_uRvZ3T")
movieList.append(movie)
movie = media.Movie("Cars 3",
                    "https://i.ytimg.com/vi_webp/yWcTbaCN3zA/movieposter.webp",
                    "https://www.youtube.com/watch?v=yWcTbaCN3zA&amp;list=PLwY4hq6U-Yslno-4XSEfQZ3QmWqXQOe_O")
movieList.append(movie)
movie = media.Movie("Kingsman: The Secret Service",
                    "https://i.ytimg.com/vi_webp/ncNLOZHrzpM/movieposter.webp",
                    "https://www.youtube.com/watch?v=ncNLOZHrzpM&amp;list=PLImMP769j55JiOrKm7lO1GiSWWO0TXnI3")
movieList.append(movie)
movie = media.Movie("Wonder Woman (2017)",
                    "https://i.ytimg.com/vi_webp/l0Mfv-8yMGo/movieposter.webp",
                    "https://www.youtube.com/watch?v=l0Mfv-8yMGo&amp;list=PLImMP769j55JiOrKm7lO1GiSWWO0TXnI3")
movieList.append(movie)
movie = media.Movie("The Red Turtle",
                    "https://i.ytimg.com/vi_webp/TMu3wRKJEQg/movieposter.webp",
                    "https://www.youtube.com/watch?v=TMu3wRKJEQg&amp;list=PLwY4hq6U-Yslno-4XSEfQZ3QmWqXQOe_O")
movieList.append(movie)

media.Movie()
print movieList
fresh_tomatoes.open_movies_page(movieList)

