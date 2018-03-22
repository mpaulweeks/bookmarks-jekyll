---
layout: page
title: Clip Player
permalink: /clip/
---

<video id="player" width="500" controls>
</video>

<div>
  If the video is broken, please let me know <a href="https://twitter.com/mpaulweeks">@mpaulweeks</a>
</div>

<script defer>
  const s3url = window.location.search.split('s3=')[1];
  const videoUrl = 'https://s3.amazonaws.com/' + s3url;
  const videoElm = document.getElementById('player');
  const sourceElm = document.createElement('source');
  sourceElm.setAttribute('src', videoUrl);
  videoElm.appendChild(sourceElm);
  videoElm.play();
</script>
