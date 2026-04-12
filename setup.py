import setuptools

with open ("README.md","r",encoding="utf-8") as f:
    long_discriptio = f.read()

__version__ = "0.0.0"

REPO_NAME ="MLOPS-project"
AUTHOR_USER_NAME ="Garvitbagadi1"
SRC_REPO ="mlProject"
AUTHOR_EMAIL ="garvitbagadi0851@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    verion=__version__,
    author = AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="small pyhton pakage for ml application",
    long_long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)