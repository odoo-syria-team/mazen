from odoo import models, fields , api


class Offer(models.Model):
    _name = 'offer.offer'
    _description = 'Offer'

    name = fields.Char(string='Offer Name', required=True)
    password = fields.Char(string='Password')
    url = fields.Char(string="Offer URL",readonly=True)
    field_ids = fields.Many2many('ir.model.fields', string='Offer Products Fields', domain="[('model_id.model', '=', 'product.template'), ('ttype', '!=', 'binary')]")

    temp_product_ids = fields.Many2many('product.template', string='Products')
    product_ids = fields.One2many('offer.product', 'offer_id', string='Products')

    def write(self, values):
        value = super(Offer, self).write(values)
        if 'temp_product_ids' in values:
            lines = self.env['offer.product'].search([('offer_id', '=', self.id)])
            if lines:
                lines.unlink()
            for product in values.get('temp_product_ids')[0][2]:                
                self.env['offer.product'].create({'name': product, 'offer_id': self.id})
                

        return value

    @api.constrains('create_uid')
    def get_url_cod(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        self.url = base_url + '/password/' + str(self.id)
         
class OfferProduct(models.Model):
    _name = 'offer.product'
    _description = 'Offer Product'

    name = fields.Many2one('product.template',string='Product Name', required=True)
    offer_id = fields.Many2one('offer.offer', string='Offer')