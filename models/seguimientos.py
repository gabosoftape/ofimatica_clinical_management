from odoo import api, fields, models, _
from odoo.addons.account.models.partner import ResPartner

class HistorialClinicoSeguimientos(models.Model):
    _name = 'historial.clinico.seguimiento'
    fecha_seguimiento = fields.Datetime('Fecha de Seguimiento', default=fields.datetime.now())
    paciente = fields.Many2one('res.partner', 'Paciente', domain=[('customer', '=', True)], required=True)
    ### RX FINAL ###
    rx_final_od_esf = fields.Char('OD ESF')
    rx_final_od_cil = fields.Char('OD CIL')
    rx_final_od_eje = fields.Char('OD EJE')
    rx_final_od_add = fields.Char('OD ADD')
    rx_final_od_dp = fields.Char('OD DP')
    rx_final_od_dnp = fields.Char('OD DNP')
    rx_final_od_vp_esf = fields.Char('OD VP ESF')
    rx_final_od_vp_cil = fields.Char('OD VP CIL')
    rx_final_od_av = fields.Char('OD AV')
    rx_final_od_prisma = fields.Char('OD PRISMA')
    rx_final_oi_esf = fields.Char('OI ESF')
    rx_final_oi_cil = fields.Char('OI CIL')
    rx_final_oi_eje = fields.Char('OI EJE')
    rx_final_oi_add = fields.Char('OI ADD')
    rx_final_oi_dp = fields.Char('OI DP')
    rx_final_oi_dnp = fields.Char('OI DNP')
    rx_final_oi_vp_esf = fields.Char('OI VP ESF')
    rx_final_oi_vp_cil = fields.Char('OI VP CIL')
    rx_final_oi_av = fields.Char('Rx final oi av')
    rx_final_oi_prisma = fields.Char('Prisma OI')
        ### DIAGNOSTICO ###
    ### DIAGNOSTICO ###
    oftalmoscopia = fields.Text()
    dx_primario = fields.Char(string='Dx primario', selection=[
        ('HIPERMETROPIA', 'H520 - HIPERMETROPIA'),
        ('MIOPIA', 'H521 MIOPIA'),
        ('ASTIGMATISMO', 'H522 - ASTIGMATISMO'),
        ('PRESBICIA', 'H524 - PRESBICIA'),
        ('ESTRABISMO CONCOMITANTE CONVERGENTE', 'H500 - ESTRABISMO CONCOMITANTE CONVERGENTE'),
        ('ESTRABISMO CONCOMITANTE DIVERGENTE', 'H501 - ESTRABISMO CONCOMITANTE DIVERGENTE'),
        ('ESTRABISMO VERTICAL', 'H502 - ESTRABISMO VERTICAL'),
        ('HETEROTROPIA INTERMITENTE', 'H503 - HETEROTROPIA INTERMITENTE'),
        ('OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS', 'H504 - OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS'),
        ('HETEROFORIA', 'H505 - HETEROFORIA'),
        ('ESTRABISMO MECANICO', 'H506 - ESTRABISMO MECANICO'),
        ('OTROS ESTRABISMOS ESPECIFICADOS', 'H508 - OTROS ESTRABISMOS ESPECIFICADOS'),
        ('ESTRABISMO, NO ESPECIFICADO', 'H509 - ESTRABISMO, NO ESPECIFICADO'),
        ('PARALISIS DE LA CONJUGACION DE LA MIRADA', 'H510 - PARALISIS DE LA CONJUGACION DE LA MIRADA'),
        ('EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR', 'H511 - EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR'),
        ('OFTALMOPLEJIA INTERNUCLEAR', 'H512 - OFTALMOPLEJIA INTERNUCLEAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES',
         'H518 - OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES'),
        ('TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO',
         'H519 - TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO'),
        ('ANISOMETROPIA Y ANISEICONIA', 'H523 - ANISOMETROPIA Y ANISEICONIA'),
        ('TRASTORNOS DE LA ACOMODACION', 'H525 - TRASTORNOS DE LA ACOMODACION'),
        ('OTROS TRASTORNOS DE LA REFRACCION', 'H526 - OTROS TRASTORNOS DE LA REFRACCION'),
        ('TRASTORNO DE LA REFRACCION, NO ESPECIFICADO', 'H527 - TRASTORNO DE LA REFRACCION, NO ESPECIFICADO'),
        ('AMBLIOPIA EX ANOPSIA', 'H530 - AMBLIOPIA EX ANOPSIA'),
        ('ALTERACIONES VISUALES SUBJETIVAS', 'H531 - ALTERACIONES VISUALES SUBJETIVAS'),
        ('DIPLOPIA', 'H532 - DIPLOPIA'),
        ('OTROS TRASTORNOS DE LA VISION BINOCULAR', 'H533 - OTROS TRASTORNOS DE LA VISION BINOCULAR'),
        ('DEFECTOS DEL CAMPO VISUAL', 'H534 - DEFECTOS DEL CAMPO VISUAL'),
        ('DEFICIENCIAS DE LA VISION CROMATICA', 'H535 - DEFICIENCIAS DE LA VISION CROMATICA'),
        ('CEGUERA NOCTURNA', 'H536 - CEGUERA NOCTURNA'),
        ('OTRAS ALTERACIONES VISUALES', 'H538 - OTRAS ALTERACIONES VISUALES'),
        ('ALTERACION VISUAL, NO ESPECIFICADA', 'H539 - ALTERACION VISUAL, NO ESPECIFICADA'),
        ('CEGUERA DE AMBOS OJOS', 'H540 - CEGUERA DE AMBOS OJOS'),
        ('CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO', 'H541 - CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO'),
        ('VISION  SUBNORMAL DE AMBOS OJOS', 'H542 - VISION  SUBNORMAL DE AMBOS OJOS'),
        ('DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS',
         'H543 - DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS'),
        ('CEGUERA  DE UN OJO', 'H544 - CEGUERA  DE UN OJO'),
        ('VISION SUBNORMAL DE UN OJO', 'H545 - VISION SUBNORMAL DE UN OJO'),
        ('DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO',
         'H546 - DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO'),
        ('DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION',
         'H547 - DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION'),
        ('NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES',
         'H55X - NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES'),
        ('ANOMALIAS DE LA FUNCION PUPILAR', 'H570 - ANOMALIAS DE LA FUNCION PUPILAR'),
        ('HIPERMETROPIA', 'H520 - HIPERMETROPIA'),
        ('MIOPIA', 'H521 MIOPIA'),
        ('ASTIGMATISMO', 'H522 - ASTIGMATISMO'),
        ('PRESBICIA', 'H524 - PRESBICIA'),
        ('ESTRABISMO CONCOMITANTE CONVERGENTE', 'H500 - ESTRABISMO CONCOMITANTE CONVERGENTE'),
        ('ESTRABISMO CONCOMITANTE DIVERGENTE', 'H501 - ESTRABISMO CONCOMITANTE DIVERGENTE'),
        ('ESTRABISMO VERTICAL', 'H502 - ESTRABISMO VERTICAL'),
        ('HETEROTROPIA INTERMITENTE', 'H503 - HETEROTROPIA INTERMITENTE'),
        ('OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS', 'H504 - OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS'),
        ('HETEROFORIA', 'H505 - HETEROFORIA'),
        ('ESTRABISMO MECANICO', 'H506 - ESTRABISMO MECANICO'),
        ('OTROS ESTRABISMOS ESPECIFICADOS', 'H508 - OTROS ESTRABISMOS ESPECIFICADOS'),
        ('ESTRABISMO, NO ESPECIFICADO', 'H509 - ESTRABISMO, NO ESPECIFICADO'),
        ('PARALISIS DE LA CONJUGACION DE LA MIRADA', 'H510 - PARALISIS DE LA CONJUGACION DE LA MIRADA'),
        ('EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR', 'H511 - EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR'),
        ('OFTALMOPLEJIA INTERNUCLEAR', 'H512 - OFTALMOPLEJIA INTERNUCLEAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES',
         'H518 - OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES'),
        ('TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO',
         'H519 - TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO'),
        ('ANISOMETROPIA Y ANISEICONIA', 'H523 - ANISOMETROPIA Y ANISEICONIA'),
        ('TRASTORNOS DE LA ACOMODACION', 'H525 - TRASTORNOS DE LA ACOMODACION'),
        ('OTROS TRASTORNOS DE LA REFRACCION', 'H526 - OTROS TRASTORNOS DE LA REFRACCION'),
        ('TRASTORNO DE LA REFRACCION, NO ESPECIFICADO', 'H527 - TRASTORNO DE LA REFRACCION, NO ESPECIFICADO'),
        ('AMBLIOPIA EX ANOPSIA', 'H530 - AMBLIOPIA EX ANOPSIA'),
        ('ALTERACIONES VISUALES SUBJETIVAS', 'H531 - ALTERACIONES VISUALES SUBJETIVAS'),
        ('DIPLOPIA', 'H532 - DIPLOPIA'),
        ('OTROS TRASTORNOS DE LA VISION BINOCULAR', 'H533 - OTROS TRASTORNOS DE LA VISION BINOCULAR'),
        ('DEFECTOS DEL CAMPO VISUAL', 'H534 - DEFECTOS DEL CAMPO VISUAL'),
        ('DEFICIENCIAS DE LA VISION CROMATICA', 'H535 - DEFICIENCIAS DE LA VISION CROMATICA'),
        ('CEGUERA NOCTURNA', 'H536 - CEGUERA NOCTURNA'),
        ('OTRAS ALTERACIONES VISUALES', 'H538 - OTRAS ALTERACIONES VISUALES'),
        ('ALTERACION VISUAL, NO ESPECIFICADA', 'H539 - ALTERACION VISUAL, NO ESPECIFICADA'),
        ('CEGUERA DE AMBOS OJOS', 'H540 - CEGUERA DE AMBOS OJOS'),
        ('CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO', 'H541 - CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO'),
        ('VISION  SUBNORMAL DE AMBOS OJOS', 'H542 - VISION  SUBNORMAL DE AMBOS OJOS'),
        ('DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS',
         'H543 - DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS'),
        ('CEGUERA  DE UN OJO', 'H544 - CEGUERA  DE UN OJO'),
        ('VISION SUBNORMAL DE UN OJO', 'H545 - VISION SUBNORMAL DE UN OJO'),
        ('DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO',
         'H546 - DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO'),
        ('DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION',
         'H547 - DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION'),
        ('NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES',
         'H55X - NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES'),
        ('ANOMALIAS DE LA FUNCION PUPILAR', 'H570 - ANOMALIAS DE LA FUNCION PUPILAR'),
        ('DOLOR OCULAR', 'H571 - DOLOR OCULAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS',
         'H578 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS'),
        ('TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO', 'H579 - TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO'),
        ('NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H580 - NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H581 - ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H588 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA',
         'H590 - SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA'),
        ('OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS',
         'H598 - OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS'),
        ('TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS',
         'H599 - TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS'),
        ('DOLOR OCULAR', 'H571 - DOLOR OCULAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS',
         'H578 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS'),
        ('TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO', 'H579 - TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO'),
        ('NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H580 - NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H581 - ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H588 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA',
         'H590 - SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA'),
        ('OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS',
         'H598 - OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS'),
        ('TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS',
         'H599 - TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS'),

    ])
    dx_secundario = fields.Char(string='Dx Secundario', selection=[
        ('HIPERMETROPIA', 'H520 - HIPERMETROPIA'),
        ('MIOPIA', 'H521 MIOPIA'),
        ('ASTIGMATISMO', 'H522 - ASTIGMATISMO'),
        ('PRESBICIA', 'H524 - PRESBICIA'),
        ('ESTRABISMO CONCOMITANTE CONVERGENTE', 'H500 - ESTRABISMO CONCOMITANTE CONVERGENTE'),
        ('ESTRABISMO CONCOMITANTE DIVERGENTE', 'H501 - ESTRABISMO CONCOMITANTE DIVERGENTE'),
        ('ESTRABISMO VERTICAL', 'H502 - ESTRABISMO VERTICAL'),
        ('HETEROTROPIA INTERMITENTE', 'H503 - HETEROTROPIA INTERMITENTE'),
        ('OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS', 'H504 - OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS'),
        ('HETEROFORIA', 'H505 - HETEROFORIA'),
        ('ESTRABISMO MECANICO', 'H506 - ESTRABISMO MECANICO'),
        ('OTROS ESTRABISMOS ESPECIFICADOS', 'H508 - OTROS ESTRABISMOS ESPECIFICADOS'),
        ('ESTRABISMO, NO ESPECIFICADO', 'H509 - ESTRABISMO, NO ESPECIFICADO'),
        ('PARALISIS DE LA CONJUGACION DE LA MIRADA', 'H510 - PARALISIS DE LA CONJUGACION DE LA MIRADA'),
        ('EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR', 'H511 - EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR'),
        ('OFTALMOPLEJIA INTERNUCLEAR', 'H512 - OFTALMOPLEJIA INTERNUCLEAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES',
         'H518 - OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES'),
        ('TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO',
         'H519 - TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO'),
        ('ANISOMETROPIA Y ANISEICONIA', 'H523 - ANISOMETROPIA Y ANISEICONIA'),
        ('TRASTORNOS DE LA ACOMODACION', 'H525 - TRASTORNOS DE LA ACOMODACION'),
        ('OTROS TRASTORNOS DE LA REFRACCION', 'H526 - OTROS TRASTORNOS DE LA REFRACCION'),
        ('TRASTORNO DE LA REFRACCION, NO ESPECIFICADO', 'H527 - TRASTORNO DE LA REFRACCION, NO ESPECIFICADO'),
        ('AMBLIOPIA EX ANOPSIA', 'H530 - AMBLIOPIA EX ANOPSIA'),
        ('ALTERACIONES VISUALES SUBJETIVAS', 'H531 - ALTERACIONES VISUALES SUBJETIVAS'),
        ('DIPLOPIA', 'H532 - DIPLOPIA'),
        ('OTROS TRASTORNOS DE LA VISION BINOCULAR', 'H533 - OTROS TRASTORNOS DE LA VISION BINOCULAR'),
        ('DEFECTOS DEL CAMPO VISUAL', 'H534 - DEFECTOS DEL CAMPO VISUAL'),
        ('DEFICIENCIAS DE LA VISION CROMATICA', 'H535 - DEFICIENCIAS DE LA VISION CROMATICA'),
        ('CEGUERA NOCTURNA', 'H536 - CEGUERA NOCTURNA'),
        ('OTRAS ALTERACIONES VISUALES', 'H538 - OTRAS ALTERACIONES VISUALES'),
        ('ALTERACION VISUAL, NO ESPECIFICADA', 'H539 - ALTERACION VISUAL, NO ESPECIFICADA'),
        ('CEGUERA DE AMBOS OJOS', 'H540 - CEGUERA DE AMBOS OJOS'),
        ('CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO', 'H541 - CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO'),
        ('VISION  SUBNORMAL DE AMBOS OJOS', 'H542 - VISION  SUBNORMAL DE AMBOS OJOS'),
        ('DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS',
         'H543 - DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS'),
        ('CEGUERA  DE UN OJO', 'H544 - CEGUERA  DE UN OJO'),
        ('VISION SUBNORMAL DE UN OJO', 'H545 - VISION SUBNORMAL DE UN OJO'),
        ('DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO',
         'H546 - DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO'),
        ('DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION',
         'H547 - DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION'),
        ('NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES',
         'H55X - NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES'),
        ('ANOMALIAS DE LA FUNCION PUPILAR', 'H570 - ANOMALIAS DE LA FUNCION PUPILAR'),
        ('HIPERMETROPIA', 'H520 - HIPERMETROPIA'),
        ('MIOPIA', 'H521 MIOPIA'),
        ('ASTIGMATISMO', 'H522 - ASTIGMATISMO'),
        ('PRESBICIA', 'H524 - PRESBICIA'),
        ('ESTRABISMO CONCOMITANTE CONVERGENTE', 'H500 - ESTRABISMO CONCOMITANTE CONVERGENTE'),
        ('ESTRABISMO CONCOMITANTE DIVERGENTE', 'H501 - ESTRABISMO CONCOMITANTE DIVERGENTE'),
        ('ESTRABISMO VERTICAL', 'H502 - ESTRABISMO VERTICAL'),
        ('HETEROTROPIA INTERMITENTE', 'H503 - HETEROTROPIA INTERMITENTE'),
        ('OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS', 'H504 - OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS'),
        ('HETEROFORIA', 'H505 - HETEROFORIA'),
        ('ESTRABISMO MECANICO', 'H506 - ESTRABISMO MECANICO'),
        ('OTROS ESTRABISMOS ESPECIFICADOS', 'H508 - OTROS ESTRABISMOS ESPECIFICADOS'),
        ('ESTRABISMO, NO ESPECIFICADO', 'H509 - ESTRABISMO, NO ESPECIFICADO'),
        ('PARALISIS DE LA CONJUGACION DE LA MIRADA', 'H510 - PARALISIS DE LA CONJUGACION DE LA MIRADA'),
        ('EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR', 'H511 - EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR'),
        ('OFTALMOPLEJIA INTERNUCLEAR', 'H512 - OFTALMOPLEJIA INTERNUCLEAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES',
         'H518 - OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES'),
        ('TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO',
         'H519 - TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO'),
        ('ANISOMETROPIA Y ANISEICONIA', 'H523 - ANISOMETROPIA Y ANISEICONIA'),
        ('TRASTORNOS DE LA ACOMODACION', 'H525 - TRASTORNOS DE LA ACOMODACION'),
        ('OTROS TRASTORNOS DE LA REFRACCION', 'H526 - OTROS TRASTORNOS DE LA REFRACCION'),
        ('TRASTORNO DE LA REFRACCION, NO ESPECIFICADO', 'H527 - TRASTORNO DE LA REFRACCION, NO ESPECIFICADO'),
        ('AMBLIOPIA EX ANOPSIA', 'H530 - AMBLIOPIA EX ANOPSIA'),
        ('ALTERACIONES VISUALES SUBJETIVAS', 'H531 - ALTERACIONES VISUALES SUBJETIVAS'),
        ('DIPLOPIA', 'H532 - DIPLOPIA'),
        ('OTROS TRASTORNOS DE LA VISION BINOCULAR', 'H533 - OTROS TRASTORNOS DE LA VISION BINOCULAR'),
        ('DEFECTOS DEL CAMPO VISUAL', 'H534 - DEFECTOS DEL CAMPO VISUAL'),
        ('DEFICIENCIAS DE LA VISION CROMATICA', 'H535 - DEFICIENCIAS DE LA VISION CROMATICA'),
        ('CEGUERA NOCTURNA', 'H536 - CEGUERA NOCTURNA'),
        ('OTRAS ALTERACIONES VISUALES', 'H538 - OTRAS ALTERACIONES VISUALES'),
        ('ALTERACION VISUAL, NO ESPECIFICADA', 'H539 - ALTERACION VISUAL, NO ESPECIFICADA'),
        ('CEGUERA DE AMBOS OJOS', 'H540 - CEGUERA DE AMBOS OJOS'),
        ('CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO', 'H541 - CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO'),
        ('VISION  SUBNORMAL DE AMBOS OJOS', 'H542 - VISION  SUBNORMAL DE AMBOS OJOS'),
        ('DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS',
         'H543 - DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS'),
        ('CEGUERA  DE UN OJO', 'H544 - CEGUERA  DE UN OJO'),
        ('VISION SUBNORMAL DE UN OJO', 'H545 - VISION SUBNORMAL DE UN OJO'),
        ('DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO',
         'H546 - DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO'),
        ('DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION',
         'H547 - DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION'),
        ('NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES',
         'H55X - NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES'),
        ('ANOMALIAS DE LA FUNCION PUPILAR', 'H570 - ANOMALIAS DE LA FUNCION PUPILAR'),
        ('DOLOR OCULAR', 'H571 - DOLOR OCULAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS',
         'H578 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS'),
        ('TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO', 'H579 - TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO'),
        ('NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H580 - NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H581 - ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H588 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA',
         'H590 - SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA'),
        ('OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS',
         'H598 - OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS'),
        ('TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS',
         'H599 - TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS'),
        ('DOLOR OCULAR', 'H571 - DOLOR OCULAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS',
         'H578 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS'),
        ('TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO', 'H579 - TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO'),
        ('NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H580 - NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H581 - ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H588 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA',
         'H590 - SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA'),
        ('OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS',
         'H598 - OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS'),
        ('TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS',
         'H599 - TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS'),

    ])
    dx_terciario = fields.Char(string='Dx Terciario', selection=[
        ('HIPERMETROPIA', 'H520 - HIPERMETROPIA'),
        ('MIOPIA', 'H521 MIOPIA'),
        ('ASTIGMATISMO', 'H522 - ASTIGMATISMO'),
        ('PRESBICIA', 'H524 - PRESBICIA'),
        ('ESTRABISMO CONCOMITANTE CONVERGENTE', 'H500 - ESTRABISMO CONCOMITANTE CONVERGENTE'),
        ('ESTRABISMO CONCOMITANTE DIVERGENTE', 'H501 - ESTRABISMO CONCOMITANTE DIVERGENTE'),
        ('ESTRABISMO VERTICAL', 'H502 - ESTRABISMO VERTICAL'),
        ('HETEROTROPIA INTERMITENTE', 'H503 - HETEROTROPIA INTERMITENTE'),
        ('OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS', 'H504 - OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS'),
        ('HETEROFORIA', 'H505 - HETEROFORIA'),
        ('ESTRABISMO MECANICO', 'H506 - ESTRABISMO MECANICO'),
        ('OTROS ESTRABISMOS ESPECIFICADOS', 'H508 - OTROS ESTRABISMOS ESPECIFICADOS'),
        ('ESTRABISMO, NO ESPECIFICADO', 'H509 - ESTRABISMO, NO ESPECIFICADO'),
        ('PARALISIS DE LA CONJUGACION DE LA MIRADA', 'H510 - PARALISIS DE LA CONJUGACION DE LA MIRADA'),
        ('EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR', 'H511 - EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR'),
        ('OFTALMOPLEJIA INTERNUCLEAR', 'H512 - OFTALMOPLEJIA INTERNUCLEAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES',
         'H518 - OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES'),
        ('TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO',
         'H519 - TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO'),
        ('ANISOMETROPIA Y ANISEICONIA', 'H523 - ANISOMETROPIA Y ANISEICONIA'),
        ('TRASTORNOS DE LA ACOMODACION', 'H525 - TRASTORNOS DE LA ACOMODACION'),
        ('OTROS TRASTORNOS DE LA REFRACCION', 'H526 - OTROS TRASTORNOS DE LA REFRACCION'),
        ('TRASTORNO DE LA REFRACCION, NO ESPECIFICADO', 'H527 - TRASTORNO DE LA REFRACCION, NO ESPECIFICADO'),
        ('AMBLIOPIA EX ANOPSIA', 'H530 - AMBLIOPIA EX ANOPSIA'),
        ('ALTERACIONES VISUALES SUBJETIVAS', 'H531 - ALTERACIONES VISUALES SUBJETIVAS'),
        ('DIPLOPIA', 'H532 - DIPLOPIA'),
        ('OTROS TRASTORNOS DE LA VISION BINOCULAR', 'H533 - OTROS TRASTORNOS DE LA VISION BINOCULAR'),
        ('DEFECTOS DEL CAMPO VISUAL', 'H534 - DEFECTOS DEL CAMPO VISUAL'),
        ('DEFICIENCIAS DE LA VISION CROMATICA', 'H535 - DEFICIENCIAS DE LA VISION CROMATICA'),
        ('CEGUERA NOCTURNA', 'H536 - CEGUERA NOCTURNA'),
        ('OTRAS ALTERACIONES VISUALES', 'H538 - OTRAS ALTERACIONES VISUALES'),
        ('ALTERACION VISUAL, NO ESPECIFICADA', 'H539 - ALTERACION VISUAL, NO ESPECIFICADA'),
        ('CEGUERA DE AMBOS OJOS', 'H540 - CEGUERA DE AMBOS OJOS'),
        ('CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO', 'H541 - CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO'),
        ('VISION  SUBNORMAL DE AMBOS OJOS', 'H542 - VISION  SUBNORMAL DE AMBOS OJOS'),
        ('DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS',
         'H543 - DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS'),
        ('CEGUERA  DE UN OJO', 'H544 - CEGUERA  DE UN OJO'),
        ('VISION SUBNORMAL DE UN OJO', 'H545 - VISION SUBNORMAL DE UN OJO'),
        ('DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO',
         'H546 - DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO'),
        ('DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION',
         'H547 - DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION'),
        ('NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES',
         'H55X - NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES'),
        ('ANOMALIAS DE LA FUNCION PUPILAR', 'H570 - ANOMALIAS DE LA FUNCION PUPILAR'),
        ('HIPERMETROPIA', 'H520 - HIPERMETROPIA'),
        ('MIOPIA', 'H521 MIOPIA'),
        ('ASTIGMATISMO', 'H522 - ASTIGMATISMO'),
        ('PRESBICIA', 'H524 - PRESBICIA'),
        ('ESTRABISMO CONCOMITANTE CONVERGENTE', 'H500 - ESTRABISMO CONCOMITANTE CONVERGENTE'),
        ('ESTRABISMO CONCOMITANTE DIVERGENTE', 'H501 - ESTRABISMO CONCOMITANTE DIVERGENTE'),
        ('ESTRABISMO VERTICAL', 'H502 - ESTRABISMO VERTICAL'),
        ('HETEROTROPIA INTERMITENTE', 'H503 - HETEROTROPIA INTERMITENTE'),
        ('OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS', 'H504 - OTRAS HETEROTROPIAS O LAS NO ESPECIFICADAS'),
        ('HETEROFORIA', 'H505 - HETEROFORIA'),
        ('ESTRABISMO MECANICO', 'H506 - ESTRABISMO MECANICO'),
        ('OTROS ESTRABISMOS ESPECIFICADOS', 'H508 - OTROS ESTRABISMOS ESPECIFICADOS'),
        ('ESTRABISMO, NO ESPECIFICADO', 'H509 - ESTRABISMO, NO ESPECIFICADO'),
        ('PARALISIS DE LA CONJUGACION DE LA MIRADA', 'H510 - PARALISIS DE LA CONJUGACION DE LA MIRADA'),
        ('EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR', 'H511 - EXCESO E INSUFICIENCIA DE LA CONVERGENCIA OCULAR'),
        ('OFTALMOPLEJIA INTERNUCLEAR', 'H512 - OFTALMOPLEJIA INTERNUCLEAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES',
         'H518 - OTROS TRASTORNOS ESPECIFICADOS DE LOS MOVIMIENTOS BINOCULARES'),
        ('TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO',
         'H519 - TRASTORNOS DEL MOVIMIENTO BINOCULAR, NO ESPECIFICADO'),
        ('ANISOMETROPIA Y ANISEICONIA', 'H523 - ANISOMETROPIA Y ANISEICONIA'),
        ('TRASTORNOS DE LA ACOMODACION', 'H525 - TRASTORNOS DE LA ACOMODACION'),
        ('OTROS TRASTORNOS DE LA REFRACCION', 'H526 - OTROS TRASTORNOS DE LA REFRACCION'),
        ('TRASTORNO DE LA REFRACCION, NO ESPECIFICADO', 'H527 - TRASTORNO DE LA REFRACCION, NO ESPECIFICADO'),
        ('AMBLIOPIA EX ANOPSIA', 'H530 - AMBLIOPIA EX ANOPSIA'),
        ('ALTERACIONES VISUALES SUBJETIVAS', 'H531 - ALTERACIONES VISUALES SUBJETIVAS'),
        ('DIPLOPIA', 'H532 - DIPLOPIA'),
        ('OTROS TRASTORNOS DE LA VISION BINOCULAR', 'H533 - OTROS TRASTORNOS DE LA VISION BINOCULAR'),
        ('DEFECTOS DEL CAMPO VISUAL', 'H534 - DEFECTOS DEL CAMPO VISUAL'),
        ('DEFICIENCIAS DE LA VISION CROMATICA', 'H535 - DEFICIENCIAS DE LA VISION CROMATICA'),
        ('CEGUERA NOCTURNA', 'H536 - CEGUERA NOCTURNA'),
        ('OTRAS ALTERACIONES VISUALES', 'H538 - OTRAS ALTERACIONES VISUALES'),
        ('ALTERACION VISUAL, NO ESPECIFICADA', 'H539 - ALTERACION VISUAL, NO ESPECIFICADA'),
        ('CEGUERA DE AMBOS OJOS', 'H540 - CEGUERA DE AMBOS OJOS'),
        ('CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO', 'H541 - CEGUERA DE UN OJO, VISION SUBNORMAL DEL OTRO'),
        ('VISION  SUBNORMAL DE AMBOS OJOS', 'H542 - VISION  SUBNORMAL DE AMBOS OJOS'),
        ('DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS',
         'H543 - DISMINUCION INDETERMINADA DE LA AGUDEZA VISUAL EN AMBOS  OJOS'),
        ('CEGUERA  DE UN OJO', 'H544 - CEGUERA  DE UN OJO'),
        ('VISION SUBNORMAL DE UN OJO', 'H545 - VISION SUBNORMAL DE UN OJO'),
        ('DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO',
         'H546 - DISMINUCION  INDETERMINADA DE LA AGUDEZA VISUAL DE UN  OJO'),
        ('DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION',
         'H547 - DISMINUCION DE LA AGUDEZA VISUAL, SIN ESPECIFICACION'),
        ('NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES',
         'H55X - NISTAGMO Y OTROS MOVIMIENTOS OCULARES IRREGULARES'),
        ('ANOMALIAS DE LA FUNCION PUPILAR', 'H570 - ANOMALIAS DE LA FUNCION PUPILAR'),
        ('DOLOR OCULAR', 'H571 - DOLOR OCULAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS',
         'H578 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS'),
        ('TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO', 'H579 - TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO'),
        ('NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H580 - NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H581 - ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H588 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA',
         'H590 - SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA'),
        ('OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS',
         'H598 - OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS'),
        ('TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS',
         'H599 - TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS'),
        ('DOLOR OCULAR', 'H571 - DOLOR OCULAR'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS',
         'H578 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO Y SUS ANEXOS'),
        ('TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO', 'H579 - TRASTORNO DEL OJO Y SUS ANEXOS, NO ESPECIFICADO'),
        ('NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H580 - NOMALIAS DE LA FUNCION PUPILAR EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H581 - ALTERACIONES  DE LA VISION EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE',
         'H588 - OTROS TRASTORNOS ESPECIFICADOS DEL OJO EN ENFERMEDADES CLASIFICADAS EN OTRA PARTE'),
        ('SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA',
         'H590 - SINDROME VITREO CONSECUTIVO A CIRUGIA DE CATARATA'),
        ('OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS',
         'H598 - OTROS TRASTORNOS DEL OJO Y SUS ANEXOS, CONSECUTIVOS A PROCEDIMIENTOS'),
        ('TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS',
         'H599 - TRASTORNO NO ESPECIFICADO DEL OJO Y SUS ANEXOS, CONSECUTIVO A PROCEDIMIENTOS'),

    ])
    is_remision = fields.Boolean('Remitido a especialista', default=False)
    remision_desc = fields.Text('Motivo de remision')
    observaciones = fields.Text('Observaciones')
    conducta = fields.Text('Conducta')
    tipo_lente = fields.Char('Tipo de Lente')
    material = fields.Char('Material')
    filtros = fields.Char('Filtros')
    uso = fields.Text('Uso')
