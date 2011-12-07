Name:		PyGreSQL
Version:	3.8.1
Release:	2%{?dist}
Summary:	A Python client library for PostgreSQL

Group:		Applications/Databases
URL:		http://www.pygresql.org/
# Author states his intention is to dual license under PostgreSQL or Python
# licenses --- this is not too clear from the current tarball documentation,
# but hopefully will be clearer in future releases.
# PostgreSQL calls their license simplified BSD, but the requirements are
# more similar to other MIT licenses.
License:	MIT or Python

Source0:	ftp://ftp.pygresql.org/pub/distrib/PyGreSQL-3.8.1.tgz

# PyGreSQL was originally shipped as a sub-RPM of the PostgreSQL package;
# these Provides/Obsoletes give a migration path.  The cutoff EVR was
# chosen to be later than anything we are likely to ship in Fedora 12.
Provides:	postgresql-python = 8.5.0-1
Obsoletes:	postgresql-python < 8.5

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	postgresql-devel python-devel

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%description
PostgreSQL is an advanced Object-Relational database management system.
The PyGreSQL package provides a module for developers to use when writing
Python code for accessing a PostgreSQL database.

%prep
%setup -q 

# Some versions of PyGreSQL.tgz contain wrong file permissions
chmod 755 tutorial
chmod 644 tutorial/*.py

%build

CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc docs/*.txt
%doc tutorial
%{python_sitearch}/*.so
%{python_sitearch}/*.py
%{python_sitearch}/*.pyc
%{python_sitearch}/*.pyo
%{python_sitearch}/*.egg-info

%changelog
* Tue Nov 24 2009 Tom Lane <tgl@redhat.com> 3.8.1-2
- Fix License tag and permissions on example scripts under tutorial/,
  per discussion in package review request.
Related: #452321

* Fri Jun 20 2008 Tom Lane <tgl@redhat.com> 3.8.1-1
- Created package by stripping down postgresql specfile and adjusting
  to meet current packaging guidelines for python modules.
