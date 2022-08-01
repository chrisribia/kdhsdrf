from django.db import models
from classManagement.models import ClassList,ClassMembersDetails

class SubjectList(models.Model):
    SubjectName = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.SubjectName

class SubjectSelectionList(models.Model):
    Subject = models.ForeignKey(SubjectList,on_delete=models.CASCADE)
    StudentClass = models.ForeignKey(ClassList,on_delete=models.CASCADE)
    StudentRegNumber = models.ForeignKey(ClassMembersDetails,on_delete=models.CASCADE)
    def __str__(self):
        return self.StudentRegNumber