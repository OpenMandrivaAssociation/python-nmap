Summary:	Use nmap and access scan results from python
Name:		python-nmap
Version:	0.3.4
Release:	2
Source0:	http://xael.org/norman/python/python-nmap/%{name}-%{version}.tar.gz
Group:		Development/Python
License:	GPLv3+
URL:		https://xael.org/norman/python/python-nmap/
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
python setup.py install \
	--root=%{buildroot} \

%files
%doc README.txt CHANGELOG
%{py_puresitedir}/nmap/
%{py_puresitedir}/python_nmap-%{version}-py%{py_ver}.egg-info
