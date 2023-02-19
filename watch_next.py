import spacy

# Load the medium English language model
nlp = spacy.load('en_core_web_md')

# Read in the movie descriptions from movies.txt
with open('movies.txt', 'r') as file:
    movie_descriptions = [line.strip() for line in file]


def suggest_movies(description, movie_descriptions):
    """
    We take the description of the movie the user wants to watch, and compare it to the descriptions of all the movies in
    our database. We then return the movie with the highest similarity score

    :param description: The description of the movie you want to watch
    :param movie_descriptions: a list of movie descriptions
    :return: the title and description of the movie that is most similar to the description given.
    """

    similarities = [nlp(description).similarity(nlp(movie)) for movie in movie_descriptions]

    max_index = similarities.index(max(similarities))

    suggestion_title = f"Movie {chr(max_index + ord('A'))}"
    suggestion_description = movie_descriptions[max_index]
    return suggestion_title, suggestion_description


# Define the current watch and its description
current_watch_title = "Planet Hulk"
current_watch_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Suggest movies based on the current watch description
suggestion_title, suggestion_description = suggest_movies(current_watch_description, movie_descriptions)

# Display the current watch and its description
print(f"Current Watch: {current_watch_title}")
print(f"Description: {current_watch_description}\n")

# Display the suggested movie and its description
print(f"Suggested Movie: {suggestion_title}")
print(f"Description: {suggestion_description}")
