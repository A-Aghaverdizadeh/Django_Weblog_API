{% extends "mail_templated/base.tpl" %}

{% block subject %}
    Reset Your Password
{% endblock %}

{% block body %}
    This is a plain text part.
{% endblock %}

{% block html %}
http://localhost:8000/accounts/api/v1/password-reset/confirm/{{ reset_url_token }}
{% endblock %}