import subprocess  # Importing subprocess module to execute shell commands
import logging  # Importing logging module for structured logging

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,  # Set log level to INFO to capture important messages
    format='| %(levelname)-15s | %(asctime)s | %(name)s | %(lineno)-4s ::  %(message)s'  # Log format
)

# Create a logger instance named "test"
logger = logging.getLogger("test")

# Define a list of shell commands to be executed
command = [
    'grep -rl "org" *',  # Search for "org" recursively in all files and return matching filenames
    'ls',  # List files and directories in the current working directory
    'pwd'  # Print the present working directory
]

# Iterate through each command and execute it
for cmd in command:
    # Run the command using subprocess
    result = subprocess.run(
        cmd, 
        shell=True,  # Enable shell command execution
        check=True,  # Raise an error if the command fails
        text=True,  # Ensure output is in string format instead of bytes
        stdout=subprocess.PIPE,  # Capture standard output
        stderr=subprocess.PIPE   # Capture standard error
    )

    # Log and print the command output
    logger.info(result.stdout)  # Log the standard output of the command

    # Print any errors, if present
    print(result.stderr, end='')  # Print standard error messages (if any)
