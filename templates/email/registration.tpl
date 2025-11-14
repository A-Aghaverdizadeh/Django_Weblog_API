{% extends "mail_templated/base.tpl" %}

{% block subject %}
    
{% endblock %}

{% block body %}
This is a plain text part.
{% endblock %}

{% block html %}
http://localhost:8000/accounts/api/v1/activate-user/{{ Token }}
{% endblock %}