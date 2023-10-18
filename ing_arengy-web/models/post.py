# -*- coding: utf-8 -*-
from odoo import fields, models, api
import random
from odoo.exceptions import UserError, ValidationError

class Post(models.Model):
    _name = 'ing.post'


    name         = fields.Char(string='Titulo', requred=True , tracking=True)
    inner_image  = fields.Image(string='Imagen interna ', tracking=True, required=True)
    image        = fields.Image(string='Imagen en cuadricula', tracking=True, required=True)
    desc         = fields.Html(string=u'Descripción', tracking=True, required=True)

    moneda = fields.Selection([
        ('ars', 'ARS'),
        ('usd', 'USD'),

    ], string="Moneda")


    categoria_ids = fields.Many2one('ing.categoria', string="Categoria")



