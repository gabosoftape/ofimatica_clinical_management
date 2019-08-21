from odoo import api, fields, models

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
    second_last_name = fields.Char(string='Segundo Apellido')
    age = fields.Integer(string='Edad')
    sex = fields.Selection(
        string=u'Sexo',
        selection=[
            ('M', 'Masculino'),
            ('F', 'Femenino')
        ],
    )
    zone = fields.Selection([('U','Urbana'),('R','Rural')])
    companion = fields.Many2one('res.partner', string="Acompañante")
    companion_document = fields.Integer(string="No. Documento", readonly=1, related='companion.id_document')
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
