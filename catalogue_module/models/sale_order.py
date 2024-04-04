from odoo import models, api, fields, _
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _name = 'sale.catalogue'
    _rec_name = 'name'

    name = fields.Char(string="name")
    image_ids = fields.One2many('sale.catalogue.line', 'catalogue_id', string="Images")
    image_ids2 = fields.One2many('sale.catalogue.line2', 'catalogue_id', string="Images")
    product_ids = fields.Many2many('product.template', string="Products")


class SaleOrderLineInherit(models.Model):
    _name = 'sale.catalogue.line'
    catalogue_id = fields.Many2one('sale.catalogue')
    image = fields.Binary('Image')


class SaleOrderLine_Inherit(models.Model):
    _name = 'sale.catalogue.line2'
    catalogue_id = fields.Many2one('sale.catalogue')
    image = fields.Binary('Image')
