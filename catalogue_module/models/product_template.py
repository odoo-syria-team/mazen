from odoo import models, api, fields, _
from odoo.exceptions import ValidationError


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    sku = fields.Char(string="SKU")
    brand_id1 = fields.Many2one('brand.elmakan', string="Brand")
    origin = fields.Many2one('res.country', string="Origin")
    color_ids = fields.Many2many('product.color', string="Color")
    basic_color_ids = fields.Many2many('product.basic.color', string="Basic Color")
    size = fields.Char('Size')
    capacity = fields.Char('Capacity')
    material_ids = fields.Many2many('product.material', string="Material")
    collection_ids = fields.Many2many('product.collection', string="Collection")
    technology_ids = fields.Many2many('product.technology', string="Technology")
    piece_ids = fields.Many2many('product.piece', string="Piece")
    upc = fields.Integer('UPC')
    test_report = fields.Boolean("Test Report")
    validity = fields.Datetime('Validity')
    feature_ids = fields.Many2many('feature.elmakan', string="Feature")
    use_care = fields.Html('Use & Care')
    packing_type = fields.Many2many('product.packing.type', string="Packing Type")
    carton_barcode = fields.Integer('Carton Barcode')
    item_number = fields.Char('Item No.')
    hs_code_1 = fields.Integer('HS Code 1')
    hs_code_1_name = fields.Char('HS Code 1 Name')
    hs_code_2 = fields.Integer('HS Code 2')
    hs_code_2_name = fields.Char('HS Code 2 Name')
    seo_title = fields.Char('SEO Title')
    seo_description = fields.Html('SEO Description')
    meta_description = fields.Html('meta Description')
    e_com_description = fields.Html('E-Com Description')
    description = fields.Html('Description')
    ar_name = fields.Char(string="Arabic Name")
    ar_description = fields.Char(string="Arabic Description")
    cbm = fields.Float(string="CBM")
    weight = fields.Float(string="Product Weight (Kg)")
    packed_weight = fields.Float(string="Packed Product Weight (Kg)")
    c_g_weight = fields.Float(string="Carton Gross Weight (kg)")
    c_n_weight = fields.Float(string="Carton Net Weight (kg)")
    c_height = fields.Float(string="Carton Height (cm)")
    c_length = fields.Float(string="Carton Length (cm)")
    c_width = fields.Float(string="Carton Width (cm)")
    v_weight = fields.Float(string="Volumetric Weight (kg)")
    width = fields.Float(string="Product Width (cm)")
    length = fields.Float(string="Product Length (cm)")
    height = fields.Float(string="Product Height (cm)")
    thickness = fields.Float(string="Product Thickness (cm)")
    pieces_per_set = fields.Float(string="Pieces Per Set")
    set_includes = fields.Char(string="Set Includes")
    family = fields.Many2many('product.family', string="Product Family")
    shopify_handle = fields.Char(string="Shopify Handle")
    amazon_sku = fields.Char(string="Amazon SKU")
    asin = fields.Char(string="ASIN")
    noon_PSKU_code = fields.Char(string="Noon PSKU Code")
    noon_X_SKU_child = fields.Char(string="Noon X SKU Child")
    dubaiStore_Sku = fields.Char(string="DubaiStore Sku")
    dubaiStore_parent = fields.Char(string="Dubai Store Parent Id")
    carrefour_SKU = fields.Char(string="Carrefour SKU")
    homecenter_SKU = fields.Char(string="Homecenter SKU")
    storeus_SKU = fields.Char(string="Storeus SKU")

    

    _sql_constraints = [
        ('sku_uniq', 'unique (sku)', "SKU must be Unique"),
        ('carton_barcode_uniq', 'unique (carton_barcode)', "Carton Barcode must be Unique")
    ]

class Color(models.Model):
    _name = 'product.color'
    name = fields.Char(string='Name')

class BasicColor(models.Model):
    _name = 'product.basic.color'
    name = fields.Char(string='Name')


class Material(models.Model):
    _name = 'product.material'
    name = fields.Char(string='Name')


class Collection(models.Model):
    _name = 'product.collection'
    name = fields.Char(string='Name')


class Technology(models.Model):
    _name = 'product.technology'
    name = fields.Char(string='Name')


class Pieces(models.Model):
    _name = 'product.piece'
    name = fields.Char(string='Name')


class Features(models.Model):
    _name = 'product.feature'
    name = fields.Char(string='Name')


# class BrandAlmakaan(models.Model):
#     _inherit = 'brand.elmakan'

#     title = fields.Text('Title', translate=True)


class Family(models.Model):
    _name = 'product.family'
    name = fields.Char(string='Name')


class PackingType(models.Model):
    _name = 'product.packing.type'
    name = fields.Char(string='Name')