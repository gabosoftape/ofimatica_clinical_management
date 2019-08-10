# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons.account.models.partner import ResPartner


class clinicalPartner(models.Model):
    _inherit ='res.partner'

    # Default values that need to be set
    convenio_id = fields.Many2one('convenio.cliente', 'Convenio')
    historial_ids = fields.One2many('historial.clinico', 'partner_id', 'Historial Clinico')
    contact_type = fields.Selection(
        string=u'Tipo de Contacto',
        selection=[
            ('1', u'Paciente'),
            ('2', u'Medico'),
            ('3', u'Especialista'),
        ],
        default='1',
        required=False,
        help=u'Identificacion del Cliente, segun los tipos definidos por la DIAN.',
    )
    id_type = fields.Selection(
        string=u'Tipo de Documento',
        selection=[
            ('CC','CEDULA DE CIUDADANÍA'),
            ('CE', 'CEDULA DE EXTRANJERÍA'),
            ('PA', 'PASAPORTE'),
            ('SC', 'SALVO CONDUCTO'),
            ('RC',  'REGISTRO CIVIL '),
            ('PE',  'PERMISO ESPECIAL DE PERMANENCIA'),
            ('TI',  'TARJETA DE IDENTIDAD'),
            ('AS',  'ADULTO SIN IDENTIFICAR'),
            ('MS',  'MENOR SIN IDENTIFICAR'),
        ],
        required=False,
        help=u'Identificacion del Cliente',
    )
    id_document = fields.Integer(string='No. Documento', default=None)
    first_name = fields.Char(string='Primer Nombre')
    second_name = fields.Char(string='Segundo Nombre')
    last_name= fields.Char(string='Primer Apellido')
    second_last_name = fields.Char(string='Primer Apellido')
    age = fields.Integer(string='Edad')
    age_udm = fields.Selection(
        string=u'Selecciona Unidad',
        selection=[
            ('1', u'Años'),
            ('2', u'Meses'),
            ('3', u'Dias')
        ],
        default='1',
    )
    sex = fields.Selection(
        string=u'Sexo',
        selection=[
            ('M', 'Masculino'),
            ('F', 'Femenino')
        ],
    )
    zone = fields.Selection([('U','Urbana'),('R','Rural')])
    companion = fields.Many2one('res.partner', string="Acompañante")
    companion_document = fields.Integer(string="No. Documento", readonly=1, default=None)
    companion_parentezco = fields.Char(string="Parentezco")
    companion_tel = fields.Char(string="Telefono de Contacto")
    # company_type is only an interface field, do not use it in business logic
    company_type = fields.Selection(string='Company Type',
                                    selection=[('person', 'Individual'), ('company', 'Company'), ('patient', 'Paciente')],
                                    compute='_compute_company_type', inverse='_write_company_type')
    nombre = fields.Char(string="Nombre")

    @api.depends('is_company')
    def _compute_ofimatica_company_type(self):
        for partner in self:
            partner.company_type = 'company' if partner.is_company else 'person'

    def _write_ofimatica_company_type(self):
        for partner in self:
            partner.is_company = partner.company_type == 'company'

    @api.onchange('company_type')
    def onchange_ofimatica_company_type(self):
        self.is_company = False
        if self.company_type == 'person':
            print('es persona')
        elif self.company_type == 'company':
            print('es compañia')
        elif self.company_type == 'patient':
            print('es paciente')



    @api.onchange('first_name', 'second_name', 'last_name', 'second_last_name')
    def _onchange_person_names(self):
        if self.company_type == 'person':
            names = [name for name in [self.first_name, self.second_name, self.last_name, self.second_last_name] if name]
            self.name = u' '.join(names)
            self.nombre = self.name
            self.display_name = self.nombre


class ConvenioCliente(models.Model):
    _name = 'convenio.cliente'
    _description = 'Convenio de Clientes'

    name = fields.Char('Descripcion', size=128, required=True)
    code = fields.Char('Codigo de Convenio', size=128, required=True)


