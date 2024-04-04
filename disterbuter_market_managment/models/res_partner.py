from odoo import models, fields, api


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    partner_type = fields.Selection([
        ('none', 'None'),
        ('customer', 'Customer'),
        ('request_distributor', 'Pending distributor'),
        ('distributor', 'distributor'),
        ('request_super_distributor', 'Pending distributor+'),
        ('super_distributor', 'distributor+')], default="none", required=True, string="Partner Type")

    product_ids = fields.One2many('product.template', 'partner_id', string="Products")
    license_number = fields.Char(string="License Number")
    commercial_license = fields.Binary(string="Commercial License")
    authentication_of_signature = fields.Binary(string="Authentication of Signature")
    sponsor_license = fields.Binary(string="Sponsor's License")

    def action_make_distributor(self):
        for rec in self:
            rec.partner_type = 'distributor'
            template = self.env.ref('bbook_distributor_market_management.mail_template_partner_distributor')
            template.send_mail(rec.id)

            activity_id = self.env['mail.activity'].sudo().search([
                ('activity_type_id', '=', 4),
                ('user_id', '=', self.env.user.id),
                ('res_model_id', '=',
                 self.env['ir.model'].sudo().search([('model', '=', 'res.partner')], limit=1).id),
                ('res_id', '=', self.id)
            ])
            if activity_id:
                activity_id.action_done()

    def action_make_super_distributor(self):
        for rec in self:
            rec.partner_type = 'request_super_distributor'
            template = self.env.ref('bbook_distributor_market_management.mail_template_partner_super_distributor')
            template.send_mail(rec.id)

            activity_id = self.env['mail.activity'].sudo().search([
                ('activity_type_id', '=', 4),
                ('user_id', '=', self.env.user.id),
                ('res_model_id', '=',
                 self.env['ir.model'].sudo().search([('model', '=', 'res.partner')], limit=1).id),
                ('res_id', '=', self.id)
            ])
            if activity_id:
                activity_id.action_done()
