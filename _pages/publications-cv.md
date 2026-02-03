---
title: "Publications"
permalink: /publications-cv/
author_profile: true
---

{% assign my_name = "Shuai Shao" %}
{% assign highlighted_name = "<strong>" | append: my_name | append: "</strong>" %}
{% assign pubs = site.publications | sort: "date" | reverse %}

<ol>
{% for p in pubs %}
  <li>
    <strong>{{ p.title }}</strong>.<br/>
    {{ p.authors | replace: my_name, highlighted_name }}.
    {% if p.venue %}<em>{{ p.venue }}</em>,{% endif %}
    {{ p.year }}.
  </li>
{% endfor %}
</ol>