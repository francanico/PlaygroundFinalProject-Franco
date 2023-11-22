from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("IturbeSeguros/", views.index, name= "IturbeSeguros"),
    path("polizas/",views.poliza, name= "poliza"),
    path("polizasview/",views.Polizalistviewt.as_view(), name= "polizasview"),
    path("polizas/crearpoliza/",views.form_poliza, name="crear_poliza"),
    path("buscadorpolizas/",views.buscador, name="buscador"),
    path("polizas/editar_poliza/<int:pk>",views.Polizaupteview.as_view(), name="editar_poliza"),
    path("polizas/eliminar_poliza/<int:pk>",views.PolizaDelete.as_view(), name="eliminar_poliza"),

    path("auto/",views.auto, name="auto"),
    path("autoview/",views.Autoview.as_view(), name="autoview"),
    path("auto/editar_auto/<int:pk>",views.autoupdate.as_view(), name="editar_auto"),
    path("auto/eliminar_auto/<int:pk>",views.Autodelete.as_view(), name="eliminar_auto"),
    path("auto/crearauto/",views.form_auto, name="crear_auto"),
    path("buscadorauto/",views.buscar_auto, name="buscarauto"),

    path("Miperfil/",views.Perfil,name= "perfil"),
    path("Miperfil/editar/",views.imagenavatar, name= "editar_perfil"),

    path("Miperfil/cambiopassword/",views.CambioPassword.as_view(),name= "changepass"),
    path("Miperfil/cambiopassword/CambioExitoso/",views.password_exitoso,name= "passcambiadoexitoso"),

    path("",views.user_login, name= "user_login"),
    path("registro/",views.user_register, name= "registro"),
    path("logout/",views.user_logout, name= "user_logout"),

    path("Contacto/",views.contactoview, name= "Contacto"), 
    path("Contacto/FormEnviadoExitosamente",views.envioform1, name= "envioform"),
    path("AcercadeMi/",views.acercademi, name= "acercademi"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)