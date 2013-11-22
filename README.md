mediaproxy
==========

mediaproxy rpm
Install some development and system packages using YUM

Development tools
yum groupinstall “Development Tools”

Development libraries and headers for some existing packages
yum install iptables-devel.x86_64
yum install libgpg-error-devel.x86_64
yum install python-devel.x86_64

libnfnetlink and libnetfilter_conntrack

yum install libnfnetlink-devel.x86_64
yum install libnetfilter_conntrack-devel.x86_64

libgcrypt

yum install libgcrypt-devel

Install some Python packages

python-zopeinterface

yum install python-zope-interface

python-cjson

This module can be installed using YUM, but first you will have to activate the rpmforge repository. The best way to do this is using the instructions here:
http://wiki.centos.org/AdditionalResources/Repositories/RPMForge

It is also possible to install the required python-cjson package from a source tarball as follows:

Suggested version: python-cjson-1.0.5.tar.gz
Locating a download site: http://pypi.python.org/pypi/python-cjson/1.0.5
Unzip: tar -xf python-cjson-1.0.5.tar.gz
Change to the sub-directory created when you unzipped the tarball
Build and install the library:
./setup.py build
./setup.py install

The following python packages are best installed from source tarballs. Details are given below:

python-application

Suggested version: python-application-1.3.0.tar.gz
Locating a download site: http://pypi.python.org/pypi/python-application/1.3.0
Unzip: tar -xf python-application-1.3.0.tar.gz
Change to the sub-directory created when you unzipped the tarball
Build and install the library:
./setup.py build
./setup.py install

python-gnutls

Suggested version: python-gnutls-1.2.4.tar.gz
Locating a download site: http://pypi.python.org/pypi/python-gnutls/1.2.4
Unzip: tar -xf python-gnutls-1.2.4.tar.gz
Change to the sub-directory created when you unzipped the tarball
Build and install the library:
./setup.py build
./setup.py install

Install the Twisted Python package

Install the core Twisted package from Twisted Matrix Labs
Suggested version: Twisted-11.0.0.tar.bz2
Locating a download site: http://twistedmatrix.com/trac
Unzip: tar -xf Twisted-11.0.0.tar.bz2
Change to the sub-directory created when you unzipped the tarball
Build and install the library:
./setup.py build
./setup.py install

Note also that version 8.2.0 of Twisted is available in the default YUM repositories. It is easier to install using YUM, but I prefer to install the later version from the source tarball because it matches the version used in the Debian install packages provided by AG-Projects.

A Checklist of dependencies and versions

On the system used for testing, the list of packages (and their versions) required by Mediaproxy looked like this prior to installation of the mediaproxy source code:

Package	Version
gcc	4.4.6
gcc-c++	4.4.6
iptables and iptables-devel	1.4.7
libnfnetlink and libnfnetlink-devel	1.0.0
libnetfilter_conntrack and libnetfilter_conntrack-devel	0.0.100
libgcrypt and libgcrypt-devel	1.4.5
libgpg-error and libgpg-error-devel	1.7
gnutls	2.8.5
python and python-devel	2.6.6
python-zope-interface	3.5.2
python-twisted	11.0.0
python-gnutls	1.2.4
python-application	1.3.0
python-cjson	1.0.5
