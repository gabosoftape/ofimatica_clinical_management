from odoo import api, fields, models, _
from odoo.addons.account.models.partner import ResPartner

class HistorialClinicoSeguimientos(models.Model):
    _name = 'historial.clinico.seguimiento'
    _description = 'Seguimientos Clinicos'
    _rec_name = 'fecha_seguimiento'
    fecha_seguimiento = fields.Datetime('Fecha de Seguimiento', default=fields.datetime.now())
    historia_id = fields.Many2one('historial.clinico')
    paciente = fields.Many2one('res.partner', 'Paciente', domain=[('customer', '=', True)], required=True)
    ### RX FINAL ###
    rx_final_od_esf = fields.Char('OD ESF')
    rx_final_od_cil = fields.Char('OD CIL')
    rx_final_od_eje = fields.Char('OD EJE')
    rx_final_od_add = fields.Char('OD ADD')
    rx_final_od_dp = fields.Char('OD DP')
    rx_final_od_dnp = fields.Char('OD DNP')
    rx_final_od_vp_esf = fields.Char('OD VP ESF')
    rx_final_od_vp_cil = fields.Char('OD VP CIL')
    rx_final_od_av = fields.Char('OD AV')
    rx_final_od_prisma = fields.Char('OD PRISMA')
    rx_final_oi_esf = fields.Char('OI ESF')
    rx_final_oi_cil = fields.Char('OI CIL')
    rx_final_oi_eje = fields.Char('OI EJE')
    rx_final_oi_add = fields.Char('OI ADD')
    rx_final_oi_dp = fields.Char('OI DP')
    rx_final_oi_dnp = fields.Char('OI DNP')
    rx_final_oi_vp_esf = fields.Char('OI VP ESF')
    rx_final_oi_vp_cil = fields.Char('OI VP CIL')
    rx_final_oi_av = fields.Char('Rx final oi av')
    rx_final_oi_prisma = fields.Char('Prisma OI')
        ### DIAGNOSTICO ###
    ### DIAGNOSTICO ###
    oftalmoscopia = fields.Text()
    dx_primario = fields.Char(string='Dx primario')
    dx_secundario = fields.Char(string='Dx Secundario')
    dx_terciario = fields.Char(string='Dx Terciario')
    is_remision = fields.Boolean('Remitido a especialista', default=False)
    remision_desc = fields.Text('Motivo de remision')
    observaciones = fields.Text('Observaciones')
    conducta = fields.Text('Conducta')
    tipo_lente = fields.Char('Tipo de Lente')
    material = fields.Char('Material')
    filtros = fields.Char('Filtros')
    uso = fields.Text('Uso')

