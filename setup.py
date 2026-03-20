from setuptools import setup, find_packages
setup(
    name="dataset-summary-tool",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pandas", "matplotlib", "seaborn"],
    author="Mashaim Hanif",
    description="A tool for dataset summary and visualization",
    long_description_content_type="text/markdown",
)