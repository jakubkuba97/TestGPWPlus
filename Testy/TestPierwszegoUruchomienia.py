import unittest
from subprocess import Popen
from threading import Thread


class TestPierwszegoUruchomieniaTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal           # unknown reason for showing error - IDE bug # TODO: try to find solution
        import FunctionWrongData        # unknown reason for showing error - IDE bug
        self.function_global = FunctionGlobal

        self.test_id = "TS002"
        self.function_global.ForTearDown().delete_pages_file()
        self.the_process = Popen(self.function_global.ForSetUp().launch_program())
        self.the_log = self.function_global.ForSetUp().get_first_launch_data(self.the_process)

        self.countdown_function_1 = FunctionGlobal.CountExecution(5)
        self.blank_data_written_test_case = FunctionWrongData.BlankDataWrittenTestCase(self.the_process)
        self.data_wrong_for_file_saving_test_case = FunctionWrongData.DataWrongForFileSavingTestCase()

    def test_pierwszego_uruchomienia_1_czesc(self):
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
        if (not self.blank_data_written_test_case.finished) or ("zla" not in self.blank_data_written_test_case.this_log.lower()):
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.blank_data_written_test_case.finished, self.test_id + ". Brak prośby o ponowienie przy pustym wejsciu!")

    def test_pierwszego_uruchomienia_2_czesc(self):
        temporary_output = self.data_wrong_for_file_saving_test_case.write_wrong_file_saving_data(self.the_process)
        self.the_log += temporary_output
        if "zla" not in temporary_output:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn("zla", temporary_output, self.test_id + ". Brak prośby o ponowienie przy blednych danych do zapisu pliku!")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.countdown_function_1 = None
        self.blank_data_written_test_case = None
        self.data_wrong_for_file_saving_test_case = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
