---
layout: page
title: Clip Player
permalink: /clip/
---

<p id="title">
  loading...
</p>

<p class="center">
  <video id="player" width="100%" controls></video>
</p>

<p>
  If the video is broken, please let me know <a href="https://twitter.com/mpaulweeks">@mpaulweeks</a>
</p>

<script defer>
  const title = window.location.search.split('title=')[1].split('&')[0];
  document.getElementById('title').innerHTML = decodeURIComponent(title);

  const s3url = window.location.search.split('s3=')[1].split('&')[0];
  const videoUrl = 'https://s3.amazonaws.com/' + s3url;
  const videoElm = document.getElementById('player');
  const sourceElm = document.createElement('source');
  sourceElm.setAttribute('src', videoUrl);
  videoElm.appendChild(sourceElm);
  // videoElm.play();
</script>
