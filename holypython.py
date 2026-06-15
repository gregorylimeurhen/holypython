import io
import pathlib
import re
import sys
import token
import tokenize

def get_path():
	arg = sys.argv[1]
	path = pathlib.Path(arg).resolve()
	return path

def get_source(path):
	with tokenize.open(path) as source_file:
		source = source_file.read()
	return source

def get_tokens(source):
	text = io.StringIO(source)
	reader = text.readline
	iterator = tokenize.generate_tokens(reader)
	tokens = list(iterator)
	return tokens

class VariableAssignmentEditor:
	def __init__(self, source):
		self.tokens = get_tokens(source)

	def edit_source(self):
		edited = []
		i = 0
		while i < len(self.tokens):
			t = self.tokens[i]
			if i + 1 < len(self.tokens):
				next_t = self.tokens[i + 1]
				if t.string == "<" and next_t.string == "-" and t.end == next_t.start:
					edited.append(t._replace(string="=", end=next_t.end))
					i += 2
					continue
			edited.append(t)
			i += 1
		source = tokenize.untokenize(edited)
		return source

class FunctionDefinitionEditor:
	def __init__(self, source):
		self.tokens = get_tokens(source)

	def edit_source(self):
		edited = []
		for t in self.tokens:
			if t.type == token.NAME and t.string == "function":
				edited.append(t._replace(string="def"))
				continue
			edited.append(t)
		source = tokenize.untokenize(edited)
		return source

class EqualityCheckEditor:
	def __init__(self, source):
		self.source = source
		self.tokens = get_tokens(source)
		self.columns = [match.start() for match in re.finditer(r"(?m)^", self.source)]

	def edit_source(self):
		edited = []
		for t in self.tokens:
			if t.string == "=" and self.is_spaced(t):
				edited.append(t._replace(string="=="))
				continue
			edited.append(t)
		source = tokenize.untokenize(edited)
		return source

	def get_offset(self, position):
		row, column = position
		offset = self.columns[row - 1] + column
		return offset

	def is_spaced(self, t):
		start = self.get_offset(t.start)
		end = self.get_offset(t.end)
		return self.source[start - 1].isspace() and self.source[end].isspace()

def write_script(source, path):
	output_path = path.with_suffix(".py")
	output_path.write_text(source)

if __name__ == "__main__":
	path = get_path()
	source = get_source(path)
	source = EqualityCheckEditor(source).edit_source()
	source = FunctionDefinitionEditor(source).edit_source()
	source = VariableAssignmentEditor(source).edit_source()
	write_script(source, path)
