%define modname yp
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 65_%{modname}.ini

Summary:	NIS (yp) extension module for PHP
Name:		php-%{modname}
Version:	5.2.3
Release:	29
Group:		Development/PHP
URL:		https://www.php.net
License:	PHP License
Source0:	yp.tar.bz2
Patch0:		yp-php54x.diff
BuildRequires:	php-devel >= 3:5.2.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Epoch:		3

%description
This is a dynamic shared object (DSO) for PHP that will add NIS (Yellow Pages)
support.

%prep

%setup -q -n yp
%patch0 -p0

%build
%serverbuild

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

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS package.xml
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-28mdv2012.0
+ Revision: 796966
- new patch
- fix build
- rebuild for php-5.4.x

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-27
+ Revision: 761349
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-26
+ Revision: 696493
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-25
+ Revision: 695494
- rebuilt for php-5.3.7

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-24
+ Revision: 646708
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-23mdv2011.0
+ Revision: 629903
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-22mdv2011.0
+ Revision: 628227
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-21mdv2011.0
+ Revision: 600552
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-20mdv2011.0
+ Revision: 588889
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-19mdv2010.1
+ Revision: 514722
- rebuilt for php-5.3.2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-18mdv2010.1
+ Revision: 485505
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-17mdv2010.1
+ Revision: 468276
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-16mdv2010.0
+ Revision: 451388
- rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 3:5.2.3-15mdv2010.0
+ Revision: 397287
- Rebuild

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-14mdv2010.0
+ Revision: 377046
- rebuilt for php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-13mdv2009.1
+ Revision: 346710
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-12mdv2009.1
+ Revision: 341851
- rebuilt against php-5.2.9RC2

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-11mdv2009.1
+ Revision: 323146
- rebuild

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-10mdv2009.1
+ Revision: 310323
- rebuilt against php-5.2.7

* Fri Jul 18 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-9mdv2009.0
+ Revision: 238476
- rebuild

* Tue Jul 15 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-8mdv2009.0
+ Revision: 235887
- rebuild

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-7mdv2009.0
+ Revision: 200123
- rebuilt against php-5.2.6

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-6mdv2008.1
+ Revision: 161965
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-5mdv2008.1
+ Revision: 107584
- restart apache if needed

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-4mdv2008.0
+ Revision: 77469
- rebuilt against php-5.2.4

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-3mdv2008.0
+ Revision: 64311
- use the new %%serverbuild macro

* Thu Jun 14 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-2mdv2008.0
+ Revision: 39395
- use distro conditional -fstack-protector

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.3-1mdv2008.0
+ Revision: 33770
- rebuilt against new upstream version (5.2.3)

* Thu May 03 2007 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.2-1mdv2008.0
+ Revision: 21019
- rebuilt against new upstream version (5.2.2)


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.1-1mdv2007.0
+ Revision: 117454
- rebuilt against new upstream version (5.2.1)

* Wed Nov 08 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-2mdv2007.0
+ Revision: 78410
- fix deps

* Tue Nov 07 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.2.0-1mdv2007.0
+ Revision: 77420
- rebuilt for php-5.2.0

* Thu Nov 02 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.6-1mdv2007.1
+ Revision: 75409
- Import php-yp

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.6-1
- rebuilt for php-5.1.6

* Thu Jul 27 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.4-2mdk
- rebuild

* Sat May 06 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.4-1mdk
- rebuilt for php-5.1.4

* Fri May 05 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.3-1mdk
- rebuilt for php-5.1.3

* Thu Feb 02 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.2-2mdk
- new group (Development/PHP) and iurt rebuild

* Sun Jan 15 2006 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.2-1mdk
- rebuilt against php-5.1.2

* Tue Nov 29 2005 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.1-1mdk
- rebuilt against php-5.1.1

* Sat Nov 26 2005 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.0-1mdk
- rebuilt against php-5.1.0

* Thu Nov 03 2005 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.0-0.RC4.1mdk
- rebuilt against php-5.1.0RC4

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.0-0.RC1.2mdk
- rebuilt to provide a -debug package too

* Sun Oct 02 2005 Oden Eriksson <oeriksson@mandriva.com> 3:5.1.0-0.RC1.1mdk
- rebuilt against php-5.1.0RC1
- the source lives in pecl now (CVS)

* Wed Sep 07 2005 Oden Eriksson <oeriksson@mandriva.com> 3:5.0.5-1mdk
- rebuilt against php-5.0.5 (Major security fixes)

* Fri May 27 2005 Oden Eriksson <oeriksson@mandriva.com> 3:5.0.4-1mdk
- rename the package

* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-1mdk
- 5.0.4

* Sun Mar 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-4mdk
- use the %%mkrel macro

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-3mdk
- rebuilt against a non hardened-php aware php lib

* Sun Jan 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-2mdk
- rebuild due to hardened-php-0.2.6

* Fri Dec 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-1mdk
- rebuilt for php-5.0.3

* Sat Sep 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.2-1mdk
- rebuilt for php-5.0.2

* Sun Aug 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.1-1mdk
- rebuilt for php-5.0.1

* Wed Aug 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.0-1mdk
- initial mandrake package

