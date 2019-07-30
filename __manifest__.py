# See LICENSE file for full copyright and licensing details.

{
    'name': 'Administracion Consultorio Oftalmologico',
    'version': '11.0',
    'author': 'Gabriel Pabón',
    'category': 'Health',
    'website': 'https://github.com/gabosoftape/',
    'depends': ['base'],
    'license': 'AGPL-3',
    'summary': 'Con este modulo podras controlar tu consultorio oftalmologico',
    'data': [
            'security/clinical_security.xml',
            'security/ir.model.access.csv',
            'data/clinical_sequence.xml',
            'report/report_view.xml',
            'report/clinical_folio_report_template.xml',
            'views/clinical_view.xml',
            'views/clinical_query.xml',
            'views/templates.xml',
            'views/menus.xml',
    ],
    'css': ['static/src/css/clinical.css'],
    'images': ['static/description/Hotel.png'],
    'application': True
}
