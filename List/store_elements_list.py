# Write a program to ask the user to enter names of their 3 favorite movies and store them in a list.

# Initialize an empty list to store the movie names
movie = []

# Ask the user to enter their first favorite movie
movie_1 = input("Enter your first element: ")

# Ask the user to enter their second favorite movie
movie_2 = input("Enter your second element: ")

# Ask the user to enter their third favorite movie
movie_3 = input("Enter your third element: ")

# Add the first movie to the list
movie.append(movie_1)

# Add the second movie to the list
movie.append(movie_2)

# Add the third movie to the list
movie.append(movie_3)

# Print the list of movies
print("List of movies is: ", movie)