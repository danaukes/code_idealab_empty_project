# -*- coding: utf-8 -*-
'''
Written by Daniel M. Aukes and CONTRIBUTORS
Email: danaukes<at>asu.edu.
Please see LICENSE for full license.
'''

from setuptools import setup
import sys
import shutil

shutil.rmtree("build", ignore_errors=True)
shutil.rmtree("dist", ignore_errors=True)
shutil.rmtree('idealab_tools.egg-info', ignore_errors=True)

packages = []
packages.append('idealab_empty_project')

package_data = {}
package_data['idealab_tools'] = []

setup_kwargs = {}
setup_kwargs['name']='idealab_empty_project'
setup_kwargs['version']='0.0.1'
setup_kwargs['classifiers']=['Programming Language :: Python','Programming Language :: Python :: 3']   
setup_kwargs['description']='Empty QT Project developed by the IDEAlab.'
setup_kwargs['author']='Dan Aukes'
setup_kwargs['author_email']='danaukes@danaukes.com'
#setup_kwargs['url']='https://github.com/idealabasu/code_idealab_tools.git'
setup_kwargs['license']='MIT'
setup_kwargs['packages']=packages
setup_kwargs['package_dir']={'idealab_empty_project' : 'python/idealab_empty_project'}
setup_kwargs['package_data'] = package_data
setup_kwargs['install_requires']=['imageio']
  
setup(**setup_kwargs)
