import setuptools

__version__ = '0.0.1'

with open("README.md", "r") as f:
    long_description = f.read()

REPO_NAME = "CNN-Classifier"
AUTHOR_NAME = "Manisha Singh"
SRC_REPO = "CNNClassifier"
AUTHOR_EMAIL = "manisha.exe@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    description = "This is classification project.",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {"Bug Tracker": f"https://{AUTHOR_NAME}/{REPO_NAME}/issues"},
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where='src')
)