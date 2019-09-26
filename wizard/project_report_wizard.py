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
        paciente = self.env['res.partner'].search([('name','like', nombre)])
        hs = self.history_select
        data = {
            'record': self.history_select,
            'nombre': paciente.name,
            'documento': paciente.id_document,
            'function': paciente.function,
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
            'rx_final_od_prisma': hs.rx_final_od_prisma,
            'rx_final_oi_prisma': hs.rx_final_oi_prisma,
            'rx_final_od_av': hs.rx_final_od_av,
            'rx_final_oi_av': hs.rx_final_oi_av,
        }
        #Datos
        print(data)
        return self.env.ref('ofimatica_clinical_management.report_project_pdf').report_action(self, data=data)
    @api.multi
    def print_remission_report_pdf(self):
        hs = self.history_select
        nombre = hs.partner_id.name
        paciente = self.env['res.partner'].search([('name','like',nombre)])
        #Datos
        data = {
            'nombre': paciente.name,
            'documento': paciente.id_document,
            'function': paciente.function,
            'telefono': paciente.phone,
            'eps': paciente.eps,
            'edad': paciente.age,
            'sexo': paciente.sex,
            'optometra': hs.optometra_id.name,
            'remitido_a': hs.especialista_id.name,
            'fecha': hs.fecha,
            'motivo': hs.motivo,
            'rx_uso_od_esf': hs.rx_uso_od_esf,
            'rx_uso_od_cil': hs.rx_uso_od_cil,
            'rx_uso_oi_esf': hs.rx_uso_oi_esf,
            'rx_uso_oi_cil': hs.rx_uso_oi_cil,
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
            'rx_final_od_prisma': hs.rx_final_od_prisma,
            'rx_final_oi_prisma': hs.rx_final_oi_prisma,
            'rx_final_od_av': hs.rx_final_od_av,
            'rx_final_oi_av': hs.rx_final_oi_av,
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
        paciente = self.env['res.partner'].search([('name', 'like', nombre)])
        hs = self.history_select
        data = {
            'record': hs,
            'nombre': paciente.name,
            'documento': paciente.id_document,
            'function': paciente.function,
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
            'rx_final_od_prisma': hs.rx_final_od_prisma,
            'rx_final_oi_prisma': hs.rx_final_oi_prisma,
            'rx_final_od_av': hs.rx_final_od_av,
            'rx_final_oi_av': hs.rx_final_oi_av,
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
        partner = self.partner_id
        paciente = self.env['res.partner'].search([('id', '=', partner.id)])
        historial_ids = self.env['historial.clinico'].search([('partner_id','like',partner.id)])
        seguimientos_ids = self.env['historial.clinico.seguimiento'].search([('paciente','like',partner.id)])
        history = []
        for historia in historial_ids:
            if historia.is_seguimiento:
                seguimientos = []
                for seguimiento in seguimientos_ids:
                    if seguimiento.historia_id.folio == historia.folio:
                        seguimientos.append({
                            'fecha_seguimiento': seguimiento.fecha_seguimiento,
                            'historia': seguimiento.historia_id.folio,
                            'paciente': seguimiento.paciente.name,
                            'rx_final_od_esf': seguimiento.rx_final_od_esf,
                            'rx_final_od_cil': seguimiento.rx_final_od_cil,
                            'rx_final_od_eje': seguimiento.rx_final_od_eje,
                            'rx_final_od_add': seguimiento.rx_final_od_add,
                            'rx_final_od_dp': seguimiento.rx_final_od_dp,
                            'rx_final_od_dnp': seguimiento.rx_final_od_dnp,
                            'rx_final_od_vp_esf': seguimiento.rx_final_od_vp_esf,
                            'rx_final_od_vp_cil': seguimiento.rx_final_od_vp_cil,
                            'rx_final_od_av': seguimiento.rx_final_od_av,
                            'rx_final_od_prisma': seguimiento.rx_final_od_prisma,
                            'rx_final_oi_esf': seguimiento.rx_final_oi_esf,
                            'rx_final_oi_cil': seguimiento.rx_final_oi_cil,
                            'rx_final_oi_eje': seguimiento.rx_final_oi_eje,
                            'rx_final_oi_add': seguimiento.rx_final_oi_add,
                            'rx_final_oi_dp': seguimiento.rx_final_oi_dp,
                            'rx_final_oi_dnp': seguimiento.rx_final_oi_dnp,
                            'rx_final_oi_vp_esf': seguimiento.rx_final_oi_vp_esf,
                            'rx_final_oi_vp_cil': seguimiento.rx_final_oi_vp_cil,
                            'rx_final_oi_av': seguimiento.rx_final_oi_av,
                            'rx_final_oi_prisma': seguimiento.rx_final_oi_prisma,
                            'oftalmoscopia': seguimiento.oftalmoscopia,
                            'dx_primario': seguimiento.dx_primario,
                            'dx_secundario':seguimiento.dx_secundario,
                            'dx_terciario':seguimiento.dx_terciario,
                            'is_remision':seguimiento.is_remision,
                            'remision_desc':seguimiento.remision_desc,
                            'observaciones': seguimiento.observaciones,
                            'conducta': seguimiento.conducta,
                            'tipo_lente': seguimiento.tipo_lente,
                            'material': seguimiento.material,
                            'filtros': seguimiento.filtros,
                            'uso': seguimiento.uso,
                        })

            history.append({
                'folio': historia.folio,
                'sede': historia.sede,
                'optometra': historia.optometra_id.name,
                'fecha': historia.fecha,
                'licor': historia.is_licor,
                'fumador': historia.is_fumador,
                'lentes': historia.is_lentes,
                'lentes_desc': historia.lentes_desc,
                'enfermedad_here': historia.is_enfermedad_here,
                'enfermedad_here_desc': historia.enfermedad_here_desc,
                'operaciones': historia.is_operaciones,
                'operaciones_desc': historia.operaciones_desc,
                'alergias': historia.is_alergias,
                'alergias_desc': historia.alergias_desc,
                'medicacion': historia.is_medicacion,
                'medicacion_desc': historia.medicacion_desc,
                'antecedentes_oculares': historia.antecedentes_oculares,
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
                'rx_final_od_prisma': historia.rx_final_od_prisma,
                'rx_final_oi_prisma': historia.rx_final_oi_prisma,
                'rx_final_od_av': historia.rx_final_od_av,
                'rx_final_oi_av': historia.rx_final_oi_av,
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
                'is_seguimiento': historia.is_seguimiento,
                'seguimientos': seguimientos,
                'observaciones': historia.observaciones,
                'rx_uso_observaciones': historia.rx_uso_observaciones,
                'notas_queratometria': historia.notas_queratometria_refraccion,
                'formula_notas': historia.formula_notas,
            })
        data = {
            'paciente': paciente.name,
            'nombres': paciente.first_name + ' ' + paciente.second_name,
            'apellidos': paciente.last_name +' '+ paciente.second_last_name,
            'tipo_documento': paciente.id_type,
            'documento': paciente.id_document,
            'direccion': partner.street,
            'telefono': paciente.phone,
            'edad': paciente.age,
            'estado_civil': paciente.estado_civil,
            'profesion': paciente.function,
            'eps': paciente.eps,
            'tipo_afil': paciente.afil_type,
            'tipo_us': paciente.us_type,
            'sexo': paciente.sex,
            'email': paciente.email,
            'ciudad': paciente.city,
            'pat_repot': paciente.pat_repot,
            'zona': paciente.zone,
            'departamento': paciente.state_id.name,
            'companion_name': paciente.companion.name,
            'companion_document': paciente.companion_document,
            'companion_parentezco': paciente.companion_parentezco,
            'companion_tel': paciente.companion_tel,
            'history_ids': history,
        }
        # Datos
        print(data)
        return self.env.ref('ofimatica_clinical_management.report_historial_pdf').report_action(self, data=data)
