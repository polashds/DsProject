from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n', " ") for req in requirements]

    return requirements


setup(
    name='dsproject',
    version='0.0.1',
    author='polash',
    author_email="polashtechai@gmail.com",
    packages=find_packages(),
    #install_requires=['numpy','pandas']
    install_requires=get_requirements('requirements.txt')
)