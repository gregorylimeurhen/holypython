import holypython

def edit_source(source):
	source = holypython.BlockEditor(source).edit_source()
	source = holypython.AssignmentEditor(source).edit_source()
	source = holypython.DefEditor(source).edit_source()
	return source

def test_edit_async_function_block():
	source = """
async function baz(a, b)
{
	return a + b
}
"""
	source = edit_source(source)
	assert source == """
async def baz(a, b):
	return a + b
"""

def test_edit_class_block():
	source = """
class Person
{
	function greet_world(self)
	{
		return "hello world"
	}
}

class Employee extends Person
{
	function get_answer(self)
	{
		return 37
	}
}

result <- Employee().get_answer()
"""
	namespace = {}
	exec(compile(edit_source(source), "<test>", "exec"), namespace)
	assert namespace["result"] == 37

def test_edit_function_block():
	source = """
function foo()
{
	x <- "foo"
	return x
}

result <- foo()
"""
	namespace = {}
	exec(compile(edit_source(source), "<test>", "exec"), namespace)
	assert namespace["result"] == "foo"
