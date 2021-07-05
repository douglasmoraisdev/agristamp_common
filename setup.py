import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="agristamp_common",
    version="1.4.8",
    author="Agristamp",
    author_email="agristamp@agristamp.com.br",
    description="Agristamp Microservices Commom Dependencies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/douglasmoraisdev/agristamp_common",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=['requests', 'pytest', 'boto3', 'httpx', 'aioredis']
)
