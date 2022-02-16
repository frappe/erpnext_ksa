from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_ksa/__init__.py
from erpnext_ksa import __version__ as version

setup(
	name="erpnext_ksa",
	version=version,
	description="App to hold regional code for Saudi Arabia, built on top of ERPNext.",
	author="Frappe Technologies",
	author_email="contact@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
