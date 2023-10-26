from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dt_gomechanic_workforce_integraion/__init__.py
from dt_gomechanic_workforce_integraion import __version__ as version

setup(
	name="dt_gomechanic_workforce_integraion",
	version=version,
	description="API Integration with Workforce app",
	author="Dipane Technologies",
	author_email="support@dipanetech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
