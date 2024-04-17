from parse import parse_timesheet

class TestParse:

    def test_one_task(self):
        input = ["Standup", 
                 "9:00-9:30"]
        
        expected_output = "Standup\n0.5 hours\n"

        output = parse_timesheet(input)
        assert output == expected_output
    
    def test_two_tasks(self):
        input = ["Standup", 
                 "9:00-9:30",
                 "Dev Meeting",
                 "9:30-10:30"]
        
        expected_output = "Standup\n0.5 hours\nDev Meeting\n1 hour\n"

        output = parse_timesheet(input)
        assert output == expected_output

    def test_duplicate_task(self):
        input = ["Standup", 
                 "9:00-9:30",
                 "Dev Meeting",
                 "9:30-10:30",
                 "Standup",
                 "10:30-11:00"]

        expected_output = "Standup\n1 hour\nDev Meeting\n1 hour\n"

        output = parse_timesheet(input)
        assert output == expected_output

    def test_long_task(self):
        input = ["Long Task", 
                 "9:00-5:00"]
        
        expected_output = "Long Task\n8.0 hours\n"

        output = parse_timesheet(input)
        assert output == expected_output

    def test_task_starting_at_noon(self):
        input = ["Task Starting at Noon", 
                 "12:15-1:00"]
        
        expected_output = "Task Starting at Noon\n0.75 hours\n"

        output = parse_timesheet(input)
        assert output == expected_output
