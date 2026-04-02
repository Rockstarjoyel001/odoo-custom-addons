from odoo import http
from odoo.http import request

class UniqueDistController(http.Controller):
    @http.route('/shop/distribution_deals', type='http', auth="public", website=True)
    def special_deals(self, **kw):
        products = request.env['product.template'].search([('sale_ok', '=', True)], limit=12)
        return request.render('unique_dist_ecommerce.special_deals_page', {
            'products': products
        })
