"""Defines URL patterns for learning logs."""

from django.urls import path
# the dot (.) tells Python to import the views.py module from the same directory
# as the current urls.py module
from . import views

# `app_name`` helps Django distinguish this urls.py file from files of
# the same name in other apps within the project
app_name = "learning_logs"
# `urlpatterns` in this module is a list of individual pages that can be
# requested from the `learning_logs` app
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # All topics page
    path("topics/", views.topics, name="topics"),
    # Single topic page
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # Page for adding new topic.
    path("new_topic/", views.new_topic, name="new_topic"),
    # Page for adding new entry.
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    # Page for editing an entry.
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]
