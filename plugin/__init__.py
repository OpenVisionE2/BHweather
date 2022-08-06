# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import os
import gettext


def localeInit():
	lang = language.getLanguage()[:2] # getLanguage returns e.g. "fi_FI" for "language_country"
	os.environ["LANGUAGE"] = lang # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
	gettext.bindtextdomain("BhWeather", resolveFilename(SCOPE_PLUGINS, "Extensions/BhWeather/locale"))


def _(txt):
	t = gettext.dgettext("BhWeather", txt)
	if t == txt:
		print("[BhWeather] fallback to default translation for", txt)
		t = gettext.gettext(txt)
	return t


localeInit()
language.addCallback(localeInit)
