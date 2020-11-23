# Course review system - Web application

We propose an effective anonymous review system called ReviewCoins, a novel Blockchain-based incentive anonymous review system. Different from the traditional centralized system, the novel anonymous review system should be secure, reliable, transparent, and tamper-resistant. 

## Why blockchain?

Blockchain-based networks are open and transparent, and promising in recording data with the good properties of tamper-resistance and decentralization.
Blockchain can provide a better incentive mechanism to encourage mobile users to perform anonymous reviews without the worry of identity information disclosure.

## Rcoins

Rcoins refer to the incentive in this blockchain based course review system. Each user has an independent digital credit account, which is used to store reputation points and which is therefore called as the Rcoins. 
Sending a review will cost Rcoins, which prevents malicious users from sending meaningless or fraudulent reviews. After a block is added successfully Reviewer and Verifier will get rewards in Rcoins. We can distinguish the users on the basis of roles. For example, not all the users have the privilege to verify the review. That way ownership will be maintained and not all people would be able to add the blocks to the chain. In case these tokens are not used for a period of time, then they will expire and no longer be used. Our system generates a mathematical problem. All those involved in the consensus process will compete to be the first to find a solution to this mathematical problem.
When the right solution is found, the entire network will broadcast that the user has the right to generate a new block and reward him with a small amount of Rcoins.

## Instructions to run

Clone the project,

```sh
$ git clone https://github.com/satwikkansal/python_blockchain_app.git
```

Install the dependencies,

```sh
$ cd python_blockchain_app
$ pip install -r requirements.txt
```

Start a blockchain node server,

```sh
# Windows users can follow this: https://flask.palletsprojects.com/en/1.1.x/cli/#application-discovery
$ export FLASK_APP=node_server.py
$ flask run --port 8000
```

One instance of our blockchain node is now up and running at port 8000.


Run the application on a different terminal session,

```sh
$ python run_app.py
```

The application should be up and running at [http://localhost:5000](http://localhost:5000).

Here are a few screenshots

1. Posting some content

![image.png](https://github.com/satwikkansal/python_blockchain_app/raw/master/screenshots/1.png)

2. Requesting the node to mine

![image.png](https://github.com/satwikkansal/python_blockchain_app/raw/master/screenshots/2.png)

3. Resyncing with the chain for updated data

![image.png](https://github.com/satwikkansal/python_blockchain_app/raw/master/screenshots/3.png)

To play around by spinning off multiple custom nodes, use the `register_with/` endpoint to register a new node. 

Here's a sample scenario that you might wanna try,

```sh
# already running
$ flask run --port 8000 &
# spinning up new nodes
$ flask run --port 8001 &
$ flask run --port 8002 &
```

You can use the following cURL requests to register the nodes at port `8001` and `8002` with the already running `8000`.

```sh
curl -X POST \
  http://127.0.0.1:8001/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://127.0.0.1:8000"}'
```

```sh
curl -X POST \
  http://127.0.0.1:8002/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://127.0.0.1:8000"}'
```

This will make the node at port 8000 aware of the nodes at port 8001 and 8002, and make the newer nodes sync the chain with the node 8000, so that they are able to actively participate in the mining process post registration.

To update the node with which the frontend application syncs (default is localhost port 8000), change `CONNECTED_NODE_ADDRESS` field in the [views.py](/app/views.py) file.

Once you do all this, you can run the application, create transactions (post messages via the web inteface), and once you mine the transactions, all the nodes in the network will update the chain. The chain of the nodes can also be inspected by inovking `/chain` endpoint using cURL.

```sh
$ curl -X GET http://localhost:8001/chain
$ curl -X GET http://localhost:8002/chain
```
