import json

jsondata = {
    "word2vecfile": "/content/GoogleNews-vectors-negative300.bin",
    "choidataset": "/content/text-segmentation/data/choi",
    "wikidataset": "/content/wiki_727",
}

with open('config.json', 'w') as f:
    json.dump(jsondata, f)
