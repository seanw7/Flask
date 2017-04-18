# Twitter Search app with Sentiment analysis.

## How to install the app
Install docker.
Open docker cli and navigate to the directory where you copied the project.
Type docker-compose up --build, and wait for a few moments while it makes the containers.

###To use this app.
After bringing up the docker-compose, go to your browser and point it to your docker-machines', or your containers ip and port 4995
an example (192.168.99.100:4995)
This will take you to the homepage. Now you can log in through the twitter auth page and make searches.

After you are done, you should type

'''
docker-compose down
'''
To bring down the running docker containers.
