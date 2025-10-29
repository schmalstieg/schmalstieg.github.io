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

<h1>Research Areas</h1>

{% for subgroup in site.data.areas %}
  <table style="width: 650px;">
    <tr><td colspan="4"><b>{{ subgroup.heading }}</b> --- {{ subgroup.description }}</td></tr>
    <tr>
      {% assign counter = 0 %}
      {% for item in subgroup.papers %}
        <td ><img src="/img/Schmalstieg_{{ item }}.jpg" width=150></td>
        {% assign counter = counter | plus: 1 %}
        {% if counter == 4 and forloop.last == false %}
          </tr><tr>
          {% assign counter = 0 %}
        {% endif %}
      {% endfor %}
      {% if counter != 0 %}
        {% assign empty_cols = 4 | minus: counter %}
        {% for i in (1..empty_cols) %}
          <td ><div style="width:150px; height:110px; background:#ffffff; display:inline-block;"></div></td>
        {% endfor %}
      {% endif %}
    </tr>
  </table>
{% endfor %}

