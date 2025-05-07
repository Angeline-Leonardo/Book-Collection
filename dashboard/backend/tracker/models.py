from django.db import models

class LearningItem(models.Model):
    TYPE_CHOICES = [('book', 'Book'), ('course', 'Course'), ('article', 'Article')]
    STATUS_CHOICES = [('to_learn', 'To Learn'), ('in_progress', 'In Progress'), ('done', 'Completed')]

    title = models.CharField(max_length=255)
    item_type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    notes = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
