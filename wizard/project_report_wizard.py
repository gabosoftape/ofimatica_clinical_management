from odoo import models, fields, api, _


class ProjectReportButton(models.TransientModel):
    _name = 'wizard.project.report'

    history_select = fields.Many2one('historial.clinico', string="Historial" , required=True)

    @api.multi
    def print_project_report_pdf(self):
        data = {
            'ids': self.ids,
            'model': self._name,
            'record': self.history_select,
            'name': self.history_select.nombre,
            'partner_id': self.history_select.partner_id,
        }
        return self.env.ref('ofimatica_clinical_management.report_project_pdf').report_action(self, data=data)

    @api.multi
    def print_project_report_xls(self):
        record = self.env['historial.clinico']
        data = {
            'ids': self.ids,
            'model': self._name,
            'record': record.id,
        }
        return self.env.ref('ofimatica_clinical_management.project_xlsx').report_action(self, data=data)
