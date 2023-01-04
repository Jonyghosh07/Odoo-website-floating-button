{
    'name': 'Floating Button',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'sequence': 0,
    'summary': """Custom Floating Icon in Website""",

    'description': """This module creates a floating button at the bottom right of your website and a new submenu 
    named "Custom Website Link" under Website/Configuration , from there you can easily add a website link .""",

    'author': 'Metamorphosis',
    'website': "https://www.metamorphosis.com.bd",
    'depends': ['website', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/portal_icon_view.xml',
        'views/assets.xml',
        'views/website_inherited.xml',
        'views/form_tree.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}