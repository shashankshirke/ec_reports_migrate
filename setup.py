from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ec_reports_migrate/__init__.py
from ec_reports_migrate import __version__ as version

setup(
	name="ec_reports_migrate",
	version=version,
	description="Migrate",
	author="Shashank",
	author_email="s@s.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
