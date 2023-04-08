from django.db import models
# Create your models here.


class Major(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name' , )

    def __str__(self):
        return self.name
    

class Course(models.Model):
    Major = models.ForeignKey(Major, related_name='courses' , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    credits = models.IntegerField()
    instructor = models.CharField(max_length=255)
    day = models.CharField(max_length=255)
    time = models.TimeField((""), auto_now=False, auto_now_add=False)
    room = models.CharField(max_length=10)

    def __str__(self):
        return self.name



