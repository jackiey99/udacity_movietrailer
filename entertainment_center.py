from media import movie
from fresh_tomatoes import open_movies_page

# initialize the list movies as an empty list
movies = []

# append the first movie to the movies list
movies.append(movie('Zootopia', 'http://cdn.collider.com/wp-content/uploads/2015/12/zootopia-movie-poster.jpg',  # NOQA
                    'https://www.youtube.com/watch?v=jWM0ct-OLsM', '2016'))

movies.append(movie('Kung Fu Panda 3', 'http://t0.gstatic.com/images?q=tbn:ANd9GcTv8AULgHD6dyYlMkjvC2YITU41wECwkPSGxHUyr9DXvct7vwY2',  # NOQA
                    'https://www.youtube.com/watch?v=10r9ozshGVE', '2016'))

movies.append(movie('Boyhood', 'http://t0.gstatic.com/images?q=tbn:ANd9GcTj0AWSMjSJ2T7vk2yQTjOIaU6XOnzXis9egJzJh6YBWrT0A5td',  # NOQA
                    'https://www.youtube.com/watch?v=Ys-mbHXyWX4', '2014'))

movies.append(movie('Deadpool', 'http://t1.gstatic.com/images?q=tbn:ANd9GcR-fLY3Z9Vn28UB-A3X_w0vjmkHcXG89HWwul5w6-sg3IonPXA_',  # NOQA
                    'https://www.youtube.com/watch?v=frRFOrbPfNc', '2016'))

# call the open_movies_page function from provided fresh_tomatoes.py to
# render the website
open_movies_page(movies)
