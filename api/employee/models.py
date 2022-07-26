from django.db import models

class Employee(models.Model):
    TEAMLEAD = 'TEAMLEAD'
    SENIOR = 'SENIOR'
    MIDDLE = 'MIDDLE'
    JUNIOR = 'JUNIOR'
    TRAINEE = "TRAINEE"

    EMPLOYEE_TYPES = (
        (TEAMLEAD, 'team leader'),
        (SENIOR, 'senior developer'),
        (MIDDLE, 'middle developer'),
        (JUNIOR, 'junior developer'),
        (TRAINEE, 'trainee')
    )

    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    name = models.CharField(max_length=100)
    joinDate = models.DateTimeField(null=True,)
    salary = models.IntegerField(null=True,)
    manager = models.CharField(null=True,max_length=100)
    
    def __str__(self):
        return "<Employee: {} {}>".format(self.name)

    def __repr__(self):
        return self.__str__()