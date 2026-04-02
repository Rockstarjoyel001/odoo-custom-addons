{
    'name': 'Unique Distribution E-commerce',
    'version': '1.0',
    'summary': 'Custom E-commerce features for Unique Distribution style site',
    'category': 'Website',
    'author': 'Odoo Developer',
    'depends': ['website_sale', 'stock'],
    'data': [
        'views/product_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}