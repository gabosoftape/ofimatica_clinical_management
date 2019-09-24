from odoo import api, fields, models

class clinicalCompany(models.Model):
    _inherit ='res.company'

    nit = fields.Char('NIT')
    hab_no = fields.Char('Hab No.')
    cod_ead = fields.Char('Cod EAD')
    pbx_fax = fields.Char('PBX/FAX')
    rte_legal = fields.Char('Representante Legal')
    sede_principal = fields.Selection(string="Sede Principal", selection=[
        ('1', 'CHIPICHAPE'),
        ('2', 'UNICENTRO'),
        ('3', 'TECNIOPTICA 2142'),
        ('4', 'TECNIOPTICA 1090'),
        ('5', 'TECNIOPTICA 1195'),
        ('6', 'TECNIOPTICA 1005'),
        ('7', 'PRINCIPAL SAS'),
        ('8', 'COMERCIAL 1189'),
        ('9', 'COMERCIAL 1187'),
    ])