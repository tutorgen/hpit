from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from core.api import *

v1_api = Api(api_name='v1')
v1_api.register(StudentResource())
v1_api.register(StudentAttributeResource())
v1_api.register(TutorResource())
v1_api.register(QuestionResource())
v1_api.register(QuestionStepResource())
v1_api.register(QuestionSkillResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hpit_shell.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    (r'^api/', include(v1_api.urls)),

    #url(r'^student/$', 'core.views.create_student'),
    #url(r'^student/(?P<id>\w+)/$', 'core.views.student'),
    #url(r'^student/(?P<id>\w+)/attribute/$', 'core.views.student_attribute'),
    #url(r'^student/(?P<id>\w+)/attribute/(?P<name>[\w\-?]+)/$', 'core.views.student_attribute_name'),
    #url(r'^student/(?P<id>\w+)/question/(?P<question_id>\d+)/hint/$', 'core.views.student_question_hint'),
    #url(r'^student/(?P<id>\w+)/question/(?P<question_id>\d+)/next/$', 'core.views.student_question_next'),

    url(r'', 'core.views.index'),
)
