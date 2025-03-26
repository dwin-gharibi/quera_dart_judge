import unittest
import os
from scripts.docker_handler import DockerHandler
from scripts.dart_runner import DartRunner

class TestDartPrograms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        DockerHandler.start_container()

    @classmethod
    def tearDownClass(cls):
        DockerHandler.stop_container()

    def test_1(self):
        dart_file = "solution.dart"
        input_file = "input4.txt"
        output_file = "output4.txt"

        DartRunner.compile_asm(dart_file)
        output = DartRunner.run_asm(dart_file, input_file)

        output_path = os.path.join(DartRunner.TEST_CASES_FOLDER, "out", output_file)
        with open(output_path, "r") as f:
            expected_output = [line.strip() for line in f.readlines()]

        self.assertEqual(output, expected_output, f"Unexpected output for {dart_file}")


if __name__ == "__main__":
    unittest.main()
