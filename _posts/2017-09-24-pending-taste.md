---
layout: panel
title: How to Taste
convention: ???
location: ???
type: panel
isLive: false
permalink: /pending/taste/
descrip: Resources for a panel hosted at ???
---

{% assign data = site.data.conventions.pending.taste %}

<div class="manga-header">Panel Description</div>
<div class="panel-description">{{data.description}}</div>

An earlier version of this panel: <a href="/acen-2017/diagnosing-taste/">How to Diagnose Your Anime Taste</a>

<div class="manga-header">Resources</div>
{% include links.html links=data.resources %}

<div class="manga-header"> Articles </div>
{% include links.html links=data.articles %}

<div class="manga-header"> Videos </div>
{% include links.html links=data.videos %}
