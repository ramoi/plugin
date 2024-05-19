import sublime
import sublime_plugin


class NumberingCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		i = 1
		for selection in self.view.sel() :
			self.view.insert(edit, selection.begin(), str(i) )
			i = i + 1

