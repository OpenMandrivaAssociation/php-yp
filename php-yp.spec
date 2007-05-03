%define modname yp
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 65_%{modname}.ini

Summary:	NIS (yp) extension module for PHP
Name:		php-%{modname}
Version:	5.2.2
Release:	%mkrel 1
Group:		Development/PHP
URL:		http://www.php.net
License:	PHP License
Source0:	yp.tar.bz2
BuildRequires:	php-devel >= 3:5.2.0
Provides:	php5-yp
Obsoletes:	php5-yp
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Epoch:		3

%description
This is a dynamic shared object (DSO) for PHP that will add NIS (Yellow Pages)
support.

%prep

%setup -q -n yp

%build

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS package.xml
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


