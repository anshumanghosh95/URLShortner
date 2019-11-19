# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
from database import create_url, page_url, search_url

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        curr_url = request.form['url']
        create = create_url({'url':curr_url})
        return render_template("tinyurl.html", name = create.tinyurl())
    return render_template("shortner.html")

@app.route('/search', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['search']
        pages = search_url(keyword)
        page = pages.search()
        return render_template("searchresult.html", name = page)
    return render_template("search.html")

@app.route('/<page_id>')
def page_route(page_id):
    page = page_url(page_id)
    page = page.page_name()
    if ('https://' or 'http://') not in page:
        page = 'https://' + page
    return redirect(page)
 
if __name__ == "__main__":
    app.run(debug= True)