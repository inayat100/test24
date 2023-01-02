from odoo import models , fields

class hospital(models.Model):
    _name = "hospital"

    image = fields.Binary("Image")
    hospital_name = fields.Char('Hospital Name')
    street1 = fields.Char('Street1')
    street2 = fields.Char('Street2')
    city = fields.Char('City')
    state = fields.Char('State')
    zip = fields.Integer("Zip")
    country = fields.Char('Country')