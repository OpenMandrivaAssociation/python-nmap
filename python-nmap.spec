Summary:	Use nmap and access scan results from python
Name:		python-nmap
Version:	0.2.7
Release:	1
Source0:	http://xael.org/norman/python/python-nmap/%{name}-%{version}.tar.gz
Group:		Development/Python
License:	GPLv3+
URL:		http://xael.org/norman/python/python-nmap/
BuildArch:	noarch
BuildRequires: python-devel

%description
python-nmap is a python library which helps in using nmap port scanner.
It allows to easilly manipulate nmap scan results and will be a perfect
tool for systems administrators who want to automatize scanning task
and reports. It also supports nmap script outputs.

It can even be used asynchronously. Results are returned one host at a time
to a callback function defined by the user.

%prep
%setup -q

%build
#nothing to do

%install
%{__python} setup.py install \
	--root=%{buildroot} \

%files
%doc README.txt CHANGELOG
%{python_sitelib}/nmap/
%{python_sitelib}/python_nmap-%{version}-py%{py_ver}.egg-info


%changelog
* Tue Dec 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.2-1mdv2011.0
+ Revision: 625614
- update to new version 0.2.2

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.1.4-2mdv2011.0
+ Revision: 590103
- rebuild for python 2.7

* Sun Jul 11 2010 Jani Välimaa <wally@mandriva.org> 0.1.4-1mdv2011.0
+ Revision: 550908
- import python-nmap



