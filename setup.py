try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # NOQA

version = __import__('fabtasktic').__version__

setup(
    name = "Fabtasktic",
    version = version,
    description = "Common Fabric Tasks for NPP",
    author = "NPP",
    author_email = "it@nationalpriorities.org",
    install_requires = ['fabric'],
    url = "https://github.com/npp/fabtasktic"
)