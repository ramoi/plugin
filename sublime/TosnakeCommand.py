import sublime
import sublime_plugin
import re


class TosnakeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		p = re.compile(r"(?P<idx>[A-Z])")
		def toSnake(t) :
			return p.sub( lambda m : '_' + m.group('idx').lower(), t)

		fp = re.compile(r"^(?P<idx>[A-Z])")

		for selection in self.view.sel() :
			text = self.view.substr(selection)
			t = fp.sub( lambda m : m.group('idx').lower(), text)
			self.view.replace(edit, selection, toSnake(t))
