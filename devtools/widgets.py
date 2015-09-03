__author__ = 'renkse'

# from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe


class AdminImageWidget(AdminFileWidget):
    """
    A ImageField Widget for admin that shows a thumbnail.
    """
    height = 100

    def __init__(self, attrs=None, height=None):
        if height:
            self.height = height
        if attrs is None:
            attrs = {}
        super(AdminImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<a target="_blank" href="%s">'
                           '<img src="%s" style="height: %dpx;" /></a>'
                           % (value.url, value.url, self.height)))
        output.append(super(AdminImageWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))