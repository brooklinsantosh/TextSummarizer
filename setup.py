import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "brooklinsantosh"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "brooklinsantosh@gmail.com"

def get_requirements(file_path: str) -> list[str]:
    """
    This function will read the requirements.txt file and return the required libraries.
    """
    HYPHEN_E_DOT = "-e ."
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        requirements = [r.replace("\n","") for r in req]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Transformer based Text Summarizer",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
)