from odoo import http
from odoo.http import request
import werkzeug.utils
import base64
import re
from odoo.addons.portal.controllers.portal import pager


class EidOfferController(http.Controller):

    def myFunc(self, e):
        return e['name']
    def myFunc1(self, e):
        return e['price']

    def convert_to_slug(self ,display_name):
        # Convert to lowercase
        slug = display_name.lower()
        
        # Replace spaces with hyphens
        slug = slug.replace(' ', '-')
        
        # Remove special characters using regex
        slug = re.sub(r'[^a-zA-Z0-9-]', '', slug)
        return slug
    @http.route('/offer/table', type='http', auth='public', website=True)
    def offer_table(self, **kw):
        offers = request.env['offer.offer'].sudo().search([])
        return http.request.render('product_offer.offer_table_page', {'offers': offers})

    @http.route('/offer/details/<int:offer_id>', type='http', auth='public', website=True , csrf=False)
    def offer_details(self, offer_id, sortby='Z-A', **kw):
        offer = request.env['offer.offer'].sudo().browse(offer_id)
        result = []
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        sorted_list = {
            'A-Z': {'label': 'A-Z', 'name': 'name', 'order': False},
            'Z-A': {'label': 'Z-A', 'name': 'name', 'order': True},
            'Price Higher to Lower': {'label': 'Price Higher to Lower', 'name': 'list_price', 'order': True},
            'Price Lower to Higher': {'label': 'Price Lower to Higher', 'name': 'list_price', 'order': False},
        }
        default_order_by = sorted_list[sortby]

        page_details = pager(url='/offer/details/<int:offer_id>', total=len(offer.product_ids.mapped('name')), url_args={'sortby': sortby})

        for product in offer.product_ids:
            name = product.with_context(lang='en_US').display_name
            image_url = base_url + '/web/image?' + 'model=product.template&id=' + str(product.name.id) + '&field=image_1920'
            result.append({
                'id' : product.name.id,
                'name' : name,
                'image_url' : image_url,
                'route' : self.convert_to_slug(name) + '-' +str(product.name.id),
                'price': product.name.list_price,
                'product_id': product.name
            })

            print('old', product)
        if default_order_by['name'] == 'name':
            result.sort(reverse=default_order_by['order'], key=self.myFunc)
        else: 
            result.sort(reverse=default_order_by['order'], key=self.myFunc1)
        
        return http.request.render('product_offer.product_offer_details_page', {
                                        'offer': result, 
                                        'offer_fields': offer.field_ids, 
                                        'product_ids': offer.product_ids.mapped('name'),
                                        'pager': page_details,
                                        'sortby': sortby,
                                        'searchbar_sortings': sorted_list
                                    }
                                )

    @http.route('/password/<int:offer_id>', type='http', auth='public', website=True , csrf=False)
    def password_checkq(self, offer_id, **kw):
        
        # Password is incorrect or offer not found, render the password check page with an error message
        return http.request.render('product_offer.password_page' , {'offer_id': offer_id})
    
    @http.route('/password/check/<int:offer_id>', type='http', auth='public', website=True , csrf=False)
    def password_check(self, offer_id, **kw):
        password = kw.get('password')
        offer = request.env['offer.offer'].sudo().browse(offer_id)
        result = []
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        print('offer.product_ids >> ' , offer.product_ids)
        for product in offer.product_ids:
            print('product>> ' , product)
            name = product.with_context(lang='en_US').display_name
            image_url = base_url + '/web/image?' + 'model=product.template&id=' + str(product.name.id) + '&field=image_1920'
            result.append({
                'id' : product.name.id,
                'name' : name,
                'image_url' : image_url,
                'route' : self.convert_to_slug(name) + '-' +str(product.name.id)
            })
        if not offer.password:
            return request.redirect('/offer/details/' + str(offer_id))
        if offer and password == offer.password:
            # Password is correct, redirect to the offer details page
            return request.redirect('/offer/details/' + str(offer_id))
        else:
            # Password is incorrect or offer not found, render the password check page with an error message
            error_message = 'Incorrect password' if offer else 'Offer not found'
            return http.request.render('product_offer.password_page', {'error_message': error_message , 'offer_id': offer_id})