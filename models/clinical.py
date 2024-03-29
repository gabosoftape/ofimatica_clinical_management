# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons.account.models.partner import ResPartner

class ConvenioCliente(models.Model):
    _name = 'convenio.cliente'
    _description = 'Convenio de Clientes'

    name = fields.Char('Descripcion', size=128, required=True)
    code = fields.Char('Codigo de Convenio', size=128, required=True)

class HistorialClinico(models.Model):
    _name = 'historial.clinico'
    _description = 'Historial Clinico'

    _rec_name = 'folio'

    @api.model
    def default_get(self, fields):
        # res = super(sale_order_invoice_wizard, self).default_get(fields)

        # res.update(ticket_ids=tickets)
        # contextual_self = self.with_context(default_load_default=True)
        res = super(HistorialClinico, self).default_get(fields)
        # res.update({'ticket_ids': tickets})
        res.update({'load_default': True})
        return res

    state = fields.Selection([('cancelada', 'Cancelada'),('nueva', 'Cita Nueva'), ('cita', 'Cita Agendada'), ('proceso', 'En Proceso'),
                              ('cerrada', 'Consulta Terminada')], 'Estado', default='nueva')
    history_type = fields.Selection([
        ('Primaria', 'Patologia Primaria'),
        ('Historia', 'Historia'),
        ('Secundaria', 'Patologia Secundaria'),
                              ], 'Estado', default="Historia", compute='_get_default_hs')

    partner_id = fields.Many2one('res.partner', 'Paciente', domain=[('customer', '=', True)], required=True)
    convenio_id = fields.Many2one('convenio.cliente', 'Convenio')
    finalidad = fields.Selection([('8', ' 8 - Deteccion de Alteraciones de agudeza visual'), ('9', 'Otro') ], default='8')
    tipo_servicio = fields.Selection([('1', 'Primera Vez'), ('2', 'Control')], default='1', readonly=True)
    fecha = fields.Datetime('Fecha y Hora', default=fields.datetime.now())

    nombre = fields.Char('Nombre', related='partner_id.name')
    documento = fields.Char('Documento')

    motivo = fields.Text('Motivo de Consulta')

    ## antecedentes_familiares = fields.Text('Antecedentes Generales Familiares y Personales') ##
    is_licor = fields.Boolean('¿Consume licor constantemente?')
    is_fumador = fields.Boolean('¿Fuma cigarrillo?')
    is_lentes = fields.Boolean('¿Usa Lentes?')
    lentes_desc = fields.Text('¡Que tipo de lentes?')
    is_enfermedad_here = fields.Boolean('Enfermedad hereditaria')
    enfermedad_here_desc = fields.Text('Describe qué enfermedades')
    is_operaciones = fields.Boolean('Cirugias')
    operaciones_desc = fields.Text('Descrpcion Cirugias')
    is_alergias = fields.Boolean('Alergias')
    alergias_desc = fields.Text('Descripcion alergias')
    is_medicacion = fields.Boolean('Medicamentos')
    medicacion_desc = fields.Text('Descripcion que medicamentos')

    antecedentes_oculares = fields.Text('Antecedentes Oculares Familiares y Personales')

    ## Agudeza ##
    load_default = fields.Boolean('Cargar Valores', default=True)

    ## LENSOMETRIA
    lensometria_od = fields.Char('OD', size=128)
    lensometria_id = fields.Char('OI', size=128)

    ### Datos Historicos
    examen_anterior = fields.Char('Examen Segmento Anterior', size=128)
    examen_motor = fields.Char('Examen Motor', size=128)
    ishihara = fields.Char('Ishihara', size=128)
    estereopsis = fields.Char('Estereopsis', size=128)

    ## Refraccion y Queratometria

    queratometria_od = fields.Char('OD', size=128)
    refraccion_od = fields.Char('OD', size=128)
    refraccion_bajo_od = fields.Char('OD', size=128)

    queratometria_oi = fields.Char('OI', size=128)
    refraccion_oi = fields.Char('OI', size=128)
    refraccion_bajo_oi = fields.Char('OI', size=128)

    notas_queratometria_refraccion = fields.Text('Notas')
    ### RX USO ###
    rx_uso_od_esf = fields.Char('Rx uso OD ESF')
    rx_uso_od_cil = fields.Char('Rx uso OD CIL')
    rx_uso_od_eje = fields.Char('Rx uso OD EJE')
    rx_uso_od_add = fields.Char('Rx uso OD ADD')
    rx_uso_oi_esf = fields.Char('Rx uso OI ESF')
    rx_uso_oi_cil = fields.Char('Rx uso OI CIL')
    rx_uso_oi_eje = fields.Char('Rx uso OI EJE')
    rx_uso_oi_add = fields.Char('Rx uso OI ADD')
    ### AGUDEZA VISUAL ###
    av_sc_od_vp = fields.Char()
    av_sc_od_vl = fields.Char()
    av_sc_oi_vp = fields.Char()
    av_sc_oi_vl = fields.Char()
    av_cc_od_vp = fields.Char()
    av_cc_od_vl = fields.Char()
    av_cc_oi_vp = fields.Char()
    av_cc_oi_vl = fields.Char()

    ### RX FINAL ###
    rx_final_od_esf = fields.Char('Rx uso OD ESF')
    rx_final_od_cil = fields.Char('Rx uso OD CIL')
    rx_final_od_eje = fields.Char('Rx uso OD EJE')
    rx_final_od_add = fields.Char('Rx uso OD ADD')
    rx_final_oi_esf = fields.Char('Rx uso OI ESF')
    rx_final_oi_cil = fields.Char('Rx uso OI CIL')
    rx_final_oi_eje = fields.Char('Rx uso OI EJE')
    rx_final_oi_add = fields.Char('Rx uso OI ADD')
    rx_final_od_dp = fields.Char('Rx uso OD DP')
    rx_final_od_dnp = fields.Char('Rx uso OD DNP')
    rx_final_oi_dp = fields.Char('Rx uso OI DP')
    rx_final_oi_dnp = fields.Char('Rx uso OI DNP')
    rx_final_od_vp_esf = fields.Char('Rx final OI DNP')
    rx_final_od_vp_cil = fields.Char('Rx final OI DNP')
    rx_final_oi_vp_esf = fields.Char('Rx final OI DNP')
    rx_final_oi_vp_cil = fields.Char('Rx final OI DNP')
    rx_final_od_av = fields.Char('Rx final od av')
    rx_final_oi_av = fields.Char('Rx final oi av')
    rx_final_od_prisma = fields.Char('Prisma OD')
    rx_final_oi_prisma = fields.Char('Prisma OI')
    ### RX FINAL ###

    prismas = fields.Char('Prismas', size=128)
    tipo_de_lente = fields.Char('Tipo de lente', size=128)
    diagnostico = fields.Char('Diagnostico', size=256)
    plan = fields.Char('Plan de Manejo', size=256)
    ### DIAGNOSTICO ###
    oftalmoscopia = fields.Text()
    dx_primario = fields.Char(string='Dx primario')
    dx_secundario = fields.Char(string='Dx Secundario')
    dx_terciario = fields.Char(string='Dx Terciario')
    ### Formula ###

    material = fields.Char('Material', size=128)
    filtros = fields.Char('Filtros', size=128)
    uso = fields.Char('Uso', size=128)
    formula_plan = fields.Char('Plan de Manejo', size=256)
    formula_notas = fields.Text('Notas')
    optometra_id = fields.Many2one('res.users', 'Optometra', domain=[('active', '=', True)])
    folio = fields.Char('Folio', size=128)
    sede = fields.Selection(string="Sede", selection=[
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
    is_remision = fields.Boolean('	Remitido a especialista ', default=False)
    remision_desc = fields.Text('Motivo de remision')
    especialista_id = fields.Many2one('res.partner', 'Especialista')
    observaciones = fields.Text()
    conducta = fields.Text()

    ### prescripcion y usoo ###
    pres_tipo_lente = fields.Char('Tipo de lente')
    pres_material = fields.Selection([('cr39','CR39'),('policarbonato','Policarbonato')],'Material')
    pres_filtro = fields.Char('filtros')
    pres_uso = fields.Selection([('permanente','Permanente'),('ocacional','Ocacional'),('cerca','Cerca'),('lejos','Lejos')],'Modo de uso.')
    pres_control = fields.Char('Control')
    #Observaciones##
    rx_uso_observaciones = fields.Text('Observaciones')
    refraccion_bajo_observaciones = fields.Text('Observaciones')
    seguimientos_id = fields.One2many('historial.clinico.seguimiento','historia_id', string="Seguimientos")
    is_seguimiento = fields.Boolean('Seguimientos')

    @api.multi
    def print_report(self):
    # Method to print sale order report
        historial_ids = self.search([], limit=1).ids
        return self.env.ref(
        'ofimatica_clinical_management.report_custom_template').report_action(historial_ids)

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        paciente = self.partner_id
        historial_check = self.env['historial.clinico'].search([('partner_id', 'like', paciente.id)])
        if historial_check:
            self.tipo_servicio = '2'
        else:
            self.tipo_servicio = '1'
        if self.partner_id and self.partner_id.convenio_id:
            self.convenio_id = self.partner_id.convenio_id.id
        if self.partner_id:
            self.nombre = self.partner_id.name

    @api.onchange('optometra_id')
    def triggerOptometra(self):
        if self.partner_id:
            self.documento = self.partner_id.id_document

    @api.multi
    def cita(self):
        self.state = 'cita'

    @api.multi
    def cancelada(self):
        self.state = 'cancelada'

    @api.multi
    def proceso(self):
        self.state = 'proceso'
        self.documento = self.partner_id.id_document
    @api.multi
    def cerrada(self):
        self.state = 'cerrada'
        self.documento = self.partner_id.id_document

    @api.onchange('load_default', 'partner_id')
    def onchange_load_defaults(self):
        if self.partner_id:
            ojo_derecho = [(0, 0, {
                'name': 'OD',
                'no_unlink': True,
           }), (0, 0, {
                'name': 'OI',
                'no_unlink': True,

           })]
            ojo_izquierdo = [(0, 0, {
               'name': 'OD',
                'no_unlink': True,
           }), (0, 0, {
                'name': 'OI',
                'no_unlink': True,
            })]
            self.agudeza_derecho_ids = ojo_derecho
            self.agudeza_izquierdo_ids = ojo_izquierdo

    @api.model
    def create(self, vals):
        number = self.env['ir.sequence'].next_by_code('historial.clinicoo')
        vals['state'] = 'cita'
        vals['folio'] = str(number)
        result = super(HistorialClinico, self).create(vals)
        return result

