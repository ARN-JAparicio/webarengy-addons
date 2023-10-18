# -*- coding: utf-8 -*-
from odoo import fields, models, api
import random
from odoo.exceptions import UserError, ValidationError


class Categoria(models.Model):
    _name = 'ing.categoria'

    name = fields.Char(string='Nombre', requred=True, tracking=True)

    post_id = fields.One2many('ing.post', 'categoria_ids')
    # curso_id = fields.Many2many('ing.curso', 'categoria_ids')



