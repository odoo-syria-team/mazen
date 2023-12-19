from odoo import models,api, fields,_

class GalleryAlmakaan(models.Model):
    _name = 'gallery.elmakan'
    _description = "this module is for gallery elmakan"


    text=fields.Text(string='Text')
    image = fields.Binary(string='Image')
    image_url = fields.Char("image url", compute='_compute_image_url')

    @api.depends('image')
    def _compute_image_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        print('base_url' , base_url)
        for obj in self:
            if obj.image:
                obj.image_url= base_url + '/web/image?' + 'model=gallery.elmakan&id=' + str(obj.id) + '&field=image'
            else:
                obj.image_url=''