.. _`model_fields`:

==============================================================================
提供するモデルフィールドクラス
==============================================================================

definable-serializerではシリアライザーを記述するためのフィールドと、
ユーザーからの入力データを保存するためのフィールドを提供しています。


.. _`definable-serializer-fields`:

シリアライザーの定義を保存するモデルフィールド
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

definable-serializerでは、JSON及びYAMLで記述された文字列及びファイルからシリアライザーを作ることができます。
特にadmin画面でシリアライザーを記述することで、デプロイの手間を緩和するのが目的です。
admin画面でテキストデータの編集を行うのは難しい話ではないものの、YAMLやJSON定義をハイライト無しで記述するのはちょっとした苦行です。

この問題を解決するために、CodeMirror2ウィジェットを利用してハイライトサポートを行う
2つのシリアライザー定義用のフィールドを用意しています。


.. _`definable_serializer_by_yaml_field_class`:

DefinableSerializerByYAMLField
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

DefinableSerializerByYAMLFieldはdjango-yamlfield
`(https://github.com/datadesk/django-yamlfield) <https://github.com/datadesk/django-yamlfield>`_ が
提供するYAMLFieldをラップし、CodeMirror2ウィジェット及び非ASCII文字が正しく表示することができます。

以下に使用例を示します。


.. code-block:: python

    class Survey(models.Model):
        ..

        question = DefinableSerializerByYAMLField()

.. figure:: imgs/codemirror2_with_yaml.png


.. _`definable_serializer_by_json_field_class`:

DefinableSerializerByJSONField
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

DefinableSerializerByJSONFieldは
jsonfield `(https://github.com/dmkoch/django-jsonfield) <https://github.com/dmkoch/django-jsonfield>`_ が
提供するJSONFieldをラップし、CodeMirror2ウィジェット及び非ASCII文字が正しく表示することができます。

以下に使用例を示します。


.. code-block:: python

    class Survey(models.Model):
        ..

        question = DefinableSerializerByJSONField()

.. figure:: imgs/codemirror2_with_json.png


------------------------------------------------------------------------------


.. _`methods-of-storing-input-data`:

ユーザーからの入力データを保存するモデルフィールド
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`storing-input-data` でも取り上げたように、モデルに結びつかないシリアライザーにユーザーから
渡されてバリデーションが完了したデータを永続的に保存するには、保存情報を扱うモデルの単一のフィールドに
シリアライズ(直列化)された状態でデータを保存します。

ようはPythonのネイティブなデータをテキストやバイナリに変換してデータベースのカラムにさえ保存できれば
どんな形でも構いません。データのシリアライズによく用いられるのが JSON, YAMLです。

definable-serializerではユーザーからの入力を保存するために2つのモデルフィールドを用意しています。


.. _`compat_json_field`:

JSONField
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

JSONは非常に人気の高いシリアライズの形式です。

しかし、Pythonに付随するJSONEncoderにはPythonのネイティブなデータである ``set型`` を
シリアライズすることができません。

また正しく設定を行わないと非ASCII文字を"\\uXXXX"で表すため、入力情報を確認すると見苦しい状態になります。

definable-serializerでは、 `jsonfield <https://github.com/dmkoch/django-jsonfield>`_
が提供するJSONFieldをラップし、この2つの問題を解消するコンパチビリティクラスを用意しています。

以下に使用例を示します。


.. code-block:: python

    from definable_serializer.models.compat import JSONField as CompatJSONField

    class Answer(models.Model):

        ..

        answer = CompatJSONField(
            verbose_name="answer data",
            help_text="answer data"
        )


このモデルフィールドを使うとadmin画面で以下のように表示されます。


.. figure:: imgs/compat_json_field.png

    非ASCII文字列が正しく表示されます


YAMLField
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

YAMLはJSONと同様、テキストでデータシリアライズします。記号が少なくインデントでデータ構造を表すため、
Pythonのコードのように美しく、可読性に優れます。

definable-serializerでは、 django-yamlfield `(https://github.com/datadesk/django-yamlfield) <https://github.com/datadesk/django-yamlfield>`_
が提供するYAMLFieldをラップし、非ASCII文字が正しく表示されるコンパチビリティクラスを用意しています。

以下に使用例を示します。


.. code-block:: python

    from definable_serializer.models.compat import YAMLField as CompatYAMLField

    class Answer(models.Model):

        ..

        answer = CompatYAMLField(
            verbose_name="answer data",
            help_text="answer data"
        )

.. figure:: imgs/compat_yaml_field.png
    :scale: 40

    非ASCII文字列が正しく表示されます