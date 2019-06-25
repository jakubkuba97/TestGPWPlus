import unittest
from subprocess import Popen
from threading import Thread


class TestDetalowychInformacjiTestCases(unittest.TestCase):
    def setUp(self) -> None:
        from sys import warnoptions
        if not warnoptions:
            import warnings
            warnings.simplefilter("ignore", ResourceWarning)
        import FunctionGlobal
        import FunctionMain
        self.function_global = FunctionGlobal

        self.test_id = "TS014"
        self.the_process = self.function_global.ForSetUp().correct_main_menu_1_site_saved()
        self.the_log = ""

        self.countdown_function_1 = FunctionGlobal.CountExecution(2)
        self.look_one_site_function_test_case = FunctionMain.LookOneSiteFunctionTestCase(self.the_process)

    def test_detalowych_informacji(self):
        self.countdown_function_1.start()
        first = True
        while not self.countdown_function_1.finished:
            if first:
                self.look_one_site_function_test_case.start()
                first = False
            if self.look_one_site_function_test_case.finished:
                break
        Thread.join(self=self.countdown_function_1)
        self.the_log += self.look_one_site_function_test_case.this_log
        if not self.look_one_site_function_test_case.finished:
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertTrue(self.look_one_site_function_test_case.finished, self.test_id + ". Blad pokazania detalowych informacji o spolce.")
        if self.look_one_site_function_test_case.the_data.replace("/look-", "")[1:-1] not in self.look_one_site_function_test_case.this_log:
            self.the_log += self.function_global.CommonTestCases().clear_remaining_input(self.the_process)
            self.function_global.ForTearDown().save_log_to_file(self.test_id, self.the_log)
            self.assertIn(self.look_one_site_function_test_case.the_data.replace("/look-", "")[1:-1], self.look_one_site_function_test_case.this_log,
                          self.test_id + ". Pokazanie detali o zlej spolce lub zle detale.")

    def tearDown(self) -> None:
        self.function_global.ForTearDown().close_program(self.the_process)
        self.function_global.ForTearDown().delete_pages_file()
        self.function_global = None
        self.test_id = None
        self.the_process = None
        self.the_log = None
        self.countdown_function_1 = None
        self.look_one_site_function_test_case = None
