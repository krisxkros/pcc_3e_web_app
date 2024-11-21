from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    # 'ForeignKey: connect each entry with a particular topic
    # 'on_delete=models.CASCADE': when a topic is deleted, all the entries
    # associated with that topic should be deleted as well.
    # This is known as a 'cascading delete'.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text) >= 50:
            return f"{self.text[:50]}..."
        return self.text
