from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .maneger import *

#criando uma classe de usuário customizada para substituir a padrão com
#atributos desejados:
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    registrationNumber = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email" #substituir o login username por e-mail
    REQUIRED_FIELDS = []
    
    objects = ManagerCustomUser()

    def __str__(self):
        return self.email    


BLOCKS = [
    ('A','Bloco A'),
    ('B','Bloco B'),
    ('C','Bloco C'),
]

class Environments(models.Model):
    name = models.CharField(max_length=100)
    block = models.CharField(max_length=30, choices=BLOCKS)

    def __str__(self):
        return self.name

TASKS_TYPE = [
    ('MA','Manutenção'),
    ('ME','Melhoria'),
]

TASKS_STATUS = [
    ('AB','Aberta'),
    ('EA','Em Andamento'),
    ('CA','Cancela'),
    ('CO','Concluída'),
    ('EN','Encerrada'),
]

#enum da tabela Courses
COURSES_CATEGORY = [
    ('CAI','Aprendizagem Industrial'),
    ('FIC','Formação Continuada'),
    ('CST','Curso Superior Tecnológico'),
    ('CT','Curso Técnico'),
]

DURATION_TYPE = [
    ('H','Horas'),
    ('S','Semestres'),
]

AREA_COURSES = [
    ('TI','Tecnologia da Informação'),
    ('MEC','Mecânica'),
    ('AUT','Automação'),
    ('ELE','Elétrica'),
]

MODALITY_COURSES = [
    ('EAD', 'Ensino à Distância'),
    ('P', 'Presencial'),
    ('H', 'Híbrido'),
]


