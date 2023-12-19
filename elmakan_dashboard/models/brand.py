from odoo import models,api, fields,_



class BrandAlmakaan(models.Model):
    _name = 'brand.elmakan'
    _description = "this module is for brand"
    _rec_name ='slug'
    slug = fields.Char(string='Slug',default='',compute='_compute_slug')
    image = fields.Binary('Image')
    title = fields.Text('Title')
    description_ids = fields.Many2many('description.elmakan' , string='Description')
    content_ids = fields.Many2many('content.elmakan' ,string='Content')
    gallery_ids = fields.Many2many('gallery.elmakan' , string='Gallery')
    image_url = fields.Char("image url", compute='_compute_image_url')
    
    isTopBrand = fields.Boolean(string='isTopBrand',default=False)
    state = fields.Boolean(string='On WebSite',default=False)

    @api.depends('title')
    def _compute_slug(self):
        for record in self:
            if record.title:
                record.slug = record.title.lower().replace(' ','-') +f'-{record.id}'
            else:
                record.slug='' 

    @api.depends('image')
    def _compute_image_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        print('base_url' , base_url)
        for obj in self:
            if obj.image:
                obj.image_url= base_url + '/web/image?' + 'model=brand.elmakan&id=' + str(obj.id) + '&field=image'
            else:
                obj.image_url=''


class BrandSliderAlmakaan(models.Model):
    _name = 'brand.slider.elmakan'
    _description = "this module is for brand slider elmakan"
    _rec_name ='title'
    text = fields.Text(string='Text',default='')
    title = fields.Text(string='Title',default='')
    image = fields.Binary('Image')
    image_url = fields.Char("image url", compute='_compute_image_url')
    state = fields.Boolean(string='On WebSite',default=False)

    @api.depends('image')
    def _compute_image_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for obj in self:
            if obj.image:
                obj.image_url= base_url + '/web/image?' + 'model=brand.slider.elmakan&id=' + str(obj.id) + '&field=image'
            else:
                obj.image_url=''


