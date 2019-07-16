from distutils.core import setup
import setup_translate

pkg = 'Extensions.BHweather'
setup (name = 'enigma2-plugin-extensions-bhweather',
       version = '0.6',
       description = 'Plugin to weather.',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg: ['*/*.png', 'locale/*/LC_MESSAGES/*.mo', 'weather/*.png', 'weather/*/*.png', 'weather/fhd/small/*.png']},
       cmdclass = setup_translate.cmdclass, # for translation
      )
