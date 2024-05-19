import sublime
import sublime_plugin
import re


class TocamelCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		p = re.compile(r"_(?P<idx>.)")
		def toCamel(t) :
			return p.sub( lambda m : m.group('idx').upper(), t)

		for selection in self.view.sel() :
			text = self.view.substr(selection)
			t = text.lower()
			self.view.replace(edit, selection, toCamel(t))



	# @classmethod
	# def toC(m) :
	# 	val = m.group('idx')
	# 	return val.upper()

