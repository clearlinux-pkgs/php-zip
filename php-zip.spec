#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-zip
Version  : 1.15.5
Release  : 6
URL      : https://pecl.php.net/get/zip-1.15.5.tgz
Source0  : https://pecl.php.net/get/zip-1.15.5.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-zip-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : libzip-dev
BuildRequires : pcre2-dev

%description
No detailed description available

%package lib
Summary: lib components for the php-zip package.
Group: Libraries

%description lib
lib components for the php-zip package.


%prep
%setup -q -n zip-1.15.5
cd %{_builddir}/zip-1.15.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/zip.so
