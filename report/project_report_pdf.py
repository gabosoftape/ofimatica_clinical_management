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
    _name = 'report.ofimatica_clinical_management.history_report_template'

    def get_report_values(self, docids, data=None):
        return data

class RemissionReportParser(models.AbstractModel):
    _name = 'report.ofimatica_clinical_management.remission_report_template'

    def get_report_values(self, docids, data=None):
        return data

class FormulaReportParser(models.AbstractModel):
    _name = 'report.ofimatica_clinical_management.formula_report_template'

    def get_report_values(self, docids, data=None):
        return data

class HistoriaReportParser(models.AbstractModel):
    _name = 'report.ofimatica_clinical_management.historial_report_template'

    def get_report_values(self, docids, data=None):
        historial_ids = data['history_ids']
        paciente = data['paciente']
        documento = data['documento']
        return {
            'vals': historial_ids,
            'paciente': paciente,
            'documento': documento,
        }