class Tasks(models.Model):
    environmentFK = models.ForeignKey(Environments, related_name='tasksEnvironments', on_delete=models.CASCADE)
    reporterFK = models.ForeignKey(CustomUser, related_name='tasksCustomUser', on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    diagnostic = models.CharField(max_length=300, null=True, blank=True)
    type = models.CharField(max_length=100,choices=TASKS_TYPE)
    status = models.CharField(max_length=100,choices=TASKS_STATUS)
    #environmentAlocationFK = models.ForeignKey(EnvironmentAlocation, related_name='tasksEnvironmentAlocation', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class TasksAssignees(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name='tasks_assignees', on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name='tasks_assignees', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.taskFK.title

    
class Equipments(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    assigneeFK = models.ForeignKey(CustomUser, related_name='equipmentsCustomUser', on_delete=models.CASCADE, 
                                   blank=True, null=True)
    
    def __str__(self):
        return self.name

class TasksStatus(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name='tasks_status', on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=TASKS_STATUS)
    creationDate = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.taskFK.title

FILE_TYPE = [
    ('D','Document'),
    ('P', 'Photo')
]

class FilesTasksStatus(models.Model):
    taskStatusFK = models.ForeignKey(TasksStatus, related_name='filesTasksStatusTask', on_delete=models.CASCADE)
    link = models.CharField(max_length=2000)
    fileType = models.CharField(max_length=300, choices=FILE_TYPE)

    def __str__(self):
        return self.fileType
    
class TasksEquipments(models.Model):
    taskFK = models.ForeignKey(Tasks, related_name='tasksEquipmentsTask', on_delete=models.CASCADE)
    equipmentFK = models.ForeignKey(Equipments, related_name='tasksEquipmentsEquipment', on_delete=models.CASCADE)   

    def __str__(self):
        return self.fileType
    
class EnvironmentsAssignees(models.Model):
    environmentFK = models.ForeignKey(Environments, related_name='environmentsAssigneesEnvironment', on_delete=models.CASCADE)
    assigneeFK = models.ForeignKey(CustomUser, related_name='environmentsAssigneesCustomUser', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.environmentFK.name

class Themes(models.Model):
    name = models.CharField(max_length=200)
    timeLoad = models.IntegerField()  # Pode ser substituído pelo valor desejado
    
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=COURSES_CATEGORY)
    duration = models.IntegerField()
    duration_type = models.CharField(max_length=200, choices=DURATION_TYPE)
    area = models.CharField(max_length=100, choices= AREA_COURSES)
    modality = models.CharField(max_length=200, choices=MODALITY_COURSES)
    themes = models.ManyToManyField(Themes)
    
    def __str__(self):
        return self.name
    
class Classes(models.Model):
    name = models.CharField(max_length=200)
    coursedFK = models.ForeignKey(Courses, related_name='classesCourses', on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    
    def __str__(self):
        return self.name
    
class DivisionClass(models.Model):
    name = models.CharField(max_length=200)
    classFK = models.ForeignKey(Classes, related_name='classesDivisionClass', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class TeacherAlocation(models.Model):
    classFK = models.ForeignKey(Classes, related_name='teacher_alocations_Class', on_delete=models.CASCADE)
    themeFK = models.ForeignKey(Themes, related_name='themesTeacherAlocation', on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    reporterFK = models.ForeignKey(CustomUser, related_name='customUserTeacherAlocation', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.themeFK.name
    
    
    
ALOCATION_STATUS = [ 
    ('1', 'Rascunho'),
    ('2', 'Assinalado'),
    ('3', 'Concluido')                
    ]
    
class TeacherAlocationDetail(models.Model):
    teacherFK = models.ForeignKey(CustomUser, related_name='customUserTeacherAlocationDetail', on_delete=models.CASCADE)
    classDivisionFK = models.ForeignKey(DivisionClass, related_name='divisionClassTeacherAlocationDetail', on_delete=models.CASCADE)
    alocationStatus = models.CharField(max_length=200, choices=ALOCATION_STATUS, default='1')
    
    def __str__(self):
        return self.classDivisionFK.name
    
    
WEEK_DAY = [ 
    ('SEG', 'Segunda-Feira'),
    ('TER', 'Terça-Feira'),
    ('QUA', 'Quarta-Feira'),
    ('QUI', 'Quinta-Feira'),
    ('SEX', 'Sexta-Feira'),
    ('SAB', 'Sábado'),
    ('DOM', 'Domingo'),                  
    ]    
    
class TeacherAlocationDetailEnv(models.Model):
    environmentFk = models.ForeignKey(Environments, related_name='environmentTeacherAlocationDetailEnv', on_delete=models.CASCADE)
    teacherAlocationDetailFK = models.ForeignKey( TeacherAlocationDetail, related_name='teacherAlocationDetailTeacherAlocationDetailEnv', on_delete=models.CASCADE)
    weedDay = models.CharField(max_length=50, choices=WEEK_DAY)
    hourStart = models.TimeField()
    hourEnd = models.TimeField()
    startDate = models.DateField()
    endDate = models.DateField()
    
    def __str__(self):
        return self.environmentFk.name

class Deadline(models.Model):
    targetDate = models.DateField()
    category = models.CharField(max_length=50, choices=COURSES_CATEGORY)
    
    
def __str__(self):
    return self.category

class Signatures(models.Model):
    ownerFK = models.ForeignKey(CustomUser, related_name='customUserSignatures', on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    signature = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.ownerFK.name
    
    

STATUS_PLAN = [ 
    ('1', 'Pendente'),
    ('2', 'Em Aprovação'),
    ('3', 'Aprovado'),
    ('4', 'Em revisão'),
    ('5', 'cancelado')
                    
    ]    


class Plan(models.Model):
    cutomUserFk = models.ForeignKey(CustomUser, related_name='customUserPlan', on_delete=models.CASCADE)
    themeFK = models.ForeignKey(Themes, related_name='themesPlan', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_PLAN)
    signatureFK = models.ForeignKey(Signatures, related_name='planSignature', on_delete=models.CASCADE, blank=True, null=True)
    approverFK = models.ForeignKey(CustomUser, related_name='planApprover', on_delete=models.CASCADE)

    def __str__(self):
        return self.teacherFK.email

class PlanStatus(models.Model):
    planFK = models.ForeignKey(Plan, related_name='planStatusPlan', on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_PLAN)
    comment = models.CharField(max_length=500)
    file = models.CharField(max_length=1000)

    def __str__(self):
        return self.planFK.teacherFK.email

    
    