class HistorialAgudezaDerecho(models.Model):
    _name = 'historial.agudeza.derecho'
    _description = 'Agudeza Visual Ojo Derecho'

    name = fields.Char('...', size=128, required=True)
    sc = fields.Char('SC', size=128)
    vl = fields.Char('VL', size=128)
    vp = fields.Char('VP', size=128)
    historial_id = fields.Many2one('historial.clinico', 'ID Ref')
    no_unlink = fields.Boolean('No permitir Borrar')

    @api.multi
    def unlink(self):
        for rec in self:
            if rec.no_unlink:
                return True
                # raise UserError("No se permite eliminar registros de Agudeza Visual")
        res = super(HistorialAgudezaDerecho, self).unlink()
        return res


class HistorialAgudezaIzquierdo(models.Model):
    _name = 'historial.agudeza.izquierdo'
    _description = 'Agudeza Visual Ojo Izquierdo'

    name = fields.Char('...', size=128)
    sc = fields.Char('SC', size=128)
    vl = fields.Char('VL', size=128)
    vp = fields.Char('VP', size=128)
    historial_id = fields.Many2one('historial.clinico', 'ID Ref')
    no_unlink = fields.Boolean('No permitir Borrar')

    @api.multi
    def unlink(self):
        for rec in self:
            if rec.no_unlink:
                return True
                # raise UserError("No se permite eliminar registros de Agudeza Visual")
        res = super(HistorialAgudezaIzquierdo, self).unlink()
        return res


