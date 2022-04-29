import requests

def get_embed_codes(tid):
    try:
        result = requests.get('https://publish.twitter.com/oembed?url=https%3A%2F%2Ftwitter.com%2FXXX%2Fstatus%2F'+tid)
        return result.json()['html'].strip();
    except:
        return "<blockquote class='missing'>This tweet is no longer available.</blockquote>";