import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template)
import utils
import json
# Static Routes


@post('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    sectionData = {"q": request.forms.get('q')}
    return template(sectionTemplate, version=utils.getVersion(), sectionTemplate=sectionTemplate, result=sectionData)


@get('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    sectionData = utils.showData()
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sorted(utils.showData(), key=lambda show: show["name"]))


@get('/show/<showId>')
def show_description(showId):
    sectionData = json.loads(utils.getJsonFromFile(showId))
    sectionTemplate = "./templates/show.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


@get('/ajax/show/<showId>')
def show_description(showId):
    sectionData = json.loads(utils.getJsonFromFile(showId))
    sectionTemplate = "./templates/show.tpl"
    return template(sectionTemplate, version=utils.getVersion(), sectionTemplate=sectionTemplate, result=sectionData)


@get('/show/<showId>/episode/<episodeId>')
def show_episode(showId, episodeId):
    sectionData = utils.showEpisode(showId, episodeId)
    sectionTemplate = "./templates/episode.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


@get('/ajax/show/<showId>/episode/<episodeId>')
def show_episode(showId, episodeId):
    sectionData = utils.showEpisode(showId, episodeId)
    sectionTemplate = "./templates/episode.tpl"
    return template(sectionTemplate, version=utils.getVersion(), sectionTemplate=sectionTemplate, result=sectionData)


@get('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sorted(utils.showData(), key=lambda show: show["name"]))


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
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


run(host='localhost', port=8000, reloader=True, debug=True)
