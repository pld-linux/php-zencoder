%define		pkgname	zencoder
%define		php_min_version 5.2.0
Summary:	Zencoder API PHP Library
Name:		php-%{pkgname}
Version:	2.2.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/zencoder/zencoder-php/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	0e0291422f189b770d14e5acc320a86a
URL:		https://github.com/zencoder/zencoder-php
BuildRequires:	/usr/bin/php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	ca-certificates
Requires:	php(core) >= %{php_min_version}
Requires:	php(curl)
Requires:	php(json)
Requires:	php(spl)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zencoder integration library for PHP.

%prep
%setup -q -n %{pkgname}-php-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
cp -a Services $RPM_BUILD_ROOT%{php_pear_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{php_pear_dir}/Services/Zencoder.php
%dir %{php_pear_dir}/Services/Zencoder
%{php_pear_dir}/Services/Zencoder/*.php
