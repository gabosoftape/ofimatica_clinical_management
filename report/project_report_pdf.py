# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Akshay Babu(<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

from odoo.http import request
from odoo import models, api


class ProjectReportParser(models.AbstractModel):
    _name = 'report.project_report_pdf.project_report_template'

    def get_report_values(self, docids, data=None):
        name = data['record']
        wizard_record = request.env['wizard.project.report'].search([])[-1]
        task_obj = request.env['historial.clinico']
        history_selected = []
        current_task = task_obj.search([('stage_id', 'in', history_selected)])

        for elements in wizard_record.stage_select:
            history_selected.append(elements.id)
        
        vals = []
        vals.append({
                    'nombre': history_selected[0].partner_id.name,
                    'id_document': history_selected[0].partner_id.id_document,
                    'function': history_selected[0].partner_id.function,
                })

        return {
            'vals': vals,
            'manager': current_task.partner_id.name,
            'date_end': current_task.fecha,
        }




