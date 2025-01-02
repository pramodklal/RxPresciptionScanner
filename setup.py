from setuptools import find_packages, setup

setup(
    name="RxScannerBOT",
    version="0.0.1",
    author="Pramod",
    author_email="pramodklal@gmail.com",
    packages=find_packages(),
    install_requires=['google-cloud-aiplatform','langchain ','langchain-openai','datasets','pypdf','python-dotenv','streamlit','pytesseract','google-generativeai']
)