{
    'name': 'Open academy',
    'version': '16.1.0',
    'website': 'https://recursostecnologicos.pe',
    'category': 'Education',
    'author': "Josue Rodriguez - Recursos Tecnologicos",
    'sequence': 50,
    'summary': 'Module for learn Odoo and Python',
    'depends': [
        'base',
    ],
    'description': "",
    'data': [
        # Aqui van las rutas de las vistas del modulo, tambien la configuracion de Securidad
        #seguridad Course
        "security/ir.model.access.csv",
        #"data/data.xml"
        #Si importa el orden o secuencia de declarcion de las Vistas
        "views/course_views.xml",
        "views/session_views.xml",
        #Declaramos la vista heredada
        "views/res_partner_view.xml"
    ],
    'qweb': [
        # Aqui van las rutas de las vistas qweb

    ],
    "assets": {
        "web.assets_backend": [
            # Aqui van los assets como css, js del backend que son parte del modulo
        ],
    },
    'installable': True, 
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
