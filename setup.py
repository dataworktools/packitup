import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.1',
    author='Felix A. Sanchez',
    author_email='devizn-data@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/devizn-data/packitup',
    project_urls = {
        "Bug Tracker": "https://github.com/devizn-data/packitup/issues"
    },
    license='GNU General Public License v3.0',
    packages=['packitup'],
    install_requires=['requests'],
)
