from django.forms.utils import ValidationError
from django.utils.translation import ugettext_lazy as _

from ..serializers import build_serializer

from copy import deepcopy
from codemirror2.widgets import CodeMirrorEditor
from jsonfield.fields import JSONField
from .compat import YAMLField

import json
from jsonfield import utils as jsonfield_utils


_CODE_MIRROR_OPTION = {
    "options": {
        'lineNumbers': True,
        'tabSize': 2,
        'indentUnit': 2,
        'indentWithTabs': False,
        'theme': "monokai",
        'lineWrapping': True
    },
    "themes": ["monokai"],
    "script_template": "admin/definable_serializer/codemirror_script.html",
}

_CODE_MIRROR_OPTION_FOR_JSON = deepcopy(_CODE_MIRROR_OPTION)
_CODE_MIRROR_OPTION_FOR_YAML = deepcopy(_CODE_MIRROR_OPTION)

_CODE_MIRROR_OPTION_FOR_JSON["options"]["mode"] = "javascript"
_CODE_MIRROR_OPTION_FOR_YAML["options"]["mode"] = "yaml"


__all__ = (
    "AbstractDefinableSerializerField",
    "DefinableSerializerByJSONField",
    "DefinableSerializerByYAMLField",
)


class AbstractDefinableSerializerField:
    def clean(self, value, *args, **kwargs):
        try:
            cleaned_data = super().clean(value, *args, **kwargs)
            build_serializer(cleaned_data)

        except Exception as except_obj:
            raise ValidationError("Invalid Format!: {}".format(except_obj))

        return cleaned_data


class CodeMirrorWidgetForJSON(CodeMirrorEditor):
    def render(self, name, value, attrs=None, **kwargs):

        if isinstance(value, dict):
            value = json.dumps(
                value, ensure_ascii=False, indent=2, default=jsonfield_utils.default)
        else:
            value.replace(r"\r\n", r"\n")

        return super().render(name, value, attrs=attrs, **kwargs)
    ...


class DefinableSerializerByJSONField(AbstractDefinableSerializerField, JSONField):
    def formfield(self, **kwargs):
        kwargs["widget"] = CodeMirrorWidgetForJSON(**_CODE_MIRROR_OPTION_FOR_JSON)
        return super().formfield(**kwargs)


class DefinableSerializerByYAMLField(AbstractDefinableSerializerField, YAMLField):
    def formfield(self, **kwargs):
        kwargs["widget"] = CodeMirrorEditor(**_CODE_MIRROR_OPTION_FOR_YAML)
        return super().formfield(**kwargs)
