from django.db import models

from djangotoolbox.fields import ListField
# Create your models here.
from companyData import data


class Company(models.Model):
  prime = models.CharField()


def populateCompany():
  company = Company(
    prime='Masih'
  )
  company.save()


# from models.company import Company, populateCompany