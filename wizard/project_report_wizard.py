from odoo import models, fields, api, _


class ProjectReportButton(models.TransientModel):
    _name = 'wizard.project.report'
    reporte = fields.Selection([('formula', 'Formula'), ('remission', 'Remision'), ('certificado', 'Certificado'),
                              ('history', 'Historia Clinica')], string='Tipo de reporte')
    history_select = fields.Many2one('historial.clinico', string="Historial" )
    partner_id = fields.Many2one('res.partner', string="Paciente")

    @api.multi
    def print_project_report_pdf(self):
        nombre = self.history_select.nombre
        caption = self.env['res.partner'].search([('name','like', nombre)])
        hs = self.history_select
        data = {
            'record': self.history_select,
            'nombre': caption.name,
            'documento': caption.id_document,
            'function': caption.function,
            'fecha': self.history_select.fecha,
            'dx_primario': hs.dx_primario,
            'oftalmoscopia': hs.oftalmoscopia,
            'conducta': self.history_select.plan,
            'rx_final_od_vp_esf': hs.rx_final_od_vp_esf,
            'rx_final_od_vp_cil': hs.rx_final_od_vp_cil,
            'rx_final_oi_vp_esf': hs.rx_final_oi_vp_esf,
            'rx_final_oi_vp_cil': hs.rx_final_oi_vp_cil,
            'rx_final_od_esf': hs.rx_final_od_esf,
            'rx_final_od_cil': hs.rx_final_od_cil,
            'rx_final_oi_esf': hs.rx_final_oi_esf,
            'rx_final_oi_cil': hs.rx_final_oi_cil,
            'rx_final_od_eje': hs.rx_final_od_eje,
            'rx_final_od_add': hs.rx_final_od_add,
            'rx_final_oi_eje': hs.rx_final_oi_eje,
            'rx_final_oi_add': hs.rx_final_oi_add,
            'rx_final_od_dp': hs.rx_final_od_dp,
            'rx_final_od_dnp': hs.rx_final_od_dnp,
            'rx_final_oi_dp': hs.rx_final_oi_dp,
            'rx_final_oi_dnp': hs.rx_final_oi_dnp,
        }
        #Datos
        print(data)
        return self.env.ref('ofimatica_clinical_management.report_project_pdf').report_action(self, data=data)
    @api.multi
    def print_remission_report_pdf(self):
        nombre = self.history_select.nombre
        caption = self.env['res.partner'].search([('name','like',nombre)])
        hs = self.history_select
        #Datos
        data = {
            'nombre': caption.name,
            'documento': caption.id_document,
            'function': caption.function,
            'fecha': hs.fecha,
            'motivo': hs.motivo,
            'rx_final_od_vp_esf': hs.rx_final_od_vp_esf,
            'rx_final_od_vp_cil': hs.rx_final_od_vp_cil,
            'rx_final_oi_vp_esf': hs.rx_final_oi_vp_esf,
            'rx_final_oi_vp_cil': hs.rx_final_oi_vp_cil,
            'rx_final_od_esf': hs.rx_final_od_esf,
            'rx_final_od_cil': hs.rx_final_od_cil,
            'rx_final_oi_esf': hs.rx_final_oi_esf,
            'rx_final_oi_cil': hs.rx_final_oi_cil,
            'rx_final_od_eje': hs.rx_final_od_eje,
            'rx_final_od_add': hs.rx_final_od_add,
            'rx_final_oi_eje': hs.rx_final_oi_eje,
            'rx_final_oi_add': hs.rx_final_oi_add,
            'rx_final_od_dp': hs.rx_final_od_dp,
            'rx_final_od_dnp': hs.rx_final_od_dnp,
            'rx_final_oi_dp': hs.rx_final_oi_dp,
            'rx_final_oi_dnp': hs.rx_final_oi_dnp,
            'queratometria_od': hs.queratometria_od,
            'queratometria_oi': hs.queratometria_oi,
            'refraccion_od': hs.refraccion_od,
            'refraccion_oi': hs.refraccion_oi,
            'dx_primario': hs.dx_primario,
            'dx_secundario': hs.dx_secundario,
            'dx_terciario': hs.dx_terciario,
            'oftalmoscopia': hs.oftalmoscopia,
            'conducta': hs.plan,
            'is_remision': hs.is_remision,
            'remision_desc': hs.remision_desc,
            'next_query': 'un año'
        }
        print(data)
        return self.env.ref('ofimatica_clinical_management.report_remission_pdf').report_action(self, data=data)

    @api.multi
    def print_formula_report_pdf(self):
        nombre = self.history_select.nombre
        caption = self.env['res.partner'].search([('name', 'like', nombre)])
        hs = self.history_select
        data = {
            'record': hs,
            'nombre': caption.name,
            'documento': caption.id_document,
            'function': caption.function,
            'fecha': hs.fecha,
            'diagnostico_primario': hs.diagnostico,
            'oftalmoscopia': 'sin datos aun',
            'conducta': hs.plan,
            'is_remision': hs.is_remision,
            'rx_final_od_esf': hs.rx_final_od_esf,
            'rx_final_od_cil': hs.rx_final_od_cil,
            'rx_final_od_eje': hs.rx_final_od_eje,
            'rx_final_od_add': hs.rx_final_od_add,
            'rx_final_oi_esf': hs.rx_final_oi_esf,
            'rx_final_oi_cil': hs.rx_final_oi_cil,
            'rx_final_oi_eje': hs.rx_final_od_eje,
            'rx_final_oi_add': hs.rx_final_od_add,
            'rx_final_od_dp': hs.rx_final_od_dp,
            'rx_final_od_dnp': hs.rx_final_od_dnp,
            'rx_final_oi_dp': hs.rx_final_oi_dp,
            'rx_final_oi_dnp': hs.rx_final_oi_dnp,
            'rx_final_od_vp_esf': hs.rx_final_od_vp_esf,
            'rx_final_od_vp_cil': hs.rx_final_od_vp_cil,
            'rx_final_oi_vp_esf': hs.rx_final_oi_vp_esf,
            'rx_final_oi_vp_cil': hs.rx_final_oi_vp_cil,
            'prismas': hs.prismas,
            'tipo_de_lente': hs.tipo_de_lente,
            'diagnostico': hs.diagnostico,
            'plan': hs.plan,
            'dx_primario': hs.dx_primario,
            'dx_secundario': hs.dx_secundario,
            'dx_terciario': hs.dx_terciario,
            'pres_tipo_lente':hs.pres_tipo_lente,
            'pres_material': hs.pres_material,
            'pres_filtro': hs.pres_filtro,
        }
        # Datos
        print(data)
        return self.env.ref('ofimatica_clinical_management.report_formula_pdf').report_action(self, data=data)


    @api.multi
    def print_historial_report_pdf(self):
        paciente = self.partner_id
        historial_ids = self.env['historial.clinico'].search([('partner_id','like',paciente.id)])
        history = []
        for historia in historial_ids:
            history.append({
                'folio': historia.folio,
                'fecha': historia.fecha,
                'diagnostico_primario': 'sin datos aun',
                'oftalmoscopia': 'sin datos aun',
                'conducta': historia.plan,
                'is_remision': historia.is_remision,
                'rx_final_od_esf': historia.rx_final_od_esf,
                'rx_final_od_cil': historia.rx_final_od_cil,
                'rx_final_od_eje': historia.rx_final_od_eje,
                'rx_final_od_add': historia.rx_final_od_add,
                'rx_final_oi_esf': historia.rx_final_oi_esf,
                'rx_final_oi_cil': historia.rx_final_oi_cil,
                'rx_final_oi_eje': historia.rx_final_od_eje,
                'rx_final_oi_add': historia.rx_final_od_add,
                'rx_final_od_dp': historia.rx_final_od_dp,
                'rx_final_od_dnp': historia.rx_final_od_dnp,
                'rx_final_oi_dp': historia.rx_final_oi_dp,
                'rx_final_oi_dnp': historia.rx_final_oi_dnp,
                'rx_final_od_vp_esf': historia.rx_final_od_vp_esf,
                'rx_final_od_vp_cil': historia.rx_final_od_vp_cil,
                'rx_final_oi_vp_esf': historia.rx_final_oi_vp_esf,
                'rx_final_oi_vp_cil': historia.rx_final_oi_vp_cil,
                'prismas': historia.prismas,
                'tipo_de_lente': historia.tipo_de_lente,
                'diagnostico': historia.diagnostico,
                'plan': historia.plan,
                'dx_primario': historia.dx_primario,
                'dx_secundario': historia.dx_secundario,
                'dx_terciario': historia.dx_terciario,
                'pres_tipo_lente': historia.pres_tipo_lente,
                'pres_material': historia.pres_material,
                'pres_filtro': historia.pres_filtro,
            })
        data = {
            'paciente': paciente.name,
            'documento': paciente.id_document,
            'history_ids': history,
        }
        # Datos
        print(data)
        return self.env.ref('ofimatica_clinical_management.report_historial_pdf').report_action(self, data=data)
