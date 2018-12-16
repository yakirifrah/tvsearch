Browse = {}

window.onpopstate = function(event) {
  // "event" object seems to contain value only when the back button is clicked
  // and if the pop state event fires due to clicks on a button
  // or a link it comes up as "undefined" 

  if(event){
    //this is a regular page
    if (!event.state){
      window.location.reload();
    }
    // Code to handle back button or prevent from navigation
    if (event.state.stateType){
      switch (event.state.stateType){
        case "show":
          Browse.loadShow(event.state.showId, false);
          break;
        case "episode":
          Browse.loadEpisode(event.state.showId, event.state.episodeId, false);
          break;
      }
    }else{
      console.log("what?", event)
    }
  }
}

Browse.loadContent = function(path, updateHistory = true, stateObj = {}){
  const dynamic = document.getElementById("dynamic");
  dynamic.innerHTML = "";
  dynamic.classList.add("loading");
  fetch(`/ajax${path}`)
  .then(function (response) {
    return response.text();
  })
  .then(function (result) {
      if (updateHistory){
        window.history.pushState(stateObj, "Ajax Load", path);
      }
      dynamic.innerHTML = result;
      dynamic.classList.remove("loading");
  });

}

Browse.loadShow = function(showid, updateHistory = true){
  Browse.loadContent(`/show/${showid}`,updateHistory, {"stateType":"show", "showId":showid});
}

Browse.loadEpisode = function(showid, episodeid, updateHistory = true){
  Browse.loadContent(`/show/${showid}/episode/${episodeid}`,updateHistory, {"stateType":"episode", "showId":showid, "episodeId":episodeid});
}