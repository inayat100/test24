from odoo import models , fields

class patient(models.Model):
    _name = "patient"

    image = fields.Binary("Image")
    patient_name = fields.Char('Patient Name')
    diseases = fields.Char('Diseases')
    symptoms = fields.Char('Symptoms')
    street1 = fields.Char('Street1')
    street2 = fields.Char('Street2 ')
    city = fields.Char('City ')
    state = fields.Char('State')
    zip = fields.Integer("Zip")
    country = fields.Char('Country')
   