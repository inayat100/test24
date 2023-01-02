from odoo import models ,fields,api

class SelectStudent(models.Model):
    _name = "selectstudent"
    
    image = fields.Binary("Image")
    name = fields.Char("First Name")
    last_name = fields.Char("Last Name")
    age = fields.Char(string="age")
    gender = fields.Char(string="Gender")
    email = fields.Char(string="E-mail")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country = fields.Char("Country")
