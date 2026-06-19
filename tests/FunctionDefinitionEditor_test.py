import snekscript
import utils

def test_edit_function():
	source = """
function add(a, b):
	return a + b

result = add(2, 3)
"""
	namespace = utils.run_source(snekscript.FunctionDefinitionEditor, source)
	assert namespace["result"] == 5
