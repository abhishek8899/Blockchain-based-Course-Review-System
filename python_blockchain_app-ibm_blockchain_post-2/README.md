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

Install the dependencies,
Some requirements will have to be added separtely as there were installation errors when mentioned in requirements.txt
```sh
$ cd project/dir
$ pip install -r requirements.txt
```

Start a blockchain node server,

```sh
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
