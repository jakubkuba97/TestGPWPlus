import unittest
from subprocess import Popen
from threading import Thread


class TestSortowaniaSpolekTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal
        import FunctionSort
        import FunctionMain
        self.function_global = FunctionGlobal

        self.test_id = "TS012"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_3_sites_saved()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(1)
        self.countdown_function_2 = FunctionGlobal.CountExecution(1)
        self.alphabetical_sort_test_case = FunctionSort.AlphabeticalSortTestCase(self.the_process)
        self.percentage_sort_test_case = FunctionSort.PercentageSortTestCase(self.the_process)
        self.look_function_test_case = FunctionMain.LookFunctionTestCase(self.the_process)

    @staticmethod
    def check_if_alphabetical(lines: str) -> bool:
        try:
            lines = lines.replace(">>> ", "")
            new_lines = lines.split("\n")
            new_lines[0] = ""
            index = 12
            correct_order = [new_lines[1][index], new_lines[2][index], new_lines[3][index]]
            correct_order.sort()
            return [new_lines[1][index], new_lines[2][index], new_lines[3][index]] == correct_order
        except IndexError:
            raise IndexError("Unexpected data type was passed here!")

    @staticmethod
    def check_if_percentage(lines: str) -> bool:
        try:
            lines = lines.replace(">>> ", "")
            new_lines = lines.split("\n")
            new_lines[0] = ""
            index = 6
            correct_order = [float(str(repr(new_lines[1][new_lines[1].index("Zmiana:") + 14:-index]).replace(",", ".").replace("'", ""))),
                             float(str(repr(new_lines[2][new_lines[2].index("Zmiana:") + 14:-index]).replace(",", ".").replace("'", ""))),
                             float(str(repr(new_lines[3][new_lines[3].index("Zmiana:") + 14:-index]).replace(",", ".").replace("'", "")))]
            old_order = correct_order.copy()
            correct_order.sort(reverse=True)
            return old_order == correct_order
        except (IndexError, ValueError):
            raise IndexError("Unexpected data type was passed here!")

    def test_sortowania_spolek_1_czesc(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.alphabetical_sort_test_case.start()
                first = False
            if self.alphabetical_sort_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.alphabetical_sort_test_case.this_log
        if not self.alphabetical_sort_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.alphabetical_sort_test_case.finished, self.test_id + ". Niepoprawne dzialanie funkcji sortowania alfabetycznego.")
        if self.alphabetical_sort_test_case.no_sites_read:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertFalse(self.alphabetical_sort_test_case.no_sites_read, self.test_id + ". Blad wczytania spolek.")

        self.countdown_function_2.start()
        first = True
        while not self.countdown_function_2.finished:
            if first:
                self.look_function_test_case.start()
                first = False
            if self.look_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_2)
        self.the_log += self.look_function_test_case.this_log
        if not self.look_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.look_function_test_case.finished, self.test_id + '. Niepoprawne dzialanie funkcji "/look".')
        if not self.check_if_alphabetical(self.look_function_test_case.this_log):
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.check_if_alphabetical(self.look_function_test_case.this_log), self.test_id + ". Niepoprawne sortowanie alfabetyczne.")

        temporary_output = ""
        temporary_output += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
        self.the_log += temporary_output
        if temporary_output != "":
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertEqual(temporary_output, "", self.test_id + ". Niepoprawny powrot do glownego menu.")

    def test_sortowania_spolek_2_czesc(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.percentage_sort_test_case.start()
                first = False
            if self.percentage_sort_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.percentage_sort_test_case.this_log
        if not self.percentage_sort_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.percentage_sort_test_case.finished, self.test_id + ". Niepoprawne dzialanie funkcji sortowania procentowego.")
        if self.percentage_sort_test_case.no_sites_read:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertFalse(self.percentage_sort_test_case.no_sites_read, self.test_id + ". Blad wczytania spolek.")

        self.countdown_function_2.start()
        first = True
        while not self.countdown_function_2.finished:
            if first:
                self.look_function_test_case.start()
                first = False
            if self.look_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_2)
        self.the_log += self.look_function_test_case.this_log
        if not self.look_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.look_function_test_case.finished, self.test_id + '. Niepoprawne dzialanie funkcji "/look".')
        if not self.check_if_percentage(self.look_function_test_case.this_log):
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.check_if_percentage(self.look_function_test_case.this_log), self.test_id + ". Niepoprawne sortowanie procentowe.")

        temporary_output = ""
        temporary_output += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
        self.the_log += temporary_output
        if temporary_output != "":
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertEqual(temporary_output, "", self.test_id + ". Niepoprawny powrot do glownego menu.")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
        self.countdown_function_1 = None
        self.countdown_function_2 = None
        self.alphabetical_sort_test_case = None
        self.percentage_sort_test_case = None
        self.look_function_test_case = None
