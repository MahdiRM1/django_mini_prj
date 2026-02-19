from django.db import models
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    
    PRIORITY_TYPE = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_TYPE)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks')

    def __str__(self):
        return self.title