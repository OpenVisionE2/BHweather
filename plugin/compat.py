# -*- coding: utf-8 -*-
#Codes for Taapat (Youtube plugin)

from re import compile
from six.moves.urllib.parse import urlencode as compat_urlencode
from six.moves.urllib.parse import quote as compat_quote
from six.moves.urllib.parse import unquote_to_bytes as compat_unquote_to_bytes
from six.moves.urllib.request import urlopen as compat_urlopen
from six.moves.urllib.request import Request as compat_Request
from six.moves.urllib.error import URLError as compat_URLError
from six.moves.urllib.parse import urljoin as compat_urljoin
from six.moves.urllib.parse import urlparse as compat_urlparse
from six import PY3

if PY3:
	# Python 3
	compat_str = str
else:
	# Python 2
	compat_str = unicode

try:
	import ssl
	sslContext = ssl._create_unverified_context()
except:
	sslContext = None


def _parse_qsl(qs):
	qs, _coerce_result = qs, compat_str
	pairs = [s2 for s1 in qs.split('&') for s2 in s1.split(';')]
	r = []
	for name_value in pairs:
		if not name_value:
			continue
		nv = name_value.split('=', 1)
		if len(nv) != 2:
			# Handle case of a control-name with no equal sign
			continue
		if len(nv[1]):
			name = nv[0].replace('+', ' ')
			name = compat_urllib_parse_unquote(name)
			name = _coerce_result(name)
			value = nv[1].replace('+', ' ')
			value = compat_urllib_parse_unquote(value)
			value = _coerce_result(value)
			r.append((name, value))
	return r


def compat_parse_qs(qs):
	parsed_result = {}
	pairs = _parse_qsl(qs)
	for name, value in pairs:
		if name in parsed_result:
			parsed_result[name].append(value)
		else:
			parsed_result[name] = [value]
	return parsed_result


def compat_ssl_urlopen(url):
	if sslContext:
		return compat_urlopen(url, context=sslContext)
	else:
		return compat_urlopen(url)


def compat_urllib_parse_unquote(string):
	if '%' not in string:
		string.split
		return string
	bits = compile(r'([\x00-\x7f]+)').split(string)
	res = [bits[0]]
	append = res.append
	for i in range(1, len(bits), 2):
		append(compat_unquote_to_bytes(bits[i]).decode('utf-8', 'replace'))
		append(bits[i + 1])
	return ''.join(res)
