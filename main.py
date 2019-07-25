
import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template, redirect, error)
from utils import get_results, get_version, get_json_from_file, get_data, get_episode, AVAILABE_SHOWS
import json
from sys import argv


@post('/search')
def search_result():
    search_value = request.forms.get("q")
    results = get_results(search_value)
    return template(
        "./pages/index.html",
        version=get_version(),
        sectionTemplate='./templates/search_result.tpl',
        query=search_value,
        results=results,
        sectionData={}
    )


@get('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template(
        "./pages/index.html",
        version=get_version(),
        sectionTemplate=sectionTemplate,
        sectionData={}
    )


@get('/show/<showId>')
def show_description(showId):
    sectionData = json.loads(get_json_from_file(showId))
    sectionTemplate = "./templates/show.tpl"
    return template(
        "./pages/index.html",
        version=get_version(),
        sectionTemplate=sectionTemplate,
        sectionData=sectionData
    )


@get('/ajax/show/<showId>')
def show_description(showId):
    sectionData = json.loads(get_json_from_file(showId))
    sectionTemplate = "./templates/show.tpl"
    return template(sectionTemplate, result=sectionData)


@get('/show/<showId>/episode/<episodeId>')
def show_episode(showId, episodeId):
    sectionData = get_episode(showId, episodeId)
    sectionTemplate = "./templates/episode.tpl"
    return template(
        "./pages/index.html",
        version=get_version(),
        sectionTemplate=sectionTemplate,
        sectionData=sectionData
    )


@get('/ajax/show/<showId>/episode/<episodeId>')
def show_episode(showId, episodeId):
    sectionData = get_episode(showId, episodeId)
    sectionTemplate = "./templates/episode.tpl"
    return template(sectionTemplate, result=sectionData)


@get('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    return template(
        "./pages/index.html",
        version=get_version(),
        sectionTemplate=sectionTemplate,
        sectionData=sorted(get_data(AVAILABE_SHOWS),
                           key=lambda show: show["name"])
    )


@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")


@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template(
        "./pages/index.html",
        version=get_version(),
        sectionTemplate=sectionTemplate,
        sectionData={}
    )


@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template(
        "./pages/index.html",
        version=get_version(),
        sectionTemplate=sectionTemplate,
        sectionData={}
    )


run(host='0.0.0.0', port=argv[1])
