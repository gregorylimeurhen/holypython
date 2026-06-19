import snekscript
import utils

def test_edit_assignment():
	namespace = utils.run_source(snekscript.VariableAssignmentEditor, "result <- 37")
	assert namespace["result"] == 37

def test_keep_comparison():
	namespace = utils.run_source(snekscript.VariableAssignmentEditor, "result = 1 < -2")
	assert namespace["result"] is False
