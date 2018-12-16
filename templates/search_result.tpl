% include("./templates/search.tpl")
<br><br>
<h2>Search Results for '{{query}}'</h2>
<ul class="search-results">
% for r in results:
<li class="search-result" onclick="Browse.loadEpisode('{{r['showid']}}', '{{r['episodeid']}}')">{{r['text']}}</li>
% end
% if not results:
    No Resutls :(
% end

</ul>