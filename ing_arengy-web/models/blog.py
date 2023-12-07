from odoo import fields, models


class BlogPost(models.Model):
    _inherit = "blog.post"



    fecha_custom = fields.Char(string="fecha")
    imagen_url       = fields.Char(string="IMAGEN")


