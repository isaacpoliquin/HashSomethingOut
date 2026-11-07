# Name: Isaac Poliquin
# Description: This assignment is a work in progress. 
#               I did not finish in time. All it does is read in the movies
#               and print the first four. This will be revised.


categories = ["movie_title","genre","release_date","director","box_office_revenue","rating","duration_minutes","production_company","quote"]

def split_line(line):
    fields = []
    current = ""
    in_quotes = False

    for ch in line:
        if ch == '"':
            in_quotes = not in_quotes
        elif ch == "," and not in_quotes:
            fields.append(current.strip())
            current = ""
        else:
            current += ch

    fields.append(current.strip())
    return fields

def parse_movies(file):
    movies = []
    data = open(file, "r", encoding="utf-8")
    next(data)
    for line in data:
        line = line.rstrip("\n")
        if not line:
            continue
        fields = split_line(line)

        movie = {}
        for i in range(len(categories)):
            if i < len(fields):
                movie[categories[i]] = fields[i]
            else:
                movie[categories[i]] = ""
        movies.append(movie)
    return movies

# def hashvalue(text):
#     total = 0
#     for ch in text:
#         total += ord(ch)
#     return total

Table_Size = 1500

movies = parse_movies("MOCK_DATA.csv")

for movie in movies[:4]:
    print(movie)

# def createMovie(title, genre, rating, munny, company, quote, producer):
#     movie = {
#         "title": title,
#         "genre": genre, 
#         "rating": rating,
#         "money": munny, 
#         "company": company,
#         "quote": quote, 
#         "producer": producer
#     }
#     return movie

# movieToAdd = createMovie("lkafdjka", "fj;dsafh", "lakfja", "al;dksfj", "kalsdjf;", "dakl;sfj", "oiads")

# key = hashValue(movieToAdd["title"])
# # put into title hash table 

# key = hashvalue(movieToAdd["quote"])
# # put into the quote has table

# #then modulo the key

# #make the hash table just a list
