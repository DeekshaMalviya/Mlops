import setuptools

with open("README.md","r", encoding="utf-8") as f:
  long_description = f.read()

__verison__ = "0.0.0"
REPO_NAME = "Mlops"
AUTHOR_USER_NAME ="DeekshaMalviya"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "deekshamalviyacp@gmail.com"

setuptools.setup(
  name= SRC_REPO,
  version=__verison__,
  author=AUTHOR_USER_NAME,
  author_email=AUTHOR_EMAIL,
  description="A small pyhton package for ml app",
  long_description=long_description,
  long_description_content="text/markdown",
  url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
  project_urls={
    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
  },
  package_dir = {"":"src"},
  packages=setuptools.find_packages(where="src")
)