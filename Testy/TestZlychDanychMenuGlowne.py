import unittest
from subprocess import Popen
from threading import Thread


class TestZlychDanychMenuGlowneTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal                   # unknown reason for showing error - IDE bug # TODO: try to find solution
        import FunctionWrongData                # unknown reason for showing error - IDE bug
        self.function_global = FunctionGlobal

        self.test_id = "TS003"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_entry()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(2)
        self.countdown_function_2 = FunctionGlobal.CountExecution(2)
        self.countdown_function_3 = FunctionGlobal.CountExecution(3)
        self.blank_data_written_test_case = FunctionWrongData.BlankDataWrittenTestCase(self.the_process)
        self.meaningless_chars_test_case = FunctionWrongData.MeaninglessCharsTestCase(self.the_process)
        self.wrong_command_test_case = FunctionWrongData.WrongCommandTestCase(self.the_process)

    def test_zlych_danych_menu_glowne_1_czesc(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.blank_data_written_test_case.start()
                first = False
            if self.blank_data_written_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.blank_data_written_test_case.this_log
        if self.blank_data_written_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertFalse(self.blank_data_written_test_case.finished, self.test_id + ". Nieoczekiwany komunikat zamiast braku reakcji.")

    def test_zlych_danych_menu_glowne_2_czesc(self):
        self.countdown_function_2.start()
        first = True
        while not self.countdown_function_2.finished:
            if first:
                self.meaningless_chars_test_case.start()
                first = False
            if self.meaningless_chars_test_case.finished:
                break
        Thread.join(self=self.countdown_function_2)
        self.the_log += self.meaningless_chars_test_case.this_log
        if self.meaningless_chars_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertFalse(self.meaningless_chars_test_case.finished, self.test_id + ". Nieoczekiwany komunikat zamiast braku reakcji.")

    def test_zlych_danych_menu_glowne_3_czesc(self):
        self.countdown_function_3.start()
        first = True
        while not self.countdown_function_3.finished:
            if first:
                self.wrong_command_test_case.start()
                first = False
            if self.wrong_command_test_case.finished:
                break
        Thread.join(self=self.countdown_function_3)
        self.the_log += self.wrong_command_test_case.this_log
        if not self.wrong_command_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.wrong_command_test_case.finished, self.test_id + ". Nieoczekiwana prosba o wpisanie danych.")
        elif "Wpisano niepoprawna" not in self.wrong_command_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("Wpisano niepoprawna", self.wrong_command_test_case.this_log, self.test_id + ". Brak informacji o niepoprawnej komendzie.")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
        self.countdown_function_1 = None
        self.countdown_function_2 = None
        self.countdown_function_3 = None
        self.blank_data_written_test_case = None
        self.meaningless_chars_test_case = None
        self.wrong_command_test_case = None
