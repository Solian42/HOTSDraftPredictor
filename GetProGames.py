import urllib, json, pickle

urls = dict()
urls[0] = "https://api.hotslogs.com/Public/Events/1124"
urls[1] = "https://api.hotslogs.com/Public/Events/1123"
urls[2] = "https://api.hotslogs.com/Public/Events/1151"
urls[3] = "https://api.hotslogs.com/Public/Events/1132"
urls[4] = "https://api.hotslogs.com/Public/Events/1148"

data = dict()
i = 0
for url in urls.itervalues():
    response = urllib.urlopen(url)
    data[i] = json.loads(response.read())
    i += 1
allReplays = list()
for tourney in data.itervalues():
    for replay in tourney[u'Replays']:
        allReplays.append(replay)
pickle.dump(allReplays, open("pro_replays.data", "wb"))