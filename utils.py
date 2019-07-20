from bottle import template
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143",
                  "175", "216", "1371", "1871", "2993", "305"]


def get_data(AVAILABE_SHOWS):
    data = []
    for show in AVAILABE_SHOWS:
        data.append(json.loads(get_json_from_file(show)))
    return data


def get_version():
    return "0.0.1"


def get_json_from_file(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


def get_episode(showId, episodeId):
    sectionData = json.loads(get_json_from_file(showId))
    for ep in sectionData["_embedded"]["episodes"]:
        if ep["id"] == int(episodeId):
            sectionData = ep
    return sectionData


def get_results(search_value):
    shows = get_data(AVAILABE_SHOWS)
    results = []
    for show in shows:
        for episode in show["_embedded"]["episodes"]:
            if (search_value.lower() in episode['name'].lower() or search_value.lower() in show['name'].lower()):
                results.append(
                    {'showid': show['id'], 'episodeid': episode['id'], 'text': f"{show['name']}: {episode['name']}"})
            elif episode['summary'] and (search_value.lower() in episode['summary'].lower()):
                results.append(
                    {'showid': show['id'], 'episodeid': episode['id'], 'text': f"{show['name']}: {episode['name']}"})
    return results
