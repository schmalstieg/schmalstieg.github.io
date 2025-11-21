---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

<a href="/all.html">&rarr; all publications</a>

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
  <tr><td style="width: 20%;"><img src="/img/{{i.ID}}.jpg" width="200"></td><td style="width: 80%;">
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
  [&nbsp;
	{%- if i.abstract -%}<a href="/pubdetail.html?param={{i.ID}}">details</a>{%- endif -%}
	{%- if i.url -%}&nbsp;<a href="/pdf/{{ i.ID }}.pdf">pdf</a>{%- endif -%}
	{%- if i.doi -%}&nbsp;<a href="https://doi.org/{{- i.doi -}}">doi</a>{%- endif -%}
	{%- if i.youtube -%}&nbsp;<a href="https://youtu.be/{{ i.youtube }}">video</a>{%- endif -%}
	&nbsp;]
  </td></tr>
{% endif %}
{% endfor %}
</table>
