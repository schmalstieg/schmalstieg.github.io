---
permalink: /areas.html
title: "Research Areas"
excerpt: "Research Areas"
author_profile: true
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

{% for subgroup in site.data.areas %}
<details>
  <summary><b>{{ subgroup.heading }}</b></summary>
  {{ subgroup.description }}
  <table style="width: 650px;">
    <tr>
      {% assign counter = 0 %}
      {% for item in subgroup.papers %}
        <td ><a href="/pdf/Schmalstieg_{{ item }}.pdf"><img src="/img/Schmalstieg_{{ item }}.jpg" width=200 alt="{{ item.title }}"></a></td>
        {% assign counter = counter | plus: 1 %}
        {% if counter == 3 and forloop.last == false %}
          </tr><tr>
          {% assign counter = 0 %}
        {% endif %}
      {% endfor %}
      {% if counter != 0 %}
        {% assign empty_cols = 3 | minus: counter %}
        {% for i in (1..empty_cols) %}
          <td ><div style="width:2000px; height:150px; background:#ffffff; display:inline-block;"></div></td>
        {% endfor %}
      {% endif %}
    </tr>
  </table>
</details>
{% endfor %}
