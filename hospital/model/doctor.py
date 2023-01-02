from odoo import models , fields

class hospital(models.Model):
    _name = "doctor"

    image = fields.Binary("Image")
    doctor_name = fields.Char('Doctor Name')
    street1 = fields.Char('Street1 ')
    street2 = fields.Char('Street2 ')
    city = fields.Char('City ')
    state = fields.Char('State')
    zip = fields.Integer("Zip")
    country = fields.Char('Country')
    # leave_day = fields.One2many("patient","leaves","Leave Day")
    # booking_date = fields.Date("Date For Leave")
