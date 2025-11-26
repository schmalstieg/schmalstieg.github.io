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
	  {% if i.doi %}
	    <div><img src="/images/doi.png" width=20>&nbsp;<a href="https://doi.org/{{ i.doi }}">{{ i.doi }}</a></div>
	  {% endif %}
	</div><div>
	  &nbsp;
    </div><div id="abstract">
	  <table><tr><td>{{ i.abstract }}</td></tr></table>
    </div>
	<div>&nbsp;</div>
	<div><button onclick="copyAbstractToClipboard()">Copy Abstract</button>
	  {% if i.url %}&nbsp;&nbsp;&nbsp; 
	    <img src="/images/pdf.png" width=20>&nbsp;<a href="/pdf/{{ i.ID }}.pdf">Download PDF</a>
	  {% endif %}
	  {% if i.youtube %}
	    &nbsp;&nbsp;&nbsp;<img src="/img/{{i.ID}}.jpg" width=50>
        <a href="https://www.youtube.com/embed/{{ i.youtube }}">Watch video</a>
	  {% endif %}
	</div>
	<div>&nbsp;</div>
    <div id="{{ i.ID }}bib" style="display:none;">
      <div id="bibtex">
	  <table><tr><td>
      <pre style="white-space: pre-line; word-wrap: break-word;">
	    {% if i.ENTRYTYPE=="inproceedings" %}@inproceedings{ {{i.ID}},
            author={ {{ i.author | replace: ",", " and" }} },
            title={ {{ i.title }} },
            year={ {{ i.year }} },
            month={ {{ i.month }} },
	        booktitle={ {{i.booktitle}} },
            pages={ {{i.page}} },
			doi={ https://doi.org/{{i.doi}} },
	      }
        {% elsif i.ENTRYTYPE=="article" %}@article{ {{i.ID}},
            author={ {{ i.author | replace: ",", " and" }} },
            title={ {{ i.title }} },
            journal={ {{i.journal}} }, 
            author={ {{ i.author }} },
            year={ {{ i.year }} },
            month={ {{ i.month }} },
	        volume={ {{i.volume}} },
	        number={ {{i.issue}} },
            pages={ {{i.page}} },
			doi={ https://doi.org/{{i.doi}} },
	      }
	    {% elsif i.ENTRYTYPE=="book" %}@book{ {{i.ID}},
            author={ {{ i.author | replace: ",", " and" }} },
            title={ {{ i.title }} },
	        publisher={ {{i.publisher}} }, 
            year={ {{ i.year }} },
	      }
        {% endif %}</pre>
	  </td></tr></table>
	  </div>
	  <button onclick="copyBibToClipboard()">Copy Bibtex</button>
    </div>
  </div>
{% endfor %}

<html>
  <body>
    <script>
      const urlParams = new URLSearchParams(window.location.search);
      const myVar = urlParams.get('param'); 
      document.getElementById(myVar).style.display = 'block';
      document.getElementById(myVar+"bib").style.display = 'block';
	</script>
	<script>
        function copyAbstractToClipboard() {
          const textToCopy = document.getElementById("abstract").innerText;
          navigator.clipboard.writeText(textToCopy)
          .then(() => { alert("Text copied to clipboard!"); })
          .catch(err => { alert("Failed to copy text: " + err); });
        }
    </script>
	<script>
        function copyBibToClipboard() {
          const textToCopy = document.getElementById("bibtex").innerText;
          navigator.clipboard.writeText(textToCopy)
          .then(() => { alert("Text copied to clipboard!"); })
          .catch(err => { alert("Failed to copy text: " + err); });
        }
    </script>
  </body>
</html>
