from mongoengine import Document, EmbeddedDocument, fields# Create your models here.
from companyData import data


class Company(Document):
  prime = fields.StringField(verbose_name="prime")
  number_set = fields.DictField(verbose_name='Number set')
  bse_code = fields.StringField(verbose_name='BSE code')
  short_name = fields.StringField(verbose_name='Short name')
  nse_code = fields.StringField(verbose_name='NSE code')
  companyrating_set = fields.ListField(verbose_name='Rating')
  annualreport_set = fields.ListField(verbose_name='Annual report')
  announcement_set = fields.ListField(verbose_name='Announcement')
  warehouse_set = fields.DictField(verbose_name='Warehouse set')
  name = fields.StringField(verbose_name='name')
  id = fields.IntField(verbose_name='id', primary_key=True)

def populateCompany():
  company = Company(**data)
  company.save()


# from models.company import *