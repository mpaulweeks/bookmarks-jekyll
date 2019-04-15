---
layout: panel
title: Music That Moves You
convention: Castle Point 2019
location: Sunday 11:45AM in TBD
type: panel
isLive: false
permalink: /castlepoint-2019/music
descrip: Resources for a panel hosted at Castle Point Anime Convention 2019
---

{% assign data = site.data.convention-2019-castlepoint.music %}

<div class="manga-header">Panel Description</div>
<div class="panel-description">{{data.description}}</div>

<!-- <div class="manga-header">Preshow</div> -->
<!-- {% include links.html links=data.preshow %} -->

<div class="manga-header">
  Clips
</div>
{% include links.html links=data.clips %}

<div class="manga-header"> Sources, Inspiration, and Further Reading </div>
{% include links.html links=data.articles %}
