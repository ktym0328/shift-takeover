from django.db import models

# Create your models here.
class Tickets(models.Model):
    subject_text = models.TextField()
    create_date = models.DateTimeField('date create')
    update_date = models.DateTimeField('date update')
    detail_text = models.TextField()
    record_text = models.TextField()
    ticket_type = models.CharField(max_length=100)
    ticket_id = models.AutoField(primary_key=True)
