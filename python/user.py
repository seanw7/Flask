from database import CursorFromConnectionFromPool
import oauth2
from twitter_utils import consumer
import json



class User():
    def __init__(self, screen_name, oauth_token, oauth_token_secret, id):

        self.screen_name = screen_name
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.id = id

        # REPR method allows you to print an object, it must return a string
    def __repr__(self):
        return "<User: {}>".format(self.screen_name)

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            # next we use the cursor. It is a tool that lets you retrieve data and read it row by row
            # Running some code... inserting values into users table. Remember that ID is self-incrementing.
            cursor.execute('INSERT INTO users (screen_name, oauth_token, oauth_token_secret) '
                           'VALUES (%s, %s, %s)',
                           (self.screen_name, self.oauth_token, self.oauth_token_secret,))

    @classmethod  # This method doesnt access the currently bound object. 'cls' stand for currently bound class
    def load_from_db_by_screen_name(cls, screen_name):
        with CursorFromConnectionFromPool() as cursor:
            # undeclared variable in a string, email var at the top
            cursor.execute('SELECT * FROM users WHERE screen_name=%s', (screen_name,))
            # we have to define a tuple here because it thinks the parenthesis around email aren't needed.
            # we do that by adding a ',' comma in behind email like this (email,) this lets python know its a tuple
            # cursor.fetchone() should get us the first user with that email.
            user_data = cursor.fetchone()
            # this is how you return the row from postgres. you can change the index order of returned items like this
            if user_data:
                return cls(screen_name=user_data[1], oauth_token=user_data[2], oauth_token_secret=user_data[3], id=user_data[0])


    def twitter_request(self, uri, verb='GET'):
        authorized_token = oauth2.Token(self.oauth_token, self.oauth_token_secret)
        authorized_client = oauth2.Client(consumer, authorized_token)

        #making twitter api calls!
        response, content = authorized_client.request(uri, verb)
        if response.status != 200:
            prnt("An error ocurred when searching!")

        return json.loads(content.decode('utf-8'))


