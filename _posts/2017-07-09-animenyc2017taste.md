---
layout: panel
title: How to Taste
convention: Anime NYC 2017
type: panel
isLive: false
permalink: /animenyc-2017/taste/
descrip: Resources for a panel hosted at Anime NYC 2007
---

{% assign data = site.data.conventions.animenyc-2017.taste %}

<div class="manga-header">Panel Description</div>
<div class="panel-description">{{data.description}}</div>

An earlier version of this panel: <a href="/acen-2017/diagnosing-taste/">How to Diagnose Your Anime Taste</a>

<div class="manga-header">Resources</div>
{% include links.html links=data.resources %}

<div class="manga-header"> Articles </div>
{% include links.html links=data.articles %}

<div class="manga-header"> Videos </div>
{% include links.html links=data.videos %}
