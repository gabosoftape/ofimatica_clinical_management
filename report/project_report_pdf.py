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
        history = data['record']
        wizard_record = request.env['wizard.project.report'].search([])[-1]
        vals = []
        vals.append({
                'name': history.nombre,
                'partner_id': history.partner_id,
                'fecha': history.fecha,
                'rx_od': history.rx_od,
                'rx_oi': history.rx_oi,
                'rx_od_av': history.rx_od_av, 
                'rx_oi_av' : history.rx_oi_av,
                'rx_add': history.rx_add, 
                'rx_dp': history.rx_dp,
                'rx_dnp': history.rx_dnp,
                'primas': history.primas,
                'tipo_de_lente': history.tipo_de_lente,
                'diagnostico': history.diagnostico,
                'plan': history.plan,
        })
        return {
            'docs': vals,
            'name': history.nombre,
            'manager': history.partner_id.name,
            'fecha': history.fecha,
        }




