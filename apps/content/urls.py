from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('content.views',
  url(r'^create/$', 'create_page', name='page_create'),
  url(r'^index/(?P<counter>\d+)/up/$', 'page_index_up',
      name='page_index_up'),
  url(r'^index/(?P<counter>\d+)/down/$', 'page_index_down',
      name='page_index_down'),
  url(r'^(?P<page_slug>[\w-]+)/$', 'show_page', name='page_show'),
  url(r'^(?P<page_slug>[\w-]+)/edit/$', 'edit_page', name='page_edit'),
  url(r'^(?P<page_slug>[\w-]+)/delete/$', 'delete_page', name='page_delete'),
  url(r'^(?P<page_slug>[\w-]+)/history/$', 'history_page',
      name='page_history'),
  url(r'^(?P<page_slug>[\w-]+)/history/(?P<version_id>\d+)/$',
      'version_page', name='page_version'),
  url(r'^(?P<page_slug>[\w-]+)/history/(?P<version_id>\d+)/restore/$',
      'restore_version', name='version_restore'),
)
