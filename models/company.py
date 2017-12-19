from django.db import models

from djangotoolbox.fields import ListField
# Create your models here.
from companyData import data



class Company(models.Model):
  prime = models.CharField()


def populateCompany():
  company = Company.objects.create(
    prime='Masih'
  )


# from models.company import Company, populateCompany