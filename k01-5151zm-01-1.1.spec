Name:	k01-5151zm-01
Version:	1.1
Release:	1%{?dist}
Summary:	Программа студента Водопьян Людмилы группы 5151зм
Group:		Testing
License:	GPL
URL:		http://www.lug.mephist.ru
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/tmp/
%description
A test package
%define debug_package %{nil}
%prep
%setup -c k01-5151zm-01-1.1
%build
gcc -o k01-5151zm-01-1.1 k01-5151zm-01-1.1.c
%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
cp k01-5151zm-01-1.1 $RPM_BUILD_ROOT/usr/local/bin
%clean
rm -rf $RPM_BUILD_ROOT
%files
/usr/local/bin/k01-5151zm-01-1.1
#%doc
%attr(0755,root,root)/usr/local/bin/k01-5151zm-01-1.1
%changelog
* Sun Nov 11 2018 Vodopyan
- Added /usr/local/bin/k01-5151zm-01-1.1
