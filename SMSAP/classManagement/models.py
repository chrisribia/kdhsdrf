from django.db import models
 

class ClassList(models.Model):
    ClassNames = models.CharField(max_length=255,unique=True)
    Teacher = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.ClassNames
     
class ClassMembersDetails(models.Model):
    ClassLevelName = models.ForeignKey(ClassList, on_delete=models.CASCADE)
    StudentReg = models.CharField(max_length=255,default=None)

    def __str__(self):
        return self.StudentReg
