

from odoo import models,api, fields,_
import os 
import base64

class AboutAlmakaan(models.Model):
    _name = 'about.elmakan'
    _description = "this module is for about elmakan"
    _rec_name ='text'
    text=fields.Text(string='Text',default='')
    video_url= fields.Char(string='video url',default='')
    content_ids = fields.Many2many('content.elmakan' , string= 'Content')
    hero_ids = fields.Many2many('hero.section.elmakan' , string= 'Heros')
    gallery_ids = fields.Many2many('gallery.elmakan' , string= 'Gallery')
    state = fields.Boolean(string='On WebSite',default=False)


