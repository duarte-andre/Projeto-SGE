from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    registrationNumber = models.CharField(max_length= 30)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD ="email"
    REQUIRED_FIELDS = []
    
               

# Create your models here.
BLOCKS = [
    ("A","Bloco A"),
    ("B","Bloco B"),
    ("C","Bloco C")
]


class Enviroment(models.Model):
    name = models.CharField(max_length=100)
    block = models.CharField(max_length=30, choise=BLOCKS)
    
    def __str__(self):
        return self.name
    
    
class Equipements(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=35)
    
    def __str__(self):
        return self.name
    

TASKS_TYPE = [
    ('MA', 'Manutenção'),
    ('ME', 'Melhoria')
]

TASKS_STATUS = [
    ('AB', ' Aberta'),
    ('EA', ' Em Andamento'),
    ('CA', ' Cancelada'),
    ('CO', ' Concluída'),
    ('EN', ' Encerrada'),
    
    
]



class Tasks(models.Model):
    enviromentFK = models.ForeignKey(Enviroment, related_name='tasksEnviroments', on_delete=models.CASCADE)
    reporterFk =models.ForeignKey(CustomUser, related_name='tasksCustomUser', on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    diagnostic = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=30, choices=TASKS_TYPE)
    status = models.CharField(max_length=30, choices=TASKS_STATUS)
   
    def __str__(self) :
        return self.title
        
        
class TasksAssignees(models.Model):
    assigneesFK =models.ForeignKey(CustomUser, related_name='tasksAssigneesCustomUser', on_delete=models.CASCADE)
    tasksFK = models.ForeignKey(Tasks, related_name='tasksAssigneesTask', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tasksFK.title
    

class TasksAssignees(models.Model):
    assigneesFK =models.ForeignKey(CustomUser, related_name='tasksAssigneesCustomUser', on_delete=models.CASCADE)
    tasksFK = models.ForeignKey(tasks, related_name='tasksAssigneesTask', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tasksFK.title
    
    
