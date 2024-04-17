import pytest
from parse import parse_timesheet

class TestParse:

    def test_simple_timesheet(self):
        input = ["Standup", "9:00-9:30"]
        
        expected_output = "Standup\n0.5 hours\n"

        output = parse_timesheet(input)
        assert output == expected_output
