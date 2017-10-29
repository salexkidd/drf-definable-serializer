.. _`install`:

==============================================================================
インストール方法
==============================================================================


パッケージのインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

以下のコマンドを実行してインストールしてください::

    pip install --upgrade restframework-definable-serializer


.. warning::

    もしdjangoとrestframeworkがインストールされていない場合は先にインストールを行ってください::

        pip install --upgrade django djangorestframework


INSTALLED_APPSへの追加
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

settings.py中にある ``INSTALLED_APPS`` に ``codemirror2`` と ``definable_serializer`` を追加してください。::

    INSTALLED_APPS = (
        ...
        'rest_framework',
        'codemirror2',
        'definable_serializer',
    )