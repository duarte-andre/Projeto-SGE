from django.contrib import admin
from .models import *

class adminCustomUser(admin.ModelAdmin):
    list_display = ('id', 'email', 'registrationNumber', 'is_active')
    list_display_links = ('id', 'email', 'registrationNumber', 'is_active',)
    search_fields = ('email', 'registrationNumber',)
    list_per_page = 10

admin.site.register(CustomUser, adminCustomUser)

class adminEnvironments(admin.ModelAdmin):
    list_display = ('id', 'name', 'block')
    list_display_links = ('id', 'name', 'block',)
    search_fields = ('name', 'block',)
    list_per_page = 10

admin.site.register(Environments, adminEnvironments)

class adminTasks(admin.ModelAdmin):
    list_display = ('id', 'title', 'environmentFK')
    list_display_links = ('id', 'title', 'environmentFK',)
    search_fields = ('title', 'environmentFK',)
    list_per_page = 10

admin.site.register(Tasks, adminTasks)

class adminTasksAssignees(admin.ModelAdmin):
    list_display = ('id', 'taskFK', 'assigneeFK')
    list_display_links = ('id', 'taskFK', 'assigneeFK',)
    search_fields = ('taskFK', 'assigneeFK',)
    list_per_page = 10

admin.site.register(TasksAssignees, adminTasksAssignees)


class adminEquipments(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'assigneeFK')
    list_display_links = ('id', 'name', 'code', 'assigneeFK',)
    search_fields = ('name', 'code', 'assigneeFK',)
    list_per_page = 10

admin.site.register(Equipments, adminEquipments)


class adminTasksStatus(admin.ModelAdmin):
    list_display = ('id', 'taskFK', 'status', 'creationDate', 'comment')
    list_display_links = ('id', 'taskFK', 'status', 'creationDate',)
    search_fields = ('status', 'creationDate',)
    list_per_page = 10

admin.site.register(TasksStatus, adminTasksStatus)


class adminFilesTasksStatus(admin.ModelAdmin):
    list_display = ('id', 'taskStatusFK', 'link', 'fileType',)
    list_display_links = ('id', 'taskStatusFK', 'link', 'fileType',)
    search_fields = ('taskStatusFK', 'link',)
    list_per_page = 10

admin.site.register(FilesTasksStatus, adminFilesTasksStatus)


class adminTasksEquipments(admin.ModelAdmin):
    list_display = ('id', 'taskFK', 'equipmentFK')
    list_display_links = ('id', 'taskFK', 'equipmentFK',)
    search_fields = ('taskFK', 'equipmentFK',)
    list_per_page = 10

admin.site.register(TasksEquipments, adminTasksEquipments)

class adminThemes(admin.ModelAdmin):
    list_display = ('id', 'name', 'timeLoad')
    list_display_links = ('id', 'name', 'timeLoad',)
    search_fields = ('name', 'timeLoad',)
    list_per_page = 10

admin.site.register(Themes, adminThemes)


class adminCourses(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'duration', 'area', 'modality')
    list_display_links = ('id', 'name', 'category', 'duration', 'area', 'modality',)
    search_fields = ('name', 'category', 'area', 'modality',)
    list_per_page = 10

admin.site.register(Courses, adminCourses)


class adminClasses(admin.ModelAdmin):
    list_display = ('id', 'name', 'courseFK', 'startDate', 'endDate')
    list_display_links = ('id', 'name', 'courseFK', 'startDate', 'endDate',)
    search_fields = ('name', 'courseFK',)
    list_per_page = 10

admin.site.register(Classes, adminClasses)


class adminClassesDivision(admin.ModelAdmin):
    list_display = ('id', 'name', 'classFK')
    list_display_links = ('id', 'name', 'classFK',)
    search_fields = ('name', 'classFK',)
    list_per_page = 10

admin.site.register(DivisionClass, adminClassesDivision)

class adminTeacherAlocation(admin.ModelAdmin):
    list_display = ('id', 'classFK', 'themeFK', 'createdDate', 'updatedDate', 'reporterFK')
    list_display_links = ('id', 'classFK', 'themeFK', 'createdDate', 'updatedDate', 'reporterFK',)
    search_fields = ('classFK', 'themeFK',)
    list_per_page = 10

admin.site.register(TeacherAlocation, adminTeacherAlocation)


class adminTeacherAlocationDetailEnv(admin.ModelAdmin):
    list_display = ('id', 'teacherAlocationDetailFK', 'environmentFK', 'weekDay', 'hourStart', 'hourEnd', 'startDate', 'endDate')
    list_display_links = ('id', 'teacherAlocationDetailFK', 'environmentFK', 'weekDay', 'hourStart', 'hourEnd', 'startDate', 'endDate',)
    search_fields = ('teacherAlocationDetailFK', 'environmentFK',)
    list_per_page = 10

admin.site.register(TeacherAlocationDetailEnv, adminTeacherAlocationDetailEnv)


class adminDeadline(admin.ModelAdmin):
    list_display = ('id', 'targetDate', 'category')
    list_display_links = ('id', 'targetDate', 'category',)
    search_fields = ('category',)
    list_per_page = 10

admin.site.register(Deadline, adminDeadline)


class adminSignatures(admin.ModelAdmin):
    list_display = ('id', 'ownerFK', 'createdDate', 'signature')
    list_display_links = ('id', 'ownerFK', 'createdDate', 'signature',)
    search_fields = ('ownerFK',)
    list_per_page = 10

admin.site.register(Signatures, adminSignatures)



class adminPlan(admin.ModelAdmin):
    list_display = ('id', 'cutomUserFk', 'themeFK', 'status','signatureFK','approverFK')
    list_display_links = ('id', 'cutomUserFk', 'themeFK', 'status','signatureFK','approverFK')
    search_fields = ('cutomUserFk', 'themeFK', 'signatureFK', 'approverFK', )
    list_per_page = 10

admin.site.register(Plan, adminPlan)


class adminPlanStatus(admin.ModelAdmin):
    list_display = ('id', 'planFK', 'createdDate', 'status','comment','file')
    list_display_links = ('id', 'planFK', 'createdDate', 'status','comment','file')
    search_fields = ('planFK',)
    list_per_page = 10

admin.site.register(PlanStatus, adminPlanStatus)
    
    