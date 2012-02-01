#!/user/bin/env python

#majority
from collections import Counter

#twitter_search
import requests
import urllib
import json

def majority(votes):
    
    C = Counter(votes)
    maj = sum(C.values()) / 2.0
    pair = C.most_common(1)[0] # in case of a tie
    return pair[0] if pair[1] > maj else None

def twitter_search(words,  twit_pages=8):
    """input: iterable of words, returns a list of results """

    sentences=[]
    twit_base ="http://search.twitter.com/search.json?"
    for page in range(1,twit_pages):
        print "adding new sentences for page %s" % page
        twit_ops = {'lang':'en', 'result_type':'mixed','include_entities':1,'page':page, 'rpp':100,
                'q': ' '.join(words)}
        r =requests.get(twit_base+urllib.urlencode(twit_ops), prefetch=True)
        content = json.loads(r.content)
        for sents in content['results']:
            # Dont want retweets 
            if not sents['text'].startswith('RT'):
                new_sent = sents['text']
                # Test if their is urls in string, if so remove them before appending
                if sents['entities'].get('urls', False):
                    for urls in sents['entities'].get('urls'):
                        i = urls['indices']
                        # Hackish with indices
                        new_sent=sents['text'].replace(sents['text'][i[0]:i[1]],'')
                sentences.append(new_sent.encode('utf-8'))
    return sentences


if __name__ == '__main__':
    print (majority(['a', 'b', 'a', 'b', 'a']))
    print (majority(['a', 'a', 'a', 'c', 'c', 'b', 'b', 'c', 'c', 'c', 'b', 'c', 'c']))
    print (majority(['a', 'b', 'c', 'a', 'b', 'a']))
