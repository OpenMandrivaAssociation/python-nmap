Summary:	Use nmap and access scan results from python
Name:		python-nmap
Version:	0.2.2
Release:	%mkrel 1
Source0:	http://xael.org/norman/python/%{name}/%{name}-%{version}.tar.gz
Group:		Development/Python
License:	GPLv3+
URL:		http://xael.org/norman/python/python-nmap/
BuildArch:	noarch
%py_requires -d
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%{__rm} -rf %{buildroot}
%{__python} setup.py install \
	--root=%{buildroot} \

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt CHANGELOG
%{python_sitelib}/nmap/
%{python_sitelib}/python_nmap-%{version}-py%{pyver}.egg-info
