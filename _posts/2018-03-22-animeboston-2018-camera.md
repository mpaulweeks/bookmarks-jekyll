---
layout: panel
title: The Simulated Camera
convention: Anime Boston 2018
location: Saturday 11:30AM in Sheraton Panel Public Garden
type: panel
isLive: true
permalink: /animeboston-2018/camera
descrip: Resources for a panel hosted at Anime Boston 2018
---

{% assign data = site.data.conventions.animeboston-2018.simulated-camera %}

View current schedule and additional info on the <a href="http://www.animeboston.com/coninfo/schedule_panel/2634">Anime Boston website</a>

An earlier version of this panel: <a href="/animenyc-2017/simulated-camera/">AnimeNYC 2017 - The Simulated Camera</a>

<div class="manga-header">Panel Description</div>
<div class="panel-description">{{data.description}}</div>

<div>
  <br/>
  <a href="{{data.slides}}" target="_blank">Opening Slides</a>
</div>

<div class="manga-header">
  Clips
  <div class="minor">sakugabooru linked where available</div>
</div>
{% include links.html links=data.clips %}

<div class="manga-header"> Sources and Inspiration </div>
{% include links.html links=data.articles %}
