import os
from scripts.docker_handler import DockerHandler

class DartRunner:
    SOLUTION_FOLDER = os.path.abspath("solution")
    TEST_CASES_FOLDER = os.path.abspath("test_cases")
    DOCKER_EXEC = ["docker-compose", "exec", "-T", "dart-container"]

    @staticmethod
    def compile_dart(dart_file):
        # No compile needed for Dart
        pass

    @staticmethod
    def run_dart(dart_file, input_file):
        input_path = f"/test_cases/in/{input_file}"
        with open(os.path.join(DartRunner.TEST_CASES_FOLDER, "in", input_file), "r") as f:
            expected_input = "\n".join([line.strip() for line in f.readlines()])

        command = DartRunner.DOCKER_EXEC + ["bash", "-c", f"echo \"{expected_input}\" | dart {dart_file}"]
        output, _ = DockerHandler.exec_command(command)
        return output
