# -*- coding: utf-8 -*-
{
    'name': "web_arengy",
    'summary': """Web arengy""",
    'description': """
        Modulo web arengy
    """,
    'author': "Ingenio Solutions",
    'website': "http://www.ingeniosolutions.com.ar",
    'category': 'Uncategorized',
    'assets': {
        'web.assets_frontend': [
            'ing_arengy-web/static/style.css',
            'https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap'
        ],

        'web.assets_backend': [
            'https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap'
        ],
    },
    'version': '1',
    'depends': ['base','website'],
    'data': [
        # Security
        'security/security.xml',
        'security/ir.model.access.csv',
        # MENUES
        # 'views/menu.xml',

        # Views

        'views/footer_custom_inherit.xml',
        'views/post.xml',
        'views/menu.xml',
        'views/novedad.xml',

        'views/cursos.xml',



        #Pages

        'views/pages/web_home.xml',
         'views/pages/web_contacto.xml',
         'views/pages/web_soluciones.xml',
         'views/pages/web_post_inner.xml',
         'views/pages/web_cursos.xml',
         'views/pages/web_curso_inner.xml',
         'views/pages/web_calidad.xml',
         'views/pages/web_novedades.xml',
         'views/pages/web_novedades_in.xml',


    ],
    'installable': True,
    'auto_install': False,
}

