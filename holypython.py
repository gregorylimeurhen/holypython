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


class AssignmentEditor:
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


class BlockEditor:
	def __init__(self, source):
		self.lines = source.splitlines(keepends=True)

	def edit_source(self):
		edited = []
		for i, line in enumerate(self.lines):
			stripped = line.strip()
			if stripped == "{":
				continue
			if stripped == "}":
				continue
			if i + 1 < len(self.lines):
				if self.lines[i + 1].strip() == "{" and self.is_header(stripped):
					line = self.edit_header_line(line)
			edited.append(line)
		source = "".join(edited)
		return source

	def edit_header_line(self, line):
		newline = "\n" if line.endswith("\n") else ""
		source = line[:-1] if newline else line
		indent = source[:len(source) - len(source.lstrip())]
		header = source.strip()
		if header.startswith("class ") and " extends " in header:
			name, parent = header[len("class "):].split(" extends ", 1)
			header = f"class {name}({parent})"
		return f"{indent}{header}:{newline}"

	def is_header(self, source):
		if source.startswith("async "):
			source = source[len("async "):]
		return source.startswith("class ") or source.startswith("function ")


class DefEditor:
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


class EqualityEditor:
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


class RangeEditor:
	def __init__(self, source):
		self.source = source
		self.tokens = get_tokens(source)
		self.columns = [match.start() for match in re.finditer(r"(?m)^", self.source)]

	def edit_source(self):
		edited = []
		source_offset = 0
		i = 0
		while i < len(self.tokens):
			t = self.tokens[i]
			if t.string != "[":
				i += 1
				continue
			result = self.find_split(i)
			if result is None:
				i += 1
				continue
			j, split = result
			start_offset = self.get_offset(t.start)
			end_offset = self.get_offset(self.tokens[j].end)
			left_start_offset = self.get_offset(t.end)
			left_end_offset = self.get_offset(split[0])
			right_start_offset = self.get_offset(split[1])
			right_end_offset = self.get_offset(self.tokens[j].start)
			left_source = RangeEditor(
				self.source[left_start_offset:left_end_offset]
			).edit_source()
			right_source = RangeEditor(
				self.source[right_start_offset:right_end_offset]
			).edit_source()
			edited.append(self.source[source_offset:start_offset])
			edited.append(f"list(range({left_source}, {right_source} + 1))")
			source_offset = end_offset
			i = j + 1
		edited.append(self.source[source_offset:])
		source = "".join(edited)
		return source

	def find_split(self, start_index):
		bracket_depth = 1
		paren_depth = 0
		split = None
		for j in range(start_index + 1, len(self.tokens)):
			t = self.tokens[j]
			if t.string == "[":
				bracket_depth += 1
			elif t.string == "]":
				bracket_depth -= 1
				if bracket_depth == 0:
					if split is None:
						return None
					return j, split
			elif bracket_depth == 1:
				if t.string == "(":
					paren_depth += 1
				elif t.string == ")":
					paren_depth -= 1
				elif split is None:
					if paren_depth == 0:
						if j + 1 < len(self.tokens):
							split = self.get_split(t, self.tokens[j + 1])
		return None

	def get_offset(self, position):
		row, column = position
		offset = self.columns[row - 1] + column
		return offset

	def get_split(self, left_token, right_token):
		if left_token.string == ".":
			left_dot = left_token.start
		elif left_token.type == token.NUMBER and left_token.string.endswith("."):
			left_dot = (left_token.end[0], left_token.end[1] - 1)
		else:
			return None
		if right_token.string == ".":
			right_dot = right_token.end
		elif right_token.type == token.NUMBER and right_token.string.startswith("."):
			right_dot = (right_token.start[0], right_token.start[1] + 1)
		else:
			return None
		return left_dot, right_dot


def write_script(source, path):
	output_path = path.with_suffix(".py")
	output_path.write_text(source)


if __name__ == "__main__":
	path = get_path()
	source = get_source(path)
	source = BlockEditor(source).edit_source()
	source = EqualityEditor(source).edit_source()
	source = AssignmentEditor(source).edit_source()
	source = RangeEditor(source).edit_source()
	source = DefEditor(source).edit_source()
	write_script(source, path)
