import datetime
import json

import requests
import pickle
# from app import app
from flask import Blueprint, render_template, redirect, request, Response
from flask_login import login_required, current_user
from wtforms import TextField, Form
from wtforms.validators import InputRequired
from app import constants

main = Blueprint('main', __name__)


# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

# posts = []
blockchain = []
current_course = '*'
try:
    blockchain = []
    with open('config.chain', 'rb') as config_chain_file:
        blockchain = pickle.load(config_chain_file)
except:
    blockchain = []

for block in blockchain:
    print(block)
def fetch_posts():
    """
    Function to fetch the chain from a blockchain node, parse the
    data and store it locally.
    """
    posts = []
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)
    return posts


@main.route('/')
def sample():
    global current_course
    current_course = '*'
    posts = fetch_posts()
    return render_template('sample.html',
                           posts=posts,
                           p1 = posts[0],
                           p2 = posts[1],
                           p3 = posts[2],
                           p4 = posts[3],
                           p5 = posts[4],
                           p6 = posts[5],
                           num_reviews = len(posts),
                           blockchain_len = len(blockchain),
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)



@main.route('/submit_review')
@login_required
def submit_review():
    global current_course
    current_course = '*'
    posts = fetch_posts()
    form = SearchForm(request.form)
    return render_template('submit_review.html',
                           title='YourNet: Decentralized '
                                 'content sharing',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string,
                           form=form)

# this handles ONLY submit of "course reviews"
@main.route('/submit', methods=['POST'])
@login_required
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """
    post_content = request.form["content"]
    course = request.form['autocomp']
    # author = request.form["author"]
    author = current_user.name

    post_object = {
        'author': author,
        'course': course,
        'content': post_content,
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/submit_review')

@main.route('/profile')
@login_required
def profile():
    global current_course
    current_course = '*'
    return render_template('profile.html', name=current_user.name)


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')

class SearchForm(Form):
    autocomp = TextField('Course Name', id='course_name_autocomplete', validators=[InputRequired()])

@main.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(constants.COURSE_NAMES), mimetype='application/json')

@main.route('/courses')
@login_required
def course_search():
    global current_course
    if current_course == '*':
        posts = []
    else:
        posts = fetch_posts()
        result_post = []
        for post in posts:
            if post['course'] == current_course:
                result_post.append(post)
        posts = result_post

    form = SearchForm(request.form)
    return render_template('course_search.html',
                           title='YourNet: Decentralized '
                                 'content sharing',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string,
                           form=form)

@main.route('/search_submit', methods=['POST'])
@login_required
def course_search_submit():
    """
    Endpoint to create a new transaction via our application.
    """
    course = request.form['autocomp']
    global current_course
    current_course = course

    return redirect('/courses')