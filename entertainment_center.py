# Attaching the other python files
import fresh_tomatoes
import media

# Iron Man (2008)
iron_man = media.Movie("Iron Man",
											 "Tony Stark builds armored suit to fight crime.",
											 "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
											 "https://www.youtube.com/watch?v=8hYlB38asDY")
# The Incredible Hulk (2008)
hulk = media.Movie("The Incredible Hulk", 
									 "The Hulk seeks a cure, but soon comes face-to-face with the Abomination.",								 
									 "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",
									 "https://www.youtube.com/watch?v=xbqNb2PFKKA")
# Iron Man 2 (2010)
iron_man_2 = media.Movie("Iron Man 2",
												 "Iron Man must now face his new enemy, the Whiplash.", 
												 "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
												 "https://www.youtube.com/watch?v=oOzuBOefL8I")
# Thor (2011)
thor = media.Movie("Thor",
									 "Thor banished to Earth, must fight to get back to Asgard, while facing Loki.",
									 "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
									 "https://www.youtube.com/watch?v=JOddp-nlNvQ")
# Captain America: The First Avengers (2011)
captain = media.Movie("Captain America: The First Avenger",
											"Captain America must fight the Nazi-back HYDRA organization.",										
											"https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
											"https://www.youtube.com/watch?v=JerVrbLldXw")
# The Avengers (2012)
avengers = media.Movie("The Avengers",
 											 "Iron man, Thor, Captain America, etc must fight Loki and his team of evil aliens.",
											 "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
											 "https://www.youtube.com/watch?v=eOrNdBpGMv8")
# Iron Man 3 (2013)
iron_man_3 = media.Movie("Iron Man 3",
												 "Iron Man faced with PTSD must face the Mandarin.",
												 "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
												 "https://www.youtube.com/watch?v=2CzoSeClcw0")
# Thor: The Dark World (2013)
thor_2 = media.Movie("Thor: The Dark World",
										 "Thor must fight the Dark Elf Malekith.",
										 "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",
										 "https://www.youtube.com/watch?v=npvJ9FTgZbM")
# Captain America: The Winter Soldier (2014)
captain_2 = media.Movie("Captain America: The Winter Soldier",
												"Captain America struggles with conspiracy and faces the Winter Solider.",
									   		"https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",
												"https://www.youtube.com/watch?v=7SlILk2WMTI")
# Guardians of the Galaxy (2014)
guardians = media.Movie("Guardians of the Galaxy",
												"The Gaurdians form their team and must face the Evil Ronan.",
												"https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
												"https://www.youtube.com/watch?v=d96cjJhvlMA")
# Avengers: Age of Ultron (2015)
avengers_2 = media.Movie("Avengers: Age of Ultron",
												 "The Avengers must fight the evil Ultron.",
												 "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
												 "https://www.youtube.com/watch?v=JAUoeqvedMo")
# Ant-Man (2015)
antman = media.Movie("Ant-Man",
										 "Ant-Man must face the Yellowjacket.",
										 "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
										 "https://www.youtube.com/watch?v=pWdKf3MneyI")
# Captain America: Civil War (2016)
captain_3 = media.Movie("Captain America: Civil War",
												"Captain America and Iron Man form a team to have an all-out feud against each other.",
												"https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
												"https://www.youtube.com/watch?v=dKrVegVI0Us")
# Doctor Strange (2016)
strange = media.Movie("Doctor Strange",
											"Dr. Strange becomes a sorcerer and must face unseen dark forces.", 
											"https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
										 	"https://www.youtube.com/watch?v=HSzx-zryEgM")
# Guardians of the Galaxy Vol. 2 (2017)
guardians_2 = media.Movie("Guardians of the Galaxy Vol. 2",
													"The Gaurdians being attacked from the Sovereign, escape and discover Peter's parentage.",
													"https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
													"https://www.youtube.com/watch?v=dW1BIid8Osg")
# Spider-Man: Homecoming (2017)
spiderman	= media.Movie("Spider-Man: Homecoming",
												"Spider-Man must face the evil Vulture.",
												"https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
												"https://www.youtube.com/watch?v=U0D3AOldjMU")
# Thor: Ragnarok (2017)
thor_3 = media.Movie("Thor Ragnarok",
										 "Thor must form a small team to face the evil Hela.",
										 "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
										 "https://www.youtube.com/watch?v=ue80QwXMRHg")
# Black Panther (2018)
panther = media.Movie("Black Panther",
											"Panther must protect his kingdom from Killmonger and foreign invaders.",
											"https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
											"https://www.youtube.com/watch?v=dxWvtMOGAhw")

# Array of movie titles
movies = [iron_man, hulk, iron_man_2, thor, captain, avengers, iron_man_3, thor_2, captain_2, guardians, avengers_2, antman, captain_3, strange, guardians_2, spiderman, thor_3, panther]

# Runs the code to create the website
fresh_tomatoes.open_movies_page(movies)