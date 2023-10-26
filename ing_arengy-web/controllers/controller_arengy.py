from odoo import http
from odoo.http import request
import logging
_log = logging.getLogger(__name__)

class WebArengy(http.Controller):

    @http.route(['/post/<model("product.template"):id_post>', '/post/<model("product.template"):id_post>/page/<int:page>'], auth='public', type='http', website=True, sitemap=True)
    def get_post(self, id_post,  page=0, **kwargs,):
        post_context = dict(request.env.context, active_id=id_post.id, partner=request.env.user.partner_id)
        post = id_post.with_context(post_context)
        kwargs.update({'id': id_post, 'main_object': post})
        domain = []
        cant = 3;


        #TODO:NUEVOS POST TRAIDOS DESDE PRODUCT.TEMPLATE

        pos = request.env['product.template'].sudo().search(domain)

        total_post = request.env['product.template'].sudo().search(domain)


        count = len(total_post)
        per_page =12

        pager = request.website.pager(url='/post', total=count, page= page, step=per_page, scope=3, url_args=None)

        _pos = request.env['product.template'].sudo().search(domain, limit=cant, offset=pager['offset'])
        values ={
         'list_post' : _pos,
            'pager': pager,
        }


        combined_values = {
            # **kwargs,  # kwargs
            # **values  # Valores adicionales
        }
        combined_values.update(values)
        combined_values.update(kwargs)


        return request.render('ing_arengy-web.page_post_inner',combined_values )



    @http.route('/cursos/<model("slide.channel"):id_curso>',auth='public', type='http', website=True, sitemap=True)

    def get_curso(self, id_curso,**kwargs,):
        curso_context = dict(request.env.context, active_id=id_curso.id, partner=request.env.user.partner_id)
        curso = id_curso.with_context(curso_context)
        kwargs.update({'id': id_curso, 'main_object': curso})
        domain = []
        cant = 12;

        # cursos = request.env['ing.curso'].sudo().search(domain, limit=cant)
        _cur = request.env['slide.channel'].sudo().search(domain, limit=cant)

        for rec in _cur:

            logging.info('---.---------------CUrso inner -------------------')
            logging.info(rec.name)



        values ={
            'curso_list': _cur
             }

        combined_values = {
            # **kwargs,  # kwargs
            # **values  # Valores adicionales
        }
        combined_values.update(values)
        combined_values.update(kwargs)




        return request.render('ing_arengy-web.page_curso_inner', combined_values)


    @http.route(['/solucion', '/solucion/page/<string:page>'], type='http', auth="public", website=True)

    def get_soluciones(self, page=0):
        domain = [('detailed_type', '=', 'service'), ('is_published', '=', True)]



        total_soluciones = request.env['product.template'].sudo().search(domain)
        total_count = len(total_soluciones)
        per_page = 12
        pager = request.website.pager(url='/solucion', total=total_count, page=page, step=per_page, scope=3, url_args=None)


        pos = request.env['product.template'].sudo().search(domain)

        for rec in pos:
            logging.info('--------------------------Soluciones ---------product template --------')
            logging.info(rec.name)

            logging.info(rec.description)




        _pos = request.env['product.template'].sudo().search(domain, limit=per_page, offset=pager['offset'])


        values = {
            'post_list': _pos,
            'pager': pager,
        }
        return request.render('ing_arengy-web.page_soluciones', values)




    @http.route(['/cursos', '/ver_mas','/cursos/page/<string:page>' ], type='http', auth="public", website=True)
    def get_cursos(self, page=0, cargar=False):
        domain = []

        total_cursos = request.env['slide.channel'].sudo().search(domain)
        total_count = len(total_cursos)
        per_page = 3



        #Todo: Nuevos cursos traidos desde e-learngin

        cur = request.env['slide.channel'].search(domain)
        participantes = cur.sudo().partner_ids

        if cargar == 'True':
            per_page = total_count



        pager = request.website.pager(url='/cursos', total=total_count, page=page, step=per_page, scope=2, url_args=None)
        _cur = request.env['slide.channel'].sudo().search(domain, limit=per_page, offset=pager['offset'])

        # _cursos = request.env['ing.curso'].sudo().search(domain, limit=per_page, offset=pager['offset'])


        values = {
            'cursos_list': _cur,
            'participantes_list': participantes,
            'pager': pager,

        }

        return request.render('ing_arengy-web.page_cursos', values)

    @http.route(['/novedades', '/mas'], type='http', auth="public", website=True)
    def get_novedades(self, page=0, cargar=False ):

        per_page = 3

        domain = []

        logging.info(per_page)

        total_novedades = request.env['blog.post'].sudo().search(domain)

        for rec in total_novedades:
            logging.info('--------------Novedades .-----------------------------')
            logging.info(rec.name)
            tag_names = rec.tag_ids.mapped('name')
            logging.info(tag_names)
            logging.info(rec.blog_id.name)




        total_count = len(total_novedades)

        if cargar == 'True':
            per_page = total_count






        pager = request.website.pager(url='/novedades', total=total_count, page=page, step=per_page, scope=3,
                                      url_args=None)

        _novedades = request.env['blog.post'].sudo().search(domain, limit=per_page, offset=pager['offset'])


        values = {
            'novedades_list': _novedades,
            'pager': pager,

        }

        return request.render('ing_arengy-web.page_novedades', values)

    @http.route('/novedades/<model("blog.post"):id_novedad>', auth='public', type='http', website=True, sitemap=True)
    def get_novedad(self, id_novedad, **kwargs, ):
        novedad_context = dict(request.env.context, active_id=id_novedad.id, partner=request.env.user.partner_id)
        curso = id_novedad.with_context(novedad_context)
        kwargs.update({'id': id_novedad, 'main_object': curso})
        domain = []
        cant = 3;

        novedades = request.env['blog.post'].sudo().search(domain, limit=cant)



        values = {
            'novedades_list': novedades
        }

        combined_values = {
            # **kwargs,  # kwargs
            # **values  # Valores adicionales
        }
        combined_values.update(values)
        combined_values.update(kwargs)

        return request.render('ing_arengy-web.page_novedades_inner', combined_values)






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
            domain = domain


        total_cursos = request.env['slide.channel'].sudo().search(domain)


        total_count = len(total_cursos)

        per_page = 3

        pager = request.website.pager(url='/filter', total=total_count, page=page, step=per_page, scope=3)

        _cursos= request.env['slide.channel'].sudo().search(domain, limit=per_page, offset=pager['offset'])


        values = {
            'cursos_list': _cursos,
            'pager': pager,

        }

        return request.render("ing_arengy-web.page_cursos", values)



    @http.route(['/filtro',  '/filtro/page/<int:page>'], type='http', auth="public",
                website=True)
    def post_filter(self, page=0,  moneda='', filtro=''):
        domain = [('detailed_type', '=', 'service'), ('is_published', '=', True)]

        if filtro != "":
            domain_filter=[('name', 'ilike', filtro)]
            domain = domain + domain_filter


        if moneda != "":
            domain_moneda = [('moneda', '=', moneda)]
            domain = domain_moneda

        total_post = request.env['product.template'].sudo().search(domain)


        total_count = len(total_post)

        per_page = 3

        pager = request.website.pager(url='/filtro' , total=total_count, page=page, step=per_page, scope=3)

        _post = request.env['product.template'].sudo().search(domain, limit=per_page, offset=pager['offset'])

        for rec in _post:
            logging.info('--------------------------------------Post name ----------------------------')
            logging.info(rec.name)
        values = {
            'post_list': _post,
            'pager': pager,

        }

        return request.render("ing_arengy-web.page_soluciones", values)