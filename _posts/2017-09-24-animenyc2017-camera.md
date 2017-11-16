---
layout: panel
title: The Simulated Camera
convention: Anime NYC 2017
location: Friday 3:30PM in Panel Room 2
type: panel
isLive: true
permalink: /animenyc-2017/simulated-camera/
descrip: Resources for a panel hosted at Anime NYC 2017
---

{% assign data = site.data.conventions.animenyc-2017.simulated-camera %}

<div class="manga-header">Panel Description</div>
<div class="panel-description">{{data.description}}</div>

<div class="manga-header">
  Clips
  <div class="minor">video sources linked where available</div>
</div>
{% include links.html links=data.clips %}

<div class="manga-header"> Sources and Inspiration </div>
{% include links.html links=data.articles %}
