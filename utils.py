from bottle import template
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143",
                  "175", "216", "1371", "1871", "2993", "305"]


def showData(AVAILABE_SHOWS):
    data = []
    for show in AVAILABE_SHOWS:
        data.append(json.loads(getJsonFromFile(show)))
    return data


def getVersion():
    return "0.0.1"


def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


def showEpisode(showId, episodeId):
    sectionData = json.loads(getJsonFromFile(showId))
    for ep in sectionData["_embedded"]["episodes"]:
        if ep["id"] == int(episodeId):
            sectionData = ep
    return sectionData


def search_result(search_value):
    shows = showData(AVAILABE_SHOWS)
    results = []
    for show in shows:
        for episode in show["_embedded"]["episodes"]:
            if (search_value.lower() in episode['name'].lower()):
                results.append(
                    {'showid': show['id'], 'episodeid': episode['id'], 'text': episode['name']})
            elif episode['summary'] and (search_value.lower() in episode['summary'].lower()):
                results.append(
                    {'showid': show['id'], 'episodeid': episode['id'], 'text': episode['name']})
    return results
