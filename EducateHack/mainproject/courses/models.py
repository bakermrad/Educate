# models.py
from django.db import models
from django.core.validators import RegexValidator
class Major(models.Model):
    name = models.CharField(max_length=255)
    requiredecredits = models.IntegerField()


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
    DAY_CHOICES = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('R', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday'),
        ('U', 'Sunday'),
    )
    day = models.CharField(max_length=1, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=10)

    
    class Meta:
        unique_together = ('name', 'day', 'start_time', 'end_time')
        ordering = ('start_time' , )

    def __str__(self):
        return self.name
    
import random
import string

from django.utils import timezone
from .models import Course, Major


def random_string(length):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_courses():
    computer_science = Major.objects.get(name='Computer Science')

    course_names = [
        'Introduction to Programming',
        'Data Structures and Algorithms',
        'Database Systems',
        'Operating Systems',
        'Computer Networks',
        'Artificial Intelligence',
        'Computer Graphics',
        'Computer Security',
        'Software Engineering',
        'Mobile App Development',
        'Web Development',
        'Distributed Systems',
        'Computer Architecture',
        'Computer Vision',
        'Machine Learning',
        'Natural Language Processing',
        'Parallel Computing',
        'Big Data Analytics',
        'Computer Ethics and Social Issues',
        'Human-Computer Interaction'
    ]

    courses = []
    for name in course_names:
        course = {
            'Major': computer_science,
            'name': name,
            'description': f'This course covers {random_string(20)}',
            'credits': random.choice([3, 4]),
            'instructor': f'{random_string(5)} {random_string(8)}',
            'day': random.choice(['M', 'T', 'W', 'R', 'F', 'S', 'U']),
            'start_time': timezone.now().replace(hour=random.randint(8, 16), minute=0, second=0),
            'end_time': timezone.now().replace(hour=random.randint(17, 22), minute=0, second=0),
            'room': f'{random_string(1).upper()}{random.randint(100, 999)}'
        }
        courses.append(course)

    for course_data in courses:
        course = Course(
            Major=course_data['Major'],
            name=course_data['name'],
            description=course_data['description'],
            credits=course_data['credits'],
            instructor=course_data['instructor'],
            day=course_data['day'],
            start_time=course_data['start_time'],
            end_time=course_data['end_time'],
            room=course_data['room']
        )
        course.save()
