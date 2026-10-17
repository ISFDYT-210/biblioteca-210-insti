from django.conf import settings


class NoCacheMiddleware:
    """
    Evita que proxies compartidos (ej. el de la red de la facultad) o el
    navegador guarden copias de las páginas dinámicas del sitio.

    Sin esto, un proxy de red puede cachear una respuesta (ej. la pantalla
    principal con datos de un usuario logueado) y servirla tal cual a otra
    persona que pida la misma URL desde esa red, o simplemente quedarse con
    una versión vieja del sitio después de un deploy. Los archivos estáticos
    (CSS/JS/imágenes), servidos por WhiteNoise con nombres con hash de
    contenido, no se tocan: esos sí conviene que se cacheen.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not request.path.startswith(settings.STATIC_URL):
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response['Pragma'] = 'no-cache'

        return response
