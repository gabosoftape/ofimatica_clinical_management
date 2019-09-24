from odoo import api, fields, models

class clinicalCompany(models.Model):
    _inherit ='res.company'

    nit = fields.Char('NIT')
    hab_no = fields.Char('Hab No.')
    cod_ead = fields.Char('Cod EAD')
    pbx_fax = fields.Char('PBX/FAX')
    rte_legal = fields.Char('Representante Legal')
    sede_principal = fields.Selection(string="Sede Principal", selection=[
        ('CHIPICHAPE', 'CHIPICHAPE'),
        ('UNICENTRO', 'UNICENTRO'),
        ('TECNIOPTICA 2142', 'TECNIOPTICA 2142'),
        ('TECNIOPTICA 1090', 'TECNIOPTICA 1090'),
        ('TECNIOPTICA 1195', 'TECNIOPTICA 1195'),
        ('TECNIOPTICA 1005', 'TECNIOPTICA 1005'),
        ('PRINCIPAL SAS', 'PRINCIPAL SAS'),
        ('COMERCIAL 1189', 'COMERCIAL 1189'),
        ('COMERCIAL 1187', 'COMERCIAL 1187'),
    ])