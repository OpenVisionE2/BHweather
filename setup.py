# -*- coding: utf-8 -*-
from distutils.core import setup
import setup_translate

pkg = 'Extensions.BhWeather'
setup (name = 'enigma2-plugin-extensions-bhweather',
       version = '0.6',
       description = 'Black Hole weather plugin.',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg: ['*/*.png', 'locale/*/LC_MESSAGES/*.mo', 'weather/*.png', 'weather/*/*.png', 'weather/fhd/small/*.png']},
       cmdclass = setup_translate.cmdclass, # for translation
      )
