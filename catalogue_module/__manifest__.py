{
    'name': 'Catalog Module',
    'summary': '',
    'description': "Allow user to create catalogue",
    'author': 'Omar Doukmak',
    'website': 'omar.doukmak.computerscience@gmail.com , +963 930 462 613',

    # category can be used to filter modules in modules listing
    'category': 'sale',
    'version': '0.1',

    # any module for this one to work correctly
    'depends': ['base', 'web', 'product', 'elmakan_dashboard'],

    'assets': {},

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/product_collection.xml',
        'views/product_color.xml',
        'views/product_material.xml',
        'views/product_family.xml',
        'views/product_piece.xml',
        'views/product_technology.xml',
        'views/product_feature.xml',
        'views/product_packing_type.xml',
        'views/product_template.xml',
        'report/report_info.xml',
        'report/catalogue_template.xml',
    ],

    # loaded in demo mode only
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
    # 'post_init_hook': 'remove_contact_us_menu',
}
