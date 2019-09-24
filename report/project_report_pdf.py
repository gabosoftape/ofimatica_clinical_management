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
        nombres = data['nombres']
        apellidos = data['apellidos']
        tipo_documento= data['tipo_documento']
        direccion = data['direccion']
        telefono = data['telefono']
        edad = data['edad']
        estado_civil = data['estado_civil']
        profesion = data['profesion']
        eps = data['eps']
        tipo_afil = data['tipo_afil']
        tipo_us = data['tipo_us']
        sexo = data['sexo']
        email= data['email']
        ciudad = data['ciudad']
        pat_repot = data['pat_repot']
        zona = data['zona']
        departamento = data['departamento']
        companion_name = data['companion_name']
        companion_documento = data['companion_document']
        companion_parentezco = data['companion_parentezco']
        companion_tel = data['companion_tel']

        return {
            'vals': historial_ids,
            'paciente': paciente,
            'documento': documento,
            'nombres': nombres,
            'apellidos': apellidos,
            'tipo_documento': tipo_documento,
            'direccion': direccion,
            'telefono': telefono,
            'edad': edad,
            'estado_civil': estado_civil,
            'profesion': profesion,
            'eps': eps,
            'tipo_afil': tipo_afil,
            'tipo_us': tipo_us,
            'sexo': sexo,
            'email': email,
            'ciudad': ciudad,
            'pat_repot': pat_repot,
            'zona': zona,
            'departamento': departamento,
            'companion_name': companion_name,
            'companion_documento': companion_documento,
            'companion_parentezco': companion_parentezco,
            'companion_tel': companion_tel,
        }