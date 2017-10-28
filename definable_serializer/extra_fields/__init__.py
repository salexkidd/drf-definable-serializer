"""
Copyright 2017 salexkidd

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from django.db.models.fields import BLANK_CHOICE_DASH
from rest_framework import serializers as rf_serializers
from rest_framework import fields as rf_fields
from copy import copy


class CheckRequiredField(rf_fields.BooleanField):
    """
    CheckRequiredField

    definable_serializer.extra_fields.CheckRequiredField
    """
    custom_error_messages = {
        'please_be_sure_to_turn_it_on': 'Please be sure to turn it on.'
    }

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if data == "" or data is None or data is False:
            self.fail('please_be_sure_to_turn_it_on')
        return data

    def __init__(self, *args, **kwargs):
        kwargs["style"] = {'base_template': 'checkbox.html',}
        super().__init__(*args, **kwargs)
        self.error_messages.update(self.custom_error_messages)


class MultipleCheckboxField(rf_fields.MultipleChoiceField):
    """
    MultipleCheckboxField

    definable_serializer.extra_fields.MultipleCheckboxField
    """

    custom_error_messages = {
        'this_field_is_required': 'This field is required.'
    }

    def __init__(self, *args, **kwargs):
        self.requred = kwargs.pop("required", False)
        kwargs["style"] = {
            'base_template': 'checkbox_multiple.html',
            'inline': kwargs.pop('inline', False)
        }

        super().__init__(*args, **kwargs)
        self.error_messages.update(self.custom_error_messages)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if self.requred and not len(data):
            self.fail('this_field_is_required')

        return data


class ChoiceWithBlankField(rf_fields.ChoiceField):
    """
    ChoiceWithBlankField

    definable_serializer.extra_fields.ChoiceWithBlankField
    """
    custom_error_messages = {
        'this_field_is_required': 'This field is required.'
    }

    def __init__(self, choices, *args, **kwargs):
        blank_choices = copy(BLANK_CHOICE_DASH)
        blank_label = kwargs.pop("blank_label", blank_choices[0][1])
        if blank_label:
            blank_choices = [["", blank_label],]

        choices = tuple(blank_choices + list(choices))

        super().__init__(choices, *args, **kwargs)
        self.error_messages.update(self.custom_error_messages)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if data == "" or data is None:
            self.fail('this_field_is_required')
        return data


class RadioField(rf_fields.ChoiceField):
    """
    RadioField

    definable_serializer.extra_fields.RadioField
    """
    def __init__(self, *args, **kwargs):
        kwargs["style"] = {
            'base_template': 'radio.html',
            'inline': kwargs.pop('inline', False)
        }
        super().__init__(*args, **kwargs)


class TextField(rf_fields.CharField):
    """
    TextField

    definable_serializer.extra_fields.TextField
    """
    def __init__(self, *args, **kwargs):
        kwargs["style"] = {
            'base_template': 'textarea.html',
            'rows': kwargs.pop('rows', 5),
            'placeholder': kwargs.pop('placeholder', "")
        }

        super().__init__(*args, **kwargs)
