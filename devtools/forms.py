# coding=utf-8
__author__ = 'renkse'

from django import forms
from django.forms.models import BaseInlineFormSet


class AtLeastOneRequiredInlineFormSet(BaseInlineFormSet):

    def clean(self):
        """Check that at least one service has been entered."""
        super(AtLeastOneRequiredInlineFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False) for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('Прикрепите не менее одного документа')
