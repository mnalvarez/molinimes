from django.db import models

# Create your models here.

class Status:
    PENDING = 0
    PASSED = 1
    ONGOING = 2
    ONGOING_WITH_FAILURES = 3
    FAILED = 4

class TestCase(models.Model):
    status = models.IntegerField(default=Status.PENDING)
    status_last_modification_date = models.DateTimeField()
    
class TestCaseStep(models.Model):
    status = models.IntegerField(default=Status.PENDING)
    status_last_modification_date = models.DateTimeField()
    test_case = models.ForeignKey('TestCase')

class TestCaseStatusChangeLog(models.Model):
    modification_date = models.DateTimeField()
    new_status = models.IntegerField()
    test_case = models.ForeignKey('TestCase')
    
class TestCaseStepStatusChangeLog(models.Model):
    modification_date = models.DateTimeField()
    new_status = models.IntegerField()
    test_case = models.ForeignKey('TestCaseStep')
