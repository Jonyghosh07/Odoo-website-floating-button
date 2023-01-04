from odoo import fields, models


class red_website(models.Model):
    _inherit = 'website'

    r_link = fields.Char(string='Redirect Link', compute="get_red_link")
    # r_text = fields.Char(string='Popup Text', compute="get_red_text")
    r_icon = fields.Char(string='Popup Icon', compute="get_red_icon")


    def get_red_link(self):
        gl=self.env['custom.website'].search([('name','=',self.name)], order='create_date desc', limit=1)
        self.r_link=gl.red_link

    # def get_red_text(self):
    #     gl=self.env['custom.website'].search([('name','=',self.name)], order='create_date desc', limit=1)
    #     self.r_text=gl.red_text

    def get_red_icon(self):
        gl=self.env['custom.website'].search([('name','=',self.name)], order='create_date desc', limit=1)
        self.r_icon=gl.red_icon

class custom_website(models.Model):
    _name='custom.website'
    _description='custom website'

    name=fields.Many2one('website', string='Select Website')
    red_link = fields.Char(string="Enter a link")    
    # red_text= fields.Char(string="Enter a text")
    red_icon= fields.Binary(string="Upload an icon")
