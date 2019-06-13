import unittest


class TestInicjujacyTestCases(unittest.TestCase):
    def setUp(self) -> None:
        import FunctionGlobal   # unknown reason for showing error - IDE bug
        self.function_global = FunctionGlobal
        self.test_id = "TS001"

    def test_inicjujacy(self):
        pass

    def tearDown(self) -> None:
        pass


# use only for debug
if __name__ == '__main__':
    import FunctionGlobal
    function_global = FunctionGlobal
    print(function_global.Constants().pages_bytes_name)
