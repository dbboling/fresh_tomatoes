import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

inception = media.Movie("Inception",
                        "A theif steals secrets by entering dreams",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Inception_%282010%29_theatrical_poster.jpg/220px-Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

bugs_life = media.Movie("A Bug's Life",
                        "A lonely, ambitious ant gets kicked out of the anthill",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/A_Bug%27s_Life.jpg/220px-A_Bug%27s_Life.jpg",
                        "https://www.youtube.com/watch?v=cgcQJxrpIgs")

rogue_one = media.Movie("Rogue One: A Star Wars Story",
                        "A young orphan girl is abducted by rebels",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png/220px-Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

lotr_fellowship = media.Movie("Lord of the Rings: The Fellowship of the Ring",
                              "A hobit inherits the world's worst piece of jewelry",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg/220px-The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                              "https://www.youtube.com/watch?v=V75dMMIW2B4")

movies = [toy_story, avatar, inception, bugs_life, rogue_one, lotr_fellowship]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
