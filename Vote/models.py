from django.db import models
from Users.models import NewUser




class Course(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class ProfessorStatic(models.Model):
    name = models.CharField(max_length=50, default="")
    behavior = models.IntegerField(default=0)
    course = models.ManyToManyField(Course)


    def __str__(self):
        return self.name

class Professor(ProfessorStatic):
    respect = models.IntegerField(default=0)
    teach = models.IntegerField(default=0)


class Poll(models.Model):
    student = models.ForeignKey(
        NewUser,
        on_delete=models.CASCADE,
        default="")

    professor = models.ForeignKey(
        to=Professor, 
        on_delete=models.CASCADE,
        related_name="vote")
    
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE,
        default="")
    
    respect = models.IntegerField(default=0)
    teach = models.IntegerField(default=0)
    behavior = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.professor.respect += self.respect
        self.professor.teach += self.teach
        self.professor.behavior += self.behavior
        self.professor.save()
        super(Poll, self).save(*args, **kwargs)