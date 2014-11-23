import logging
import os

from twitter import *

from drunkzackkitz import markov
from drunkzackkitz import utils

logging.basicConfig(level=logging.INFO)


OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')
OAUTH_SECRET = os.environ.get('OAUTH_SECRET')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')

if not OAUTH_TOKEN or not OAUTH_SECRET or not CONSUMER_KEY or not CONSUMER_SECRET:
    raise Exception('missing environment variable')

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

filename = "drunkzackkitz/scripts/zack.txt"
orange = utils.file_to_words(filename)

markov = markov.Markov(orange)
markov.prime_cache()

def generate():
    pairs = markov.generate(size=17)

    # Strip off the @ replies. Twittar doesn't like that
    txt = ' '.join(pairs).replace('@', '')

logging.info(txt)
logging.info(len(txt))

txt = generate()
try:
    t.statuses.update(status=txt)
except:
    txt = generate()
    t.statuses.update(status=txt)
