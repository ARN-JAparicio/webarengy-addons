from odoo import http
from odoo.http import request
import logging
_log = logging.getLogger(__name__)

class WebArengy(http.Controller):

    @http.route(['/post/<model("ing.post"):id_post>', '/post/<model("ing.post"):id_post>/page/<int:page>'], auth='public', type='http', website=True, sitemap=True)
    def get_post(self, id_post,  page=0, **kwargs,):
        post_context = dict(request.env.context, active_id=id_post.id, partner=request.env.user.partner_id)
        post = id_post.with_context(post_context)
        kwargs.update({'id': id_post, 'main_object': post})
        domain = []
        cant = 3;

        total_post = request.env['ing.post'].sudo().search(domain)
        count = len(total_post)
        per_page =12

        pager = request.website.pager(url='/post', total=count, page= page, step=per_page, scope=3, url_args=None)

        posts = request.env['ing.post'].sudo().search(domain, limit=cant, offset=pager['offset'])
        values ={
         'list_post' : posts,
            'pager': pager,
        }


        combined_values = {
            # **kwargs,  # kwargs
            # **values  # Valores adicionales
        }
        combined_values.update(values)
        combined_values.update(kwargs)


        return request.render('website.inner-post',combined_values )



    @http.route('/cursos/<model("ing.curso"):id_curso>',auth='public', type='http', website=True, sitemap=True)

    def get_curso(self, id_curso,**kwargs,):
        curso_context = dict(request.env.context, active_id=id_curso.id, partner=request.env.user.partner_id)
        curso = id_curso.with_context(curso_context)
        kwargs.update({'id': id_curso, 'main_object': curso})
        domain = []
        cant = 12;

        cursos = request.env['ing.curso'].sudo().search(domain, limit=cant)

        values ={
            'curso_list': cursos
             }

        combined_values = {
            # **kwargs,  # kwargs
            # **values  # Valores adicionales
        }
        combined_values.update(values)
        combined_values.update(kwargs)




        return request.render('website.inner-curso', combined_values)


    @http.route(['/solucion', '/solucion/page/<string:page>'], type='http', auth="public", website=True)

    def get_soluciones(self, page=0):
        domain = []

        total_soluciones = request.env['ing.post'].sudo().search(domain)
        total_count = len(total_soluciones)
        per_page = 12
        pager = request.website.pager(url='/solucion', total=total_count, page=page, step=per_page, scope=3, url_args=None)


        posts = request.env['ing.post'].sudo().search(domain, limit=per_page, offset=pager['offset'])


        values = {
            'post_list': posts,
            'pager': pager,
        }
        return request.render('ing_arengy-web.page_soluciones', values)




    @http.route(['/cursos', '/ver_mas','/cursos/page/<string:page>' ], type='http', auth="public", website=True)
    def get_cursos(self, page=0, cargar=False):
        domain = []

        total_cursos = request.env['ing.curso'].sudo().search(domain)
        total_count = len(total_cursos)
        per_page = 3


        if cargar == 'True':
            per_page = total_count



        pager = request.website.pager(url='/cursos', total=total_count, page=page, step=per_page, scope=3, url_args=None)


        _cursos = request.env['ing.curso'].sudo().search(domain, limit=per_page, offset=pager['offset'])


        values = {
            'cursos_list': _cursos,
            'pager': pager,

        }

        return request.render('ing_arengy-web.page_cursos', values)

    @http.route(['/novedades', '/mas'], type='http', auth="public", website=True)
    def get_novedades(self, page=0, cargar=False ):

        per_page = 3

        domain = []
        logging.info('--------------PER PAGE ........................')

        logging.info(per_page)

        total_novedades = request.env['ing.novedad'].sudo().search(domain)
        total_count = len(total_novedades)

        if cargar == 'True':
            per_page = total_count





        pager = request.website.pager(url='/novedades', total=total_count, page=page, step=per_page, scope=3,
                                      url_args=None)

        _novedades = request.env['ing.novedad'].sudo().search(domain, limit=per_page, offset=pager['offset'])


        values = {
            'novedades_list': _novedades,
            'pager': pager,

        }

        return request.render('ing_arengy-web.page_novedades', values)

    @http.route('/novedades/<model("ing.novedad"):id_novedad>', auth='public', type='http', website=True, sitemap=True)
    def get_novedad(self, id_novedad, **kwargs, ):
        novedad_context = dict(request.env.context, active_id=id_novedad.id, partner=request.env.user.partner_id)
        curso = id_novedad.with_context(novedad_context)
        kwargs.update({'id': id_novedad, 'main_object': curso})
        domain = []
        cant = 3;

        novedades = request.env['ing.novedad'].sudo().search(domain, limit=cant)

        values = {
            'novedades_list': novedades
        }

        combined_values = {
            # **kwargs,  # kwargs
            # **values  # Valores adicionales
        }
        combined_values.update(values)
        combined_values.update(kwargs)

        return request.render('website.inner-nov', combined_values)






######FILTROS #################


    @http.route(['/filter' , '/filter/page/<int:page>'], type='http', auth="public", website=True)
    def cursos_filter(self, page=0, tipo='', filter=''):

        domain = []


        if filter != "":
            domain_filter=[('name', 'ilike', filter)]
            domain = domain_filter
            logging.info('------------------entrando en filtro ------------')

        if tipo != "":
            logging.info('-------------Entrando en tipo ------------')
            domain_tipo = [('tipo', '=', tipo)]
            domain = domain_tipo


        total_cursos = request.env['ing.curso'].sudo().search(domain)



        total_count = len(total_cursos)

        per_page = 3

        pager = request.website.pager(url='/filter', total=total_count, page=page, step=per_page, scope=3)

        _cursos= request.env['ing.curso'].sudo().search(domain, limit=per_page, offset=pager['offset'])


        values = {
            'cursos_list': _cursos,
            'pager': pager,

        }

        return request.render("ing_arengy-web.page_cursos", values)



    @http.route(['/filtro',  '/filtro/page/<int:page>'], type='http', auth="public",
                website=True)
    def post_filter(self, page=0,  moneda='', filtro=''):
        domain = []

        if filtro != "":
            domain_filter=[('name', 'ilike', filtro)]
            domain = domain_filter


        if moneda != "":
            domain_moneda = [('moneda', '=', moneda)]
            domain = domain_moneda

        total_post = request.env['ing.post'].sudo().search(domain)


        total_count = len(total_post)

        per_page = 3

        pager = request.website.pager(url='/filtro' , total=total_count, page=page, step=per_page, scope=3)

        _post = request.env['ing.post'].sudo().search(domain, limit=per_page, offset=pager['offset'])

        for rec in _post:
            logging.info('--------------------------------------Post name ----------------------------')
            logging.info(rec.name)
        values = {
            'post_list': _post,
            'pager': pager,

        }

        return request.render("ing_arengy-web.page_soluciones", values)