from distutils.core import setup

if __name__== '__main__':
    setup(include_package_data=True,
          description='Sequence motif visualization',
          url='NA',
          download_url='NA',
          version='0.1',
          packages=['seqmotif'],
          setup_requires=[],
          install_requires=['numpy>=1.9', 'matplotlib>=1.4'],
          scripts=[],
          name='seqmotif')
