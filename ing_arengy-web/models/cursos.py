# -*- coding: utf-8 -*-
from odoo import fields, models, api
import random
from odoo.exceptions import UserError, ValidationError


class Curso(models.Model):
    _name = 'ing.curso'

    name = fields.Char(string='Titulo', requred=True, tracking=True)
    inner_image  = fields.Image(string='Imagen interna ', tracking=True, required=True)
    image        = fields.Image(string='Imagen en cuadricula', tracking=True, required=True)
    desc         = fields.Html(string=u'Descripción', tracking=True, required=True)

    texto_corto = fields.Char(string="Texto corto", required="True")

    categoria_ids = fields.Many2many(comodel_name='ing.categoria', string="Categorias")

    tipo = fields.Selection ([
            ('curso', 'Curso'),
            ('certificacion', 'Certificacion'),

        ], string="Tipo")

