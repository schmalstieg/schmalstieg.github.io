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

<h1>Current research areas</h1>

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
