<h1>{{result['name']}}</h1>
<%
    season = 0
%>
<div class="show">
% for ep in result['_embedded']['episodes']:
    % if ep["season"] > season:
        % if season > 0:
        </div>
        % end
    <div class="season">
    <h2 class="season-title clickable {{ !'shown' if ep["season"] == 1 else ''}}" onclick="this.classList.toggle('shown')"><i class="fas fa-film"></i>Season {{ep["season"]}}</h2>
    <%
    season += 1
    %>
    % end
    <article class="clickable shadowed" onclick="Browse.loadEpisode('{{result['id']}}', '{{ep['id']}}')">
        <div class="cover-holder">
            % if ep['image']:
                <img src="{{ep['image']['original']}}" class="show-cover"/>
            % else:
                <img src="/images/noimage.png" class="show-cover"/>
            % end
        </div>
        <h3 class="show-name">{{ep['name']}}</h3>
    </article>
% end
</div>
</div>