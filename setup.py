from setuptools import find_packages, setup

setup(
    name="medical_chatbot",
    version="0.1.0",
    author="Sarthak Singh Rawat",
    author_email="sarthakrawat1092@gmail.com",
    packages=find_packages(),
    install_requires=[
        "openai",
        "pinecone-client",
        "langchain",
        "python-dotenv",
        "faiss-cpu",
        "pydantic",
        "pytest",   
    ]
)