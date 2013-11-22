%define name python-application
%define version 1.3.0
%define unmangled_version 1.3.0
%define release 1

Summary: Basic building blocks for python applications
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Dan Pascu <dan@ag-projects.com>
Url: http://ag-projects.com/

%description

This package is a collection of modules that are useful when building python
applications. Their purpose is to eliminate the need to divert resources into
implementing the small tasks that every application needs to do in order to
run successfully and focus instead on the application logic itself.

The modules that the application package provides are:

1. process       - UNIX process and signal management.
2. python        - python utility classes and functions.
3. configuration - a simple interface to handle configuration files.
4. log           - an extensible system logger for console and syslog.
5. debug         - memory troubleshooting and execution timing.
6. system        - interaction with the underlying operating system.
7. notification  - an application wide notification system.
8. version       - manage version numbers for applications and packages.
9. dependency    - verify package dependencies at runtime.



%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
