from setuptools import setup, find_packages
import definable_serializer

try:
    with open("README.md") as f:
        long_description = f.read()

except Exception as e:
    long_description = ""

setup(
    name='restframework-definable-serializer',
    author = "salexkidd",
    author_email = "salexkidd@gmail.com",
    url = "https://github.com/salexkidd/restframework-definable-serializer",
    description='restframework-definable-serializer',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords = ["django", "restframework", "serializer"],
    version=definable_serializer.__VERSION__,
    packages=find_packages(
        exclude=[
            "*.tests", "*.tests.*", "tests.*", "tests",
        ]
    ),
    package_data={
        'definable_serializer': [
            'templates/admin/definable_serializer/*.html',
            'LICENSE'
        ]},
    license="MIT",
    install_requires=[
        "django-codemirror2>=0.2",
        "jsonfield2>=3.0.3",
        "django-yamlfield>=1.0.3",
        "PyYAML>=5.2",
        "ruamel.yaml>=0.13.5",
        "simplejson>=3.11.1",
        "six>=1.13.0",
        "dateparser==0.7.2",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
