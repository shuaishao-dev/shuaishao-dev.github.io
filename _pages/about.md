---
permalink: /
title: "Shuai Shao"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a PhD student in Computer Science at the [University of Connecticut (UConn)](https://www.uconn.edu), advised by [Prof. Tingting Yu](https://tingting-yu.scholar.uconn.edu/).
My research interests include **concurrent programming**, **static analysis**, **software refactoring**, and **LLMs for software engineering**. 
I am particularly interested in developing **practical and explainable techniques** that bridge **software artifacts** (e.g., bug reports and source code) to understand, localize, and improve issues in large-scale systems.
---

## Selected Publications

{% assign my_name = "Shuai Shao" %}
{% assign highlighted_name = "<strong>" | append: my_name | append: "</strong>" %}
{% assign pubs = site.publications | sort: "date" | reverse %}

<ol>

{%- comment -%} Published / Accepted {%- endcomment -%}
{% assign count = 0 %}
{% for p in pubs %}
  {% if p.venue contains "arXiv" %}
    {% continue %}
  {% endif %}
  {% if count >= 10 %}
    {% break %}
  {% endif %}
  <li>
    <strong>{{ p.title }}</strong>.<br/>
    {{ p.authors | replace: my_name, highlighted_name }}.<br/>
    <em>{{ p.venue }}</em>, {{ p.year }}.
  </li>
  {% assign count = count | plus: 1 %}
{% endfor %}

{%- comment -%} Fill with arXiv if < 10 {%- endcomment -%}
{% for p in pubs %}
  {% if count >= 10 %}
    {% break %}
  {% endif %}
  {% unless p.venue contains "arXiv" %}
    {% continue %}
  {% endunless %}
  <li>
    <strong>{{ p.title }}</strong>.<br/>
    {{ p.authors | replace: my_name, highlighted_name }}.<br/>
    <em>{{ p.venue }}</em>, {{ p.year }}.
  </li>
  {% assign count = count | plus: 1 %}
{% endfor %}

</ol>

<p>
  <a href="/publications-cv/">Full publication list</a>
</p>

---

## Work Experience

- **Spring 2026**: Teaching Assistant  
  *CSE 3400 / CSE 5850 — Introduction to Cryptography and Cybersecurity*

- **Fall 2025**: Teaching Assistant  
  *CSE 3400 / CSE 5850 — Introduction to Cryptography and Cybersecurity*