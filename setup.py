#########################################################################
#
# Copyright (C) 2014 Starter Kit Development Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################


from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='starterkit',
    version=__import__('geosk').get_version(),
    description="starterkit, based on GeoNode",
    long_description=long_description,
    url='https://github.com/SP7-Ritmare/starterkit',
    author='Starter Kit Development Team',
    author_email='help.skritmare@irea.cnr.it',
    license="GPL3",
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
    ],
    keywords="StarterKit GeoNode Django sensors SOS",
    packages=find_packages(),
    install_requires=[
    "django-overextends",
    "django-annoying",
    "django-rosetta",
    "django-grappelli==2.4.10",
    "djproxy",
    "Django==1.5.5" # required by GeoNode 2.0
    ],
    # 
    include_package_data = True,
    # exclude_package_data = {'': ['.gitignore', ],
    #                         'geosk': ['local_settings.py'],
    #                         # 'model': ['config.py']
    #                         },
    setup_requires = [ "setuptools_git >= 0.3", ],

)

