from odoo import models,api, fields,_

class BoxesAlmakaan(models.Model):
    _name = 'boxes.elmakan'
    _description = "this module is for boxes.elmakan"


    text =fields.Text(string='text')
    title =fields.Char(string='title')