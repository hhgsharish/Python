# Define a class named `TestingExamples`
class TestingExamples:
    # Constructor (__init__) method to initialize package name and version
    def __init__(self, pkg_name, version):
        self.name = pkg_name  # Store the package name
        self.version = version  # Store the package version

    # Method to display package details
    def check_artifact(self):
        print(f"The package name is {self.name}")  # Print the package name
        print(f"The version is {self.version}")  # Print the package version

    # Method to print package name and version in a combined format
    def print_combine(self):
        print(f"The package name with version {self.name}:{self.version}")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Take user input for package name and version
    package = input("Enter the package Name\n")
    version = input("Enter the version\n")

    # Create an instance of `TestingExamples` with user-provided values
    check = TestingExamples(package, version)

    # Call methods to display package details
    check.check_artifact()  # Prints individual package details
    check.print_combine()  # Prints package name along with version
