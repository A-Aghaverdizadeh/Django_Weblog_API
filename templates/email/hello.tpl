{% extends "mail_templated/base.tpl" %}

{% block subject %}
    
{% endblock %}

{% block body %}
This is a plain text part.
{% endblock %}

{% block html %}
This is an <strong>html</strong> part.
<br><hr>
Token: {{ Token }}
{% endblock %}