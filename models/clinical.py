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
            ('11', u'11 - Registro civil de nacimiento'),
            ('12', u'12 - Tarjeta de identidad'),
            ('13', u'13 - Cédula de ciudadanía'),
            ('14',
             u'14 - Certificado de la Registraduría para sucesiones ilíquidas de personas naturales que no tienen ningún documento de identificación.'),
            ('15',
             u'15 - Tipo de documento que identifica una sucesión ilíquida, expedido por la notaria o por un juzgado. '),
            ('21', u'21 - Tarjeta de extranjería'),
            ('22', u'22 - Cédula de extranjería'),
            ('31', u'31 - NIT/RUT'),
            ('33', u'33 - Identificación de extranjeros diferente al NIT asignado DIAN'),
            ('41', u'41 - Pasaporte'),
            ('42', u'42 - Documento de identificación extranjero'),
            ('43', u'43 - Sin identificación del exterior o para uso definido por la DIAN'),
        ],
        required=False,
        help=u'Identificacion del Cliente, segun los tipos definidos por la DIAN.',
    )
    id_document = fields.Integer(string='No. Documento', default=None)
    first_name = fields.Char(string='Primer Nombre')
    second_name = fields.Char(string='Segundo Nombre')
    last_name= fields.Char(string='Primer Apellido')
    second_last_name = fields.Char(string='Primer Apellido')
    age = fields.Integer(string='Edad', default=None)
    age_udm = fields.Selection(
        string=u'Selecciona Unidad',
        selection=[
            ('1', u'1 - Años'),
            ('2', u'2 - Meses'),
            ('3', u'3 - Dias')
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
    zone = fields.Selection([('Zona1','zona1')])
    function = fields.Char('Profesion')
    companion = fields.Many2one('res.partner', string="Acompañante")
    companion_document = fields.Integer(string="No. Documento", readonly=1, default=None)
    companion_parentezco = fields.Char(string="Parentezco")
    companion_tel = fields.Char(string="Telefono de Contacto")

    @api.onchange('first_name', 'second_name', 'last_name', 'second_last_name')
    def _onchange_person_names(self):
        if self.company_type == 'person':
            names = [name for name in [self.first_name, self.second_name, self.last_name, self.second_last_name] if name]
            self.name = u' '.join(names)


class ConvenioCliente(models.Model):
    _name = 'convenio.cliente'
    _description = 'Convenio de Clientes'

    name = fields.Char('Descripcion', size=128, required=True)


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

    anamnesis = fields.Text('Anamnesis')

    fecha = fields.Date('Fecha', default=fields.Date.today())

    documento_identidad = fields.Char('Documento de Identidad', size=128)

    nombre = fields.Char('Nombre', size=128)

    apellidos = fields.Char('Apellidos', size=128)

    edad = fields.Integer('Edad')

    ocupacion = fields.Char('Ocupacion', size=128)

    telefono = fields.Char('Telefono', size=128)

    celular = fields.Char('Celular', size=128)

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

    ### RX FINAL ###

    rx_od = fields.Char('OD', size=128)
    rx_oi = fields.Char('OI', size=128)
    rx_od_av = fields.Char('AV', size=128)
    rx_oi_av = fields.Char('AV', size=128)
    rx_add = fields.Char('ADD', size=128)
    rx_dp = fields.Char('DP', size=128)
    rx_dnp = fields.Char('DNP', size=128)
    primas = fields.Char('Primas', size=128)
    tipo_de_lente = fields.Char('Tipo de lente', size=128)
    diagnostico = fields.Char('Diagnostico', size=256)
    plan = fields.Char('Plan de Manejo', size=256)

    ### Formula ###

    formula_rx_od = fields.Char('OD', size=128)
    formula_rx_oi = fields.Char('OI', size=128)
    formula_rx_od_av = fields.Char('AV', size=128)
    formula_rx_oi_av = fields.Char('AV', size=128)
    formula_rx_add = fields.Char('ADD', size=128)
    formula_rx_dp = fields.Char('DP', size=128)
    formula_rx_dnp = fields.Char('DNP', size=128)
    formula_primas = fields.Char('Primas', size=128)
    formula_tipo_de_lente = fields.Char('Tipo de lente', size=128)
    material = fields.Char('Material', size=128)
    filtros = fields.Char('Filtros', size=128)
    uso = fields.Char('Uso', size=128)
    farmaco_1 = fields.Char('Farmaco 1', size=128)
    farmaco_2 = fields.Char('Farmaco 2', size=128)
    formula_plan = fields.Char('Plan de Manejo', size=256)
    formula_notas = fields.Text('Notas')
    optometra_id = fields.Many2one('res.partner', 'Optometra')
    folio = fields.Char('Folio', size=128)

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id and self.partner_id.convenio_id:
            self.convenio_id = self.partner_id.convenio_id.id
        if self.partner_id:
            self.nombre = self.partner_id.name
            self.telefono = self.partner_id.phone
            self.celular = self.partner_id.mobile

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
        vals['folio'] = self.env['ir.sequence'].next_by_code('historial.clinico') or _('Folio No.')
        result = super(HistorialClinico, self).create(vals)
        return result


