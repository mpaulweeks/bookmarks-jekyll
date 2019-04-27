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

{% assign data = site.data.convention-2018-animeboston.simulated-camera %}

View current schedule and additional info on the <a href="http://www.animeboston.com/coninfo/schedule_panel/2634">Anime Boston website</a>

<div class="manga-header">Panel Description</div>
<div class="panel-description">{{data.description}}</div>

<div class="manga-header">Preshow</div>
{% include links.html links=data.preshow %}

<div class="manga-header">Resources</div>
{% include links.html links=data.resources %}

<div class="manga-header">
  Clips
  <div class="minor">sakugabooru linked where available</div>
</div>
{% include links.html links=data.clips %}

<div class="manga-header"> Sources and Inspiration </div>
{% include links.html links=data.articles %}

*See also: an earlier version of this panel from <a href="/animenyc-2017/simulated-camera/">AnimeNYC 2017</a>*
