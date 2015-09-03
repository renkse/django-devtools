# coding=utf-8
__author__ = 'renkse'

from django.core.exceptions import ValidationError
import re


# валидатор размера картинки
def is_valid_size(weight=3000000, errorstr='3МБ'):
    def innerfn(image_field):
        if image_field._get_size() > weight:  # in bytes
            raise ValidationError, "Размер файла не должен превышать {0}".format(errorstr)
    return innerfn


def rus_verification(self, variable, var_name_str):
    if variable is not None:
            regexp = re.compile(ur'^[а-яА-ЯёЁ ]{2,100}$')
            verified_str = regexp.match(variable)
            if not verified_str:
                self._errors[var_name_str] = self.error_class([u'Только русские буквы.'])


def phone_verification(self, variable, var_name_str):
    if variable is not None:
        regexp = re.compile(ur'^[0-9+() -]+$')
        verified_str = regexp.match(variable)
        if not verified_str:
            self._errors[var_name_str] = self.error_class([u'В номере телефона допустимы только цифры, пробелы и '
                                                           u'символы: "+", "-", "(", ")".'])