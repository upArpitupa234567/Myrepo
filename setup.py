from setuptools import find_packages,setup

REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILENAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","")for requirement_name in ]

setup(
    name = "sensor",
    version="59.6.0",
    author="arpit",
    author_email = "arpitupadhyay382@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)