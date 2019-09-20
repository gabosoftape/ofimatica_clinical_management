# See LICENSE file for full copyright and licensing details.

{
    'name': 'Administracion Consultorio Oftalmologico',
    'version': '11.0.1',
    'author': 'Gabriel Pabón',
    'category': 'Health',
    'website': 'https://github.com/gabosoftape/',
    'depends': ['base','stock'],
    'license': 'AGPL-3',
    'summary': 'Con este modulo podras controlar tu consultorio oftalmologico',
    'data': [
            'security/clinical_security.xml',
            'security/ir.model.access.csv',
            'data/clinical_sequence.xml',
            'views/clinical_view.xml',
            'views/clinical_query.xml',
            'views/templates.xml',
            'views/menus.xml',
            'report/project_report_pdf_view.xml',
            'views/project_report.xml',
    ],
    'css': ['static/src/css/clinical.css'],
    'images': ['static/description/icon.png'],
    'application': True
}