class HistorialClinico(models.Model):
    _name = 'historial.clinico'
    _description = 'Historial Clinico'

    _rec_name = 'nombre'

    @api.model
    def default_get(self, fields):
        # res = super(sale_order_invoice_wizard, self).default_get(fields)

        # res.update(ticket_ids=tickets)
        # contextual_self = self.with_context(default_load_default=True)
        res = super(HistorialClinico, self).default_get(fields)
        # res.update({'ticket_ids': tickets})
        res.update({'load_default': True})
        return res

    state = fields.Selection([('cancelada', 'Cancelada'), ('cita', 'Cita Agendada'), ('proceso', 'En Proceso'),
                              ('cerrada', 'Consulta Terminada')], 'Estado', default="cita")

    partner_id = fields.Many2one('res.partner', 'Paciente', domain=[('customer', '=', True)], required=True)
    convenio_id = fields.Many2one('convenio.cliente', 'Convenio')

    finalidad = fields.Selection([('8', ' 8 - Deteccion de Alteraciones de agudeza visual'), ('9', 'Otro') ], default='8')
    tipo_servicio = fields.Selection([('1', 'Primera Vez'), ('2', 'Control')], default='1')

    fecha = fields.Datetime('Fecha y Hora', default=fields.datetime.now())

    nombre = fields.Char('Nombre', related='partner_id.name')

    motivo = fields.Text('Motivo de Consulta')

    antecedentes_familiares = fields.Text('Antecedentes Generales Familiares y Personales')

    antecedentes_oculares = fields.Text('Antecedentes Oculares Familiares y Personales')

    ## Agudeza ##
    load_default = fields.Boolean('Cargar Valores', default=True)

    agudeza_derecho_ids = fields.One2many('historial.agudeza.derecho', 'historial_id', 'Agudeza Ojo Derecho')

    agudeza_izquierdo_ids = fields.One2many('historial.agudeza.izquierdo', 'historial_id', 'Agudeza Ojo Izquiero')

    ## LENSOMETRIA
    lensometria_od = fields.Char('OD', size=128)
    lensometria_id = fields.Char('OI', size=128)

    ### Datos Historicos
    examen_anterior = fields.Char('Examen Segmento Anterior', size=128)
    examen_motor = fields.Char('Examen Motor', size=128)
    examen_posterior = fields.Char('Examen Segmento Posterior', size=128)
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
    rx_final_od_dp  = fields.Char('Rx uso OD DP')
    rx_final_od_dnp = fields.Char('Rx uso OD DNP')
    rx_final_oi_dp = fields.Char('Rx uso OI DP')
    rx_final_oi_dnp = fields.Char('Rx uso OI DNP')
    rx_final_od_vp_esf = fields.Char('Rx final OI DNP')
    rx_final_od_vp_cil = fields.Char('Rx final OI DNP')
    rx_final_oi_vp_esf = fields.Char('Rx final OI DNP')
    rx_final_oi_vp_cil = fields.Char('Rx final OI DNP')

    ### RX FINAL ###

    prismas = fields.Char('Prismas', size=128)
    tipo_de_lente = fields.Char('Tipo de lente', size=128)
    diagnostico = fields.Char('Diagnostico', size=256)
    plan = fields.Char('Plan de Manejo', size=256)
    ### DIAGNOSTICO ###
    oftalmoscopia = fields.Text()
    dx_primario = fields.Selection(string='Dx primario', selection=[
        ('H520', 'HIPERMETROPIA'),
        ('H521', 'MIOPIA'),
        ('H522', 'ASTIGMATISMO'),
        ('H524', 'PRESBICIA'),
        ('H500', 'ESTRABISMO CONCOMITANTE CONVERGENTE'),
        ('H501', 'ESTRABISMO CONCOMITANTE DIVERGENTE'),
        ('H502', 'ESTRABISMO VERTICAL'),
        ('H503', 'HETEROTROPIA INTERMITENTE'),
        ('H504', 'OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS'),
        ('H505', 'HETEROFORIA'),
        ('H506', 'ESTRABISMO MECANICO'),
        ('H508', 'OTROS ESTRABISMOS ESPECIFICADOS'),
        ('H509', 'ESTRABISMO, NO ESPECIFICADO'),
        ('H510', 'PARALISIS DE LA CONJUGACION DE LA MIRADA'),
        ('H511', 'EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR'),
        ('H512', 'OFTALMOPLEJIA INTERNUCLEAR'),
        ('H518', 'OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES'),
        ('H519', 'TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO'),
        ('H523', 'ANISOMETROPIA Y ANISEICONIA'),
        ('H525', 'TRASTORNOS DE LA ACOMODACION'),
        ('H526', 'OTROS TRASTORNOS DE LA REFRACCION'),
        ('H527', 'TRASTORNO DE LA REFRACCION, NO ESPECIFICADO'),
        ('H530', 'AMBLIOPIA EX ANOPSIA'),
        ('H531', 'ALTERACIONES VISUALES SUBJETIVAS'),
        ('H532', 'DIPLOPIA'),
        ('H533', 'OTROS TRASTORNOS DE LA VISION BINOCULAR'),
        ('H534', 'DEFECTOS DEL CAMPO VISUAL'),
        ('H535', 'DEFICIENCIAS DE LA VISION CROMATICA'),
        ('H536', 'CEGUERA NOCTURNA'),
        ('H538', 'OTRAS ALTERACIONES VISUALES'),
        ('H539', 'ALTERACION VISUAL, NO ESPECIFICADA'),
        ('H540', 'CEGUERA DE AMBOS OJOS'),
        ('H541', 'CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO'),
        ('H542', 'VISION  SUBNORMAL DE AMBOS OJOS'),
        ('H543', 'DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS'),
        ('H544', 'CEGUERA  DE UN OJO'),
        ('H545', 'VISION SUBNORMAL DE UN OJO'),
        ('H546', 'DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO'),
        ('H547', 'DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION'),
        ('H55X', 'NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES'),
        ('H570', 'ANOMALIAS DE LA FUNCION PUPILAR'),
        ('H571', 'DOLOR OCULAR'),
        ('H578', 'OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS'),
        ('H579', 'TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO'),
        ('H580', 'NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('H581', 'ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('H588', 'OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('H590', 'SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA'),
        ('H598', 'OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS'),
        ('H599', 'TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS'),

    ])
    dx_secundario = fields.Selection(string='Dx Secundario', selection=[
        ('H520', 'HIPERMETROPIA'),
        ('H521', 'MIOPIA'),
        ('H522', 'ASTIGMATISMO'),
        ('H524', 'PRESBICIA'),
        ('H500', 'ESTRABISMO CONCOMITANTE CONVERGENTE'),
        ('H501', 'ESTRABISMO CONCOMITANTE DIVERGENTE'),
        ('H502', 'ESTRABISMO VERTICAL'),
        ('H503', 'HETEROTROPIA INTERMITENTE'),
        ('H504', 'OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS'),
        ('H505', 'HETEROFORIA'),
        ('H506', 'ESTRABISMO MECANICO'),
        ('H508', 'OTROS ESTRABISMOS ESPECIFICADOS'),
        ('H509', 'ESTRABISMO, NO ESPECIFICADO'),
        ('H510', 'PARALISIS DE LA CONJUGACION DE LA MIRADA'),
        ('H511', 'EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR'),
        ('H512', 'OFTALMOPLEJIA INTERNUCLEAR'),
        ('H518', 'OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES'),
        ('H519', 'TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO'),
        ('H523', 'ANISOMETROPIA Y ANISEICONIA'),
        ('H525', 'TRASTORNOS DE LA ACOMODACION'),
        ('H526', 'OTROS TRASTORNOS DE LA REFRACCION'),
        ('H527', 'TRASTORNO DE LA REFRACCION, NO ESPECIFICADO'),
        ('H530', 'AMBLIOPIA EX ANOPSIA'),
        ('H531', 'ALTERACIONES VISUALES SUBJETIVAS'),
        ('H532', 'DIPLOPIA'),
        ('H533', 'OTROS TRASTORNOS DE LA VISION BINOCULAR'),
        ('H534', 'DEFECTOS DEL CAMPO VISUAL'),
        ('H535', 'DEFICIENCIAS DE LA VISION CROMATICA'),
        ('H536', 'CEGUERA NOCTURNA'),
        ('H538', 'OTRAS ALTERACIONES VISUALES'),
        ('H539', 'ALTERACION VISUAL, NO ESPECIFICADA'),
        ('H540', 'CEGUERA DE AMBOS OJOS'),
        ('H541', 'CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO'),
        ('H542', 'VISION  SUBNORMAL DE AMBOS OJOS'),
        ('H543', 'DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS'),
        ('H544', 'CEGUERA  DE UN OJO'),
        ('H545', 'VISION SUBNORMAL DE UN OJO'),
        ('H546', 'DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO'),
        ('H547', 'DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION'),
        ('H55X', 'NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES'),
        ('H570', 'ANOMALIAS DE LA FUNCION PUPILAR'),
        ('H571', 'DOLOR OCULAR'),
        ('H578', 'OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS'),
        ('H579', 'TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO'),
        ('H580', 'NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('H581', 'ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('H588', 'OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('H590', 'SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA'),
        ('H598', 'OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS'),
        ('H599', 'TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS'),

    ])
    dx_terciario = fields.Selection(string='Dx Terciario', selection=[
        ('H520', 'HIPERMETROPIA'),
        ('H521', 'MIOPIA'),
        ('H522', 'ASTIGMATISMO'),
        ('H524', 'PRESBICIA'),
        ('H500', 'ESTRABISMO CONCOMITANTE CONVERGENTE'),
        ('H501', 'ESTRABISMO CONCOMITANTE DIVERGENTE'),
        ('H502', 'ESTRABISMO VERTICAL'),
        ('H503', 'HETEROTROPIA INTERMITENTE'),
        ('H504', 'OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS'),
        ('H505', 'HETEROFORIA'),
        ('H506', 'ESTRABISMO MECANICO'),
        ('H508', 'OTROS ESTRABISMOS ESPECIFICADOS'),
        ('H509', 'ESTRABISMO, NO ESPECIFICADO'),
        ('H510', 'PARALISIS DE LA CONJUGACION DE LA MIRADA'),
        ('H511', 'EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR'),
        ('H512', 'OFTALMOPLEJIA INTERNUCLEAR'),
        ('H518', 'OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES'),
        ('H519', 'TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO'),
        ('H523', 'ANISOMETROPIA Y ANISEICONIA'),
        ('H525', 'TRASTORNOS DE LA ACOMODACION'),
        ('H526', 'OTROS TRASTORNOS DE LA REFRACCION'),
        ('H527', 'TRASTORNO DE LA REFRACCION, NO ESPECIFICADO'),
        ('H530', 'AMBLIOPIA EX ANOPSIA'),
        ('H531', 'ALTERACIONES VISUALES SUBJETIVAS'),
        ('H532', 'DIPLOPIA'),
        ('H533', 'OTROS TRASTORNOS DE LA VISION BINOCULAR'),
        ('H534', 'DEFECTOS DEL CAMPO VISUAL'),
        ('H535', 'DEFICIENCIAS DE LA VISION CROMATICA'),
        ('H536', 'CEGUERA NOCTURNA'),
        ('H538', 'OTRAS ALTERACIONES VISUALES'),
        ('H539', 'ALTERACION VISUAL, NO ESPECIFICADA'),
        ('H540', 'CEGUERA DE AMBOS OJOS'),
        ('H541', 'CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO'),
        ('H542', 'VISION  SUBNORMAL DE AMBOS OJOS'),
        ('H543', 'DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS'),
        ('H544', 'CEGUERA  DE UN OJO'),
        ('H545', 'VISION SUBNORMAL DE UN OJO'),
        ('H546', 'DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO'),
        ('H547', 'DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION'),
        ('H55X', 'NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES'),
        ('H570', 'ANOMALIAS DE LA FUNCION PUPILAR'),
        ('H571', 'DOLOR OCULAR'),
        ('H578', 'OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS'),
        ('H579', 'TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO'),
        ('H580', 'NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('H581', 'ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('H588', 'OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('H590', 'SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA'),
        ('H598', 'OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS'),
        ('H599', 'TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS'),

    ])


    ### Formula ###

    material = fields.Char('Material', size=128)
    filtros = fields.Char('Filtros', size=128)
    uso = fields.Char('Uso', size=128)
    formula_plan = fields.Char('Plan de Manejo', size=256)
    formula_notas = fields.Text('Notas')
    optometra_id = fields.Many2one('res.partner', 'Optometra')
    folio = fields.Char('Folio', size=128)
    sede = fields.Selection(string="Sede", selection=[
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
    is_remision = fields.Boolean('	Remitido a especialista ', default=False)
    especialista_id = fields.Many2one('res.partner', 'Especialista')
    observaciones = fields.Text()
    conducta = fields.Text()

    ### prescripcion y usoo ###
    pres_tipo_lente = fields.Selection([('bifocal','Bifocal'),('ocupacional','Ocupacional'),('progresivo','Progresivo'),('sencillo','Visión sencilla')],'Tipo de lente')
    pres_material = fields.Selection([('cr39','CR39'),('policarbonato','Policarbonato')],'Material')
    pres_filtro = fields.Selection([('ar','AR'),('uv','UV')],'filtros')
    pres_uso = fields.Selection([('permanente','Permanente'),('ocacional','Ocacional'),('cerca','Cerca'),('lejos','Lejos')],'Modo de uso.')

    @api.multi
    def print_report(self):
    # Method to print sale order report
        historial_ids = self.search([], limit=1).ids
        return self.env.ref(
        'ofimatica_clinical_management.report_custom_template').report_action(historial_ids)

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id and self.partner_id.convenio_id:
            self.convenio_id = self.partner_id.convenio_id.id
        if self.partner_id:
            self.nombre = self.partner_id.name


    @api.multi
    def cita(self):
        self.state = 'cita'

    @api.multi
    def cancelada(self):
        self.state = 'cancelada'

    @api.multi
    def proceso(self):
        self.state = 'proceso'

    @api.multi
    def cerrada(self):
        self.state = 'cerrada'

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
        vals['folio'] = str(number)
        result = super(HistorialClinico, self).create(vals)
        return result






