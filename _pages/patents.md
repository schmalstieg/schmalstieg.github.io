---
layout: archive
title: "Patents"
permalink: /patents.html
author_profile: true
---

{% assign sorted_list = site.data.patents %}
{% assign this_year = "2999" %}
{% assign idx = 1 %}

<table style="width: 600px;">
{% for i in sorted_list %}
  {% assign last_year = this_year %}
  {% assign this_year = i.year %}
  {% assign idx = idx | plus: 1 %}
  {% if last_year != this_year %}<tr><td><h2>{{this_year}}</h2></td></tr>{% endif %}
  <tr><td>
    {{ i.author }}: <b>{{ i.title }}</b>. {{i.howpublished}}, granted {{ i.month }}, {{ i.year }}
  </td></tr>
{% endfor %}
</table>
