from django.db import models

class Internship(models.Model):
    STATUS_CHOICES = [
        ('Applied','Applied'),
        ('Under Review', 'Under Review'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    application_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )
    stipend = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    def _str_(self):
        return self.company + "-" + self.position
