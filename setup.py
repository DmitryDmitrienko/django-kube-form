from setuptools import setup
from kubeform import VERSION


setup(
    name='kubeform',
    version='.'.join(map(str, VERSION)),
    author='Dmitry Dmitrienko',
    author_email='dmitry.dmitrienko@outlook.com',
    packages=['kubeform'],
    url='https://github.com/DmitryDmitrienko/django-kube-form',
    license='See LICENSE',
    description='Reusable Django app for display kube forms',
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    include_package_data=True
)