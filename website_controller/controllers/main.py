from odoo.http import request
from odoo import http

class WebsiteShopAjaxCart(http.Controller):

    @http.route(['/form'],type='http', auth='public', website=True, sitemap=False)
    def res_data(self,**post):
        print("\n\n post----------------",post)
        res_country = request.env["res.country"].search([])
        return request.render('website_controller.form_template',{'data':res_country})

    @http.route(['/form/submit'],type='http',auth='public', website=True, sitemap=False, csrf=False)
    def submit_data(self,**post):
        if post:
            post.pop("csrf_token")
            request.env["res.partner"].sudo().create(post)
        return request.redirect('/thank-you')

    @http.route(['/thank-you'],type='http',auth='public', website=True, sitemap=False)
    def redirect_acknowledge(self,**post):
        return request.render('website_controller.thank_you')

    # @http.route(['/add/ajax/cart/products'], type='json', auth="public", website=True, csrf=False)
    # def ajax_cart(self, **kw):
    #     order = request.website.sale_get_order()
    #     values = {'website_sale_order': order, 'date': date.today()}
    #     return request.env['ir.ui.view']._render_template('ajax_cart.ajax_cart_lines_grid', values=values)