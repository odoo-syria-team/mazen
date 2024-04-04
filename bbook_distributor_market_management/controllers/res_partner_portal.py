from odoo import http, _
from odoo.http import request
from datetime import datetime
import base64
from odoo.exceptions import UserError, AccessDenied


class WebsiteNotificationController(http.Controller):

    @http.route('/my/request/distributor/form', type='http', auth="user", website=True, methods=['GET', 'POST'], csrf=False)
    def request_distributor(self):
        try:
            if request.env.user.partner_id.partner_type in ['distributor', 'super_distributor']:
                raise AccessDenied()
        except UserError as e:
            return str(e)
        except Exception as e:
            return str(e)

        if request.httprequest.method == 'POST':
            try:
                if request.env.user.partner_id.partner_type not in ['request_distributor', 'request_super_distributor']:
                    rec_id = request.env['ir.model'].sudo().search([('model', '=', 'res.partner')], limit=1)
                    user_id = request.env['res.users'].sudo().search(
                        [('partner_id', '=', request.env.ref('base.partner_admin').id)])

                    request.env.user.partner_id.sudo().write(self._write_vals())
                    if request.env.user.partner_id.partner_type == 'request_distributor':
                        summary = _('Partner distributor Subscription Request')
                        note = _('Upgrade partner to distributor subscription')
                    else:
                        summary = _('Partner distributor+ Subscription Request')
                        note = _('Upgrade partner to distributor+ subscription')

                    request.env['mail.activity'].sudo().create({
                        'activity_type_id': 4,
                        'summary': summary,
                        'user_id': user_id.id,
                        'res_model_id': rec_id.id,
                        'res_id': request.env.user.partner_id.id,
                        'date_deadline': datetime.today(),
                        'note': note,
                    })

                return request.redirect('/my/home')

            except UserError as e:
                return str(e)
            except Exception as e:
                return str(e)

        else:
            try:
                if request.env.user.partner_id.partner_type in ['request_distributor', 'request_super_distributor']:
                    rec_id = request.env['ir.model'].sudo().search([('model', '=', 'res.partner')], limit=1)
                    user_id = request.env['res.users'].sudo().search(
                        [('partner_id', '=', request.env.ref('base.partner_admin').id)])
                    notification_ids = request.env['mail.activity'].sudo().search([
                        ('activity_type_id', '=', 4),
                        ('user_id', '=', user_id.id),
                        ('res_model_id', '=', rec_id.id),
                        ('res_id', '=', request.env.user.partner_id.id)
                    ])
                    notification_ids.sudo().unlink()
                    request.env.user.partner_id.sudo().write({'partner_type': 'none'})
                    return request.redirect('/my/home')

                elif request.env.user.partner_id.partner_type not in ['super_distributor', 'distributor', 'request_distributor']:
                    return request.render('bbook_distributor_market_management.distributors_request_form',
                                          {
                                              'country_ids': http.request.env['res.country'].sudo().search([])
                                          })

                else:
                    return request.redirect('/my/home')

            except UserError as e:
                return str(e)
            except Exception as e:
                return str(e)

    def _write_vals(self):

        form_dict = {}
        form_file_dict = {}
        partner_vals = {}

        form = request.httprequest.form
        for key, value in zip(form.keys(), form.values()):
            form_dict[key] = form.getlist(key)

        form_files = request.httprequest.files
        for key, value in zip(form_files.keys(), form_files.values()):
            form_file_dict[key] = form_files.getlist(key)

        for key, value in zip(form_file_dict.keys(), form_file_dict.values()):
            if key in ['commercial_license', 'authentication_of_signature', 'sponsor_license']:
                partner_vals[key] = base64.b64encode(value[0].read())

        partner_vals['partner_type'] = 'request_distributor'

        for key, value in zip(form_dict.keys(), form_dict.values()):
            if key == 'country_id':
                partner_vals[key] = request.env['res.country'].sudo().search(
                    [('id', '=', int(value[0]))]) if value else None

            # if key == 'company_name':
            #     partner_vals[key] = request.env['res.company'].sudo().create({'name', value[0]})

            if key == 'partner_type':
                partner_vals[key] = 'request_super_distributor'

            if key in ['name', 'phone', 'email', 'license_number', 'city', 'street']:
                partner_vals[key] = value[0]
        print('partner_vals', partner_vals)
        return partner_vals
