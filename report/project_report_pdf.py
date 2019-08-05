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
        partner_id = self.env['res_partner'].search([('partner_id','=',self.wizard_record.partner_id)])       
        vals = []
        vals.append({
                    'name': self.wizard_record.nombre,
                    'id_document': self.partner_id.id_document,
                    'function': self.partner_id.function,
                })

        return {
            'vals': vals,
            'manager': self.name,
            'date_end': self.wizard_record.fecha,
        }




