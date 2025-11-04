---
permalink: /pubdetail.html
title: "Publication Details"
excerpt: "Publication Details"
author_profile: true
---

<script>
  // Parse URL search parameters
  const urlParams = new URLSearchParams(window.location.search);
  const paramValue = urlParams.get('param'); // 'param' is the name of the query parameter

  if(paramValue) {
    // Insert the parameter value into an element with id="output"
    document.getElementById('output').textContent = paramValue;
  }
  else
  {
    document.getElementById('output').textContent = 'NONE';
  }
  else</script>

<p>Parameter value: <span id="output"></span></p>
