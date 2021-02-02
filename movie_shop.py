class movie:
    movies = []
    def __init__(self, title, director, year, actors):
        self.title = title
        self.director = director
        self.year = year
        self.actors = actors
        movie.movies.append(self)

    def __str__(self):
        return f"{self.title} by {self.director}, {self.year}"

movie("amarcord", "federico fellini", 1974, ["magali noel", "bruno zanin", "pupella maggio", "armando drancia"])
movie("the big easy", "jim mcbridge", 1987, ["dennis quaid", "ellen brakin", "ned beatty", "lisa jane persky", "john goodman", "charles ludlam"])
movie("the godfather", "francis ford coppola", 1972, ["marlon brando", "al pacino", "james caan", "robert duvall", "diane keaton"])
movie("boyz n the hood", "john singleton", 1991, ["cuba gooding jr.", "larry fishburne", "tyra ferrell", "morris chestnut"])

def movies_made_in_year(year, list_of_movies = movie.movies):
    return [str(x) for x in filter(lambda m: m.year == year, list_of_movies)]

def movies_made_by(name, list_of_movies = movie.movies):
    return [str(x) for x in filter(lambda m: m.director == name, list_of_movies)]

def movies_with_author(name, list_of_movies = movie.movies):
    return [str(x) for x in filter(lambda m: name in m.actors, list_of_movies)]

def titles_of_movies_astisfying(procedure, list_of_movies = movie.movies):
    return [str(x.title) for x in filter(lambda movie: eval(procedure), list_of_movies)]

def titles_of_movies_astisfying_with_comprehension(procedure, list_of_movies = movie.movies):
    return [str(movie.title) for movie in list_of_movies if eval(procedure)]




# print(movies_made_in_year(1987))
# print(movies_made_by('john singleton'))
# print(movies_with_author("tyra ferrell"))
#print(titles_of_movies_astisfying_with_comprehension("movie.year == 1974")) # the function to end all functions

valid_query = ["year", "made", "director", "directed", "actors", "between"]
def query(words, list_of_movies=movie.movies):
    if "so long" in words or "bye" in words:
        return "Bye!"

    if not set(valid_query).intersection(set(words.split())):
        return "Invalid Query!"

    if "in year" in words or "made in" in words:
        return titles_of_movies_astisfying(f"str(movie.year) in '{words}'")
    if "director" in words or "directed by" in words:
        return titles_of_movies_astisfying(f"movie.director in '{words}'")
    if "actors in" in words or "acted in" in words:
        return [movie.actors for movie in list_of_movies if movie.title in words]
    if "made between" in words:
        val = [int(x) for x in words.split() if x.isdigit() and len(x) == 4]
        return [movie.title for movie in list_of_movies if movie.year in range(min(val), max(val))]
    return "No results"
    


print(query("movies made in year 1974"))
print(query("movies directed by john singleton"))
print(query("actors in boyz n the hood"))
print(query("what movies were made between 1985 and 1990"))
print(query("why is the sky blue"))
print(query("so long"))
