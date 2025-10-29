---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from:
  - /about.html
---
<style>
  table {
    border-collapse: collapse;
    border-spacing: 0;
    border: none;
  }
  th, td {
    border: none !important;
    border-style: none;
    padding: 8px;
  }
</style>


Dieter Schmalstieg is Alexander von Humboldt Professor of Visual Computing at the University of Stuttgart, Germany. He is also an adjunct professor at the Institute of Visual Computing at Graz University of Technology, Austria. His current research interests are augmented reality, virtual reality, computer graphics, visualization and human-computer interaction. He received Dipl.-Ing. (1993), Dr. techn. (1997) and Habilitation (2001) from Vienna University of Technology. He is author and co-author of over 400 peer-reviewed scientific publications with over 30,000 citations and over twenty best paper awards and nominations. His current and past organizational roles include associate editor in chief of IEEE Transactions on Visualization and Computer Graphics, associate editor of Frontiers in Robotics and AI, member of the steering committee of the IEEE International Symposium on Mixed and Augmented Reality, chair of the EUROGRAPHICS working group on Virtual Environments, and key researcher of the K-Plus Competence Centers VRVis (Vienna) and Know-Center (Graz). In 2002, he received the START career award presented by the Austrian Science Fund. In 2008, he founded the Christian Doppler Laboratory for Handheld Augmented Reality. In 2012, he received the IEEE Virtual Reality technical achievement award, and, in 2020, the IEEE ISMAR Career Impact Award. He was elected as Fellow of IEEE, as a member of the Young Curia of the Austrian Academy of Sciences, the Academia Europaea, and the IEEE VGTC Virtual Reality Academy. 

<h1>Team</h1>

<a href="https://www.visus.uni-stuttgart.de/arbeitsgruppen/schmalstieg-group/">VISUS</a>, University of Stuttgart -------- 
<a href="https://ivc.tugraz.at/">Institute of Visual Computing</a>, Graz

<h1>Selected Publications</h1>

{% assign sorted_list = site.data.articles %}
{% assign this_year = "2999" %}
{% assign idx = 1 %}

<table style="width: 600px;">
{% for i in sorted_list %}
{% if i.selected=="1" %}
  {% assign last_year = this_year %}
  {% assign this_year = i.year %}
  {% assign idx = idx | plus: 1 %}
  {% if last_year != this_year %}<tr><td colspan="2" style="text-align: center;"><h2>{{this_year}}</h2></td></tr>{% endif %}
  <tr><td style="width: 20%;"><img src="img/{{i.ID}}.jpg" width="200"></td><td style="width: 80%;">
    {{i.author}}:
    <b>{{ i.title }}</b>
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
  [<a href="bib/{{i.ID}}.bib">bib</a>
	{%- if i.abstract -%}, <a href="abstract/{{i.ID}}.txt">abstract</a>{%- endif -%}
	{%- if i.url -%}, <a href="/pdf/{{ i.ID }}.pdf">pdf</a>{%- endif -%}
	{%- if i.doi -%}, <a href="https://doi.org/{{- i.doi -}}">doi</a>{%- endif -%}
	{%- if i.video -%}, <a href="{{ i.video }}">video</a>{%- endif -%}
	]
  </td></tr>
{% endif %}
{% endfor %}
</table>
