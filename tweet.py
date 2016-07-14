import twitter
import os
import sys
import markov

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

print api.VerifyCredentials()

input_path = " ".join(sys.argv[1:])
# Open the file and turn it into one long string
input_text = markov.open_and_read_file(input_path)
# Get a Markov chain and pass in number of words for the n-gram
chains = markov.make_chains(input_text, 2)
# Produce random text
random_text = markov.make_text(chains)

tweet_made = markov.make_tweet(random_text)

status = api.PostUpdate(tweet_made)

print tweet_made