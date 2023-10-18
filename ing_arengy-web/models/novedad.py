from odoo import fields, models, api
import random
from odoo.exceptions import UserError, ValidationError

class Novedad(models.Model):
    _name = 'ing.novedad'


    name         = fields.Char(string='Titulo', requred=True , tracking=True)
    inner_image  = fields.Image(string='Imagen interna ', tracking=True, required=True)
    image        = fields.Image(string='Imagen en cuadricula', tracking=True, required=True)
    desc         = fields.Html(string=u'Descripción', tracking=True, required=True)
    fecha        = fields.Date(string='Fecha', tracking=True, default=fields.Date.context_today)

    categoria_ids = fields.Many2many(comodel_name='ing.categoria', string="Categorias")



    def get_fecha(self):
        dic = {
            'January': 'Enero',
            'February': 'Febrero',
            'March': 'Marzo',
            'April': 'Abril',
            'May': 'Mayo',
            'June': 'Junio',
            'July': 'Julio',
            'August': 'Agosto',
            'September': 'Septiembre',
            'October': 'Octubre',
            'November': 'Noviembre',
            'December': 'Diciembre',
        }
        dia = self.fecha.strftime('%d')
        mes = self.fecha.strftime('%B')
        anio = self.fecha.strftime('%Y')
        return "{0} de {1} | {2}".format(dia, dic.get(mes, mes), anio)

