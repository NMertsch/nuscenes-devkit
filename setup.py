import setuptools


setuptools.setup(
    name='nuscenes-devkit',
    version='1.1.1',
    author='Holger Caesar, Oscar Beijbom, Qiang Xu, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, '
           'Sergi Widjaja, Kiwoo Shin, Caglayan Dicle, Freddy Boulton, Whye Kit Fong, Asha Asvathaman et al.',
    author_email='nuscenes@motional.com',
    description='The official devkit of the nuScenes dataset (www.nuscenes.org).',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nutonomy/nuscenes-devkit',
    python_requires='>=3.6',
    install_requires=open('requirements.txt').read().splitlines(keepends=False),
    packages=setuptools.find_packages('nuscenes'),
    package_dir={'': 'nuscenes'},
    package_data={'': ['*.json']},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'License :: Free for non-commercial use'
    ],
    license='cc-by-nc-sa-4.0'
)
