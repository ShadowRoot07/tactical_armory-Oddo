from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    square_token = fields.Char(string="ID Square (Token)", help="Identificador único de Square")
    is_tactical_gear = fields.Boolean(string="Equipamiento Táctico", default=True)
    grade_quality = fields.Selection([
        ('basic', 'Entrada / Amateur'),
        ('mid', 'Intermedio / Simulación'),
        ('pro', 'Grado Profesional / Mil-Sim')
    ], string="Grado del Equipo", default='mid')
    technical_specs = fields.Text(string="Especificaciones Técnicas")

