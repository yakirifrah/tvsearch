<h1>Browse your favorite TV show</h1>
<div class="browse">
% for show in result:
    <article class="clickable shadowed" onclick="Browse.loadShow('{{show['id']}}')">
        <div class="rating">
            <i class="fas fa-star"></i><span class="average">{{show['rating']['average']}}</span>
        </div>
        <div class="cover-holder">
            <img src="{{show['image']['original']}}" class="show-cover"/>
        </div>
        <h3 class="show-name">{{show['name']}}</h3>
    </article>
% end
</div>