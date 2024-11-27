# Django template Language Syntax

[Documentation](https://docs.djangoproject.com/en/5.1/ref/templates/)

- [Templates topic guide](https://docs.djangoproject.com/en/5.1/topics/templates/)

## Variables

A variable outputs a value from the context, which is a *dict-like object mapping keys to values*.

>`{{ abc }}`

```django
My first name is {{ first_name }}. My last name is {{ last_name }}.
```

```json
{'first_name': 'John', 'last_name': 'Doe'}
```

Dictionary lookup, attribute lookup and list-index lookups are implemented with a dot notation:

```django
{{ my_dict.key }}
{{ my_object.attribute }}
{{ my_list.0 }}
```

## Tags

[Reference of built-in tags](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#ref-templates-builtins-tags)

Tags provide arbitrary logic in the rendering process.

>`{% abc %}`

```django
{% csrf_token %}

# Most tags accept arguments:
{% cycle 'odd' 'even' %}

# Some tags (for, if) require beginning and ending tags:
{% for topic in topics %}
    <li><a href="{% url 'learning_logs:topic' topic.id %}">{{ topic.text }}</a></li>
{% empty %}
<li>No topics have been added yet.</li>
{% endfor %}
```

A tag can:

- output content
- serve as a control structure e.g. an `“if" statement` or a `“for” loop`
- grab content from a database
- enable access to other template tags

## Filters

[Reference of built-in filters](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#ref-templates-builtins-filters)

Filters transform the values of variables and tag arguments.

>`{{ django|title }}`

```django
# Some filters take an argument:
{{ entry.date_added|date:"d.M.Y, H:i" }}
```

## Comments

>`{# this won't be rendered #}`

A `{% comment %}` tag provides multi-line comments.
