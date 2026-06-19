import snekscript

def test_edit_equality():
	source = snekscript.EqualityCheckEditor("if a = b:\n\tpass\n").edit_source()
	assert source == "if a == b:\n\tpass\n"

def test_keep_keyword_argument():
	source = snekscript.EqualityCheckEditor("print(\"hi\", end=\"\")").edit_source()
	assert source == "print(\"hi\", end=\"\")"
