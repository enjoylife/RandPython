import numpy as np
from twython import Twython

twitter = Twython()
trends = twitter.getDailyTrends(exclude='hashtags')
for trend in trends['trends']: # loop index is over time of pop trends
    print trends['trends'][trend][0]['query'] # trends{'trends':2012-1-31 19:00:[{"name":"...", "query":"...}]
