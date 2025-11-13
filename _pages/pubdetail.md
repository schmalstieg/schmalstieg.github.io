---
permalink: /pubdetail.html
title: "Publication Details"
excerpt: "Publication Details"
author_profile: true
---

{% for i in site.data.articles %}
  <div id="{{ i.ID }}" style="display:none;">
    <div>
	  {{ i.author }}:
	</div><div>
	  <b>{{ i.title }}</b>
	</div><div>
	  {% if i.ENTRYTYPE=="inproceedings" %}
	    In <i>{{i.booktitle}}</i>,
	  {% elsif i.ENTRYTYPE=="article" %}
	    <i>{{i.journal}}</i>, 
	    {% if i.volume %}vol. {{i.volume}},{% endif%}
	    {% if i.issue %}num. {{i.issue}},{% endif%}
	  {% elsif i.ENTRYTYPE=="book" %}
	    <i>{{i.publisher}}</i>, 
	  {% endif %}
      {% if i.page %}pages {{i.page}},{% endif %}
	  {{ i.month }} {{ i.year }}{% if i.note %}, {{i.note}}{% endif %}.
    </div><div>
	  &nbsp;
    </div><div>
      <div id="abstract">{{ i.abstract }}</div>
      <button onclick="copyToClipboard()">Copy</button>
    </div><div>
	  &nbsp;
	</div>
    {% if i.video %}
      <div>
        <iframe width="560" height="315"
          src="https://www.youtube.com/embed/{{ i.video }}" 
          title="YouTube video player"
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen>
        </iframe>
	  </div>
    {% endif %}
  </div>
{% endfor %}

<html>
  <body>
    <script>
      const urlParams = new URLSearchParams(window.location.search);
      const myVar = urlParams.get('param'); 
      document.getElementById(myVar).style.display = 'block';
    </script>
	  <script>
        function copyToClipboard() {
          const textToCopy = document.getElementById("abstract").innerText;
          navigator.clipboard.writeText(textToCopy)
          .then(() => { alert("Text copied to clipboard!"); })
          .catch(err => { alert("Failed to copy text: " + err); });
        }
    </script>
  </body>
</html>
