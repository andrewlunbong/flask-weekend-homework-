from app import app
from flask import render_template, request, redirect
from models.books import *
from models.book import *




@app.route('/books')
def index():
    return render_template('index.jinja', title = "Home", books = book_list)

@app.route('/books/<index>')
def single_book(index):
  book = book_list[int(index) -1 ]
  return render_template('book.jinja', book = book, title = "Book")

@app.route('/books/delete', methods=['POST'])
def remove_book():
   banana = request.form['book']
   delete_book(banana)
   return redirect('/books')

@app.route('/books', methods=['POST']) 
def add_books():
    name=request.form['add_name']
    author=request.form['add_author']
    genre=request.form['add_genre']
    new_book=Book(name, author, genre)
    add_new_books(new_book)
    return redirect('/books')



   



