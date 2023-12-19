from odoo import models,api, fields,_
class ContentAlmakaan(models.Model):
    _name = 'content.elmakan'
    _description = "this module is for content elmakan"  

    text = fields.Text(string='Text',default='')
    title = fields.Char(string='title',default='')
    link = fields.Char(string='link',default='')
    image = fields.Binary(string='Image')
    image_url = fields.Char("image url", compute='_compute_image_url')
    

    @api.depends('image')
    def _compute_image_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for obj in self:
            if obj.image:
                obj.image_url= base_url + '/web/image?' + 'model=content.elmakan&id=' + str(obj.id) + '&field=image'
            else:
                obj.image_url=''