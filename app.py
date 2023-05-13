from flask import Flask, redirect, url_for, request, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib
import pickle
import json
from flask_cors import CORS

app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost/flask/"}})
CORS(app)

# Load pretrained Model
with open('Movie_recommend.pkl', 'rb') as file:
   vectorizer,similarity,movies = pickle.load(file)
   

   
# @app.route('/api/recommendations', methods=['POST'])
# def get_recommendations():
#    if request.method == 'POST':
      
#       movie_name = request.json.get('movie_name')
#       list_of_all_titles = movies['movie title'].tolist()

#       find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

#       close_match = find_close_match[0]

#       index_of_the_movie = movies[movies['movie title'] == close_match]['index'].values[0]

#       similarity_score = list(enumerate(similarity[index_of_the_movie]))

#       sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

#       movieList = []
#       for movie in sorted_similar_movies:
#          index = movie[0]
#          title_from_index = movies[movies.index==index]['movie title'].values[0]

#          movieList.append(title_from_index)

#       return jsonify({'movies': movieList[:10]})



   
@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
   
   movie_name = request.args.get('name')
   list_of_all_titles = movies['movie title'].tolist()

   find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

   close_match = find_close_match[0]

   index_of_the_movie = movies[movies['movie title'] == close_match]['index'].values[0]

   similarity_score = list(enumerate(similarity[index_of_the_movie]))

   sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
   
   movieList = []
   for movie in sorted_similar_movies:
      index = movie[0]
      title_from_index = movies[movies.index==index]['movie title'].values[0]
      
      movieList.append(title_from_index)
      
   return jsonify({'movies': movieList[:10]})

   
@app.route('/')
def index():
   return render_template('index.html')

   
if __name__ == "__main__":
   app.run(debug=True, port=2121)