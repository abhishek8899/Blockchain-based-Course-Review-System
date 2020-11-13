import datetime
import json

import requests
from flask import render_template, redirect, request
import pickle
from app import app

# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []
blockchain = []
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

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)


@app.route('/')
def sample():
    fetch_posts()
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



@app.route('/form')
def index():
    fetch_posts()
    return render_template('index.html',
                           title='YourNet: Decentralized '
                                 'content sharing',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)

@app.route('/submit', methods=['POST'])
def submit_textarea():
    """
    Endpoint to create a new transaction via our application.
    """
    post_content = request.form["content"]
    course = request.form["course"]
    author = request.form["author"]

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

    return redirect('/form')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')
