from odoo import models, fields, api, _


class ProjectReportButton(models.TransientModel):
    _name = 'wizard.project.report'

    history_select = fields.Many2one('historial.clinico', string="Historial" , required=True)

    @api.multi
    def print_project_report_pdf(self):
        nombre = self.history_select.nombre
        caption = self.env['res.partner'].search([('name','like',nombre)])
        data = {
            'record': self.history_select,
            'nombre': caption.name,
            'documento': caption.id_document,
            'function': caption.function,
            'fecha': self.history_select.fecha,
            'diagnostico_primario': self.history_select.diagnostico,
            'oftalmoscopia': 'sin datos aun',
            'conducta': self.history_select.plan,
        }
        #Datos
        print(data)
        return self.env.ref('ofimatica_clinical_management.report_project_pdf').report_action(self, data=data)
    @api.multi
    def print_remission_report_pdf(self):
        nombre = self.history_select.nombre
        caption = self.env['res.partner'].search([('name','like',nombre)])
        data = {
            'record': self.history_select,
            'nombre': caption.name,
            'documento': caption.id_document,
            'function': caption.function,
            'fecha': self.history_select.fecha,
            'rx_od': self.history_select.rx_od,
            'rx_oi': self.history_select.rx_oi,
            'rx_od_av': self.history_select.rx_od_av,
            'rx_oi_av': self.history_select.rx_oi_av,
            'rx_add': self.history_select.rx_add,
            'diagnostico_primario': self.history_select.diagnostico,
            'oftalmoscopia': 'sin datos aun',
            'conducta': self.history_select.plan,
            'is_remision' : self.history_select.is_remision,
        }
        #Datos
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
    def print_project_report_xls(self):
        record = self.env['historial.clinico']
        data = {
            'ids': self.ids,
            'model': self._name,
            'record': record.id,
        }
        return self.env.ref('ofimatica_clinical_management.project_xlsx').report_action(self, data=data)
