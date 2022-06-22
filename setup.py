from distutils.core import setup
from unknown_fields import __appname__, __version__, __license__, __url__, __author__

setup(
    name=__appname__,  # How you named your package folder (MyLib)
    packages=[__appname__],  # Chose the same as "name"
    version=__version__,  # Start with a small number and increase it with every change you make
    license=__license__,  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Wrapper to handle unknown parameters for dataclasses init',  # Give a short description about your
    # library
    author=__author__,  # Type in your name
    author_email='haruna-dev@proton.me',  # Type in your E-Mail
    url=__url__,  # Provide either the link to your github or to your website
    download_url=f'{__url__}/archive/{__version__}.tar.gz',  # I explain this later on
    keywords=[''],  # ToDo
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
