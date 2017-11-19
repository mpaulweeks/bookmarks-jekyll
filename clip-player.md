---
layout: page
title: Clip Player
permalink: /clip/
---

<video id="player" width="500" controls>
</video>

<div>
  Is the video not showing up? Try downloading the file (with the above arrow).
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
