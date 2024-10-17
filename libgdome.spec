%define src_name gdome2

%define major 0
%define libname  %mklibname gdome %{major}
%define develname %mklibname -d gdome

Summary:	A DOM level2 library for accessing XML files
Name:		libgdome
Version:	0.8.1
Release:	11
License:	LGPL
Group:		System/Libraries
URL:		https://gdome2.cs.unibo.it
Source0:	http://gdome2.cs.unibo.it/tarball/%{src_name}-%{version}.tar.bz2
Patch0:		gdome2-0.8.1-gdome-config_lib64.diff
Patch1:		gdome2-0.8.1-fix-str-fmt.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(glib)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

Provides:	gdome2

%description
Libgdome is a DOM C library developed for the Gnome project.
Libgdome is a DOM level2 Implementation.
Libgdome supports "Core" and "XML" modules.
Libgdome supports "Events" and "MutationEvents" modules.
Libgdome is based on libxml2.

%package -n	%{libname}
Summary:	A DOM level2 library for accessing XML files
Group:		System/Libraries

%description -n	%{libname}
A fast, light and complete DOM level2 implementation
based on libxml2

%package -n	%{develname}
Summary:	DOM level2 library for accessing XML files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{src_name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gdome0-devel < %{version}-%{release}

%description -n	%{develname}
This package contains the header files and static libraries for
developing with libgdome.

%prep
%setup -qn %{src_name}-%{version}
%patch0 -p0
%patch1 -p0

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--enable-glib-1=no

%make

%install
%makeinstall_std
%multiarch_binaries %{buildroot}%{_bindir}/gdome-config

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc AUTHORS MAINTAINERS ChangeLog INSTALL README COPYING COPYING.LIB
%{_bindir}/gdome-config
%{_datadir}/aclocal/gdome2.m4
%{_includedir}/*
%{_libdir}/pkgconfig/gdome2.pc
%{_libdir}/lib*.so
%{_libdir}/*.sh
%{_mandir}/man1/gdome-config.1*
%multiarch %{multiarch_bindir}/gdome-config



%changelog
* Tue Mar 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.8.1-11
+ Revision: 787555
- rebuild
- cleaned up spec

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-10mdv2011.0
+ Revision: 609749
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 0.8.1-9mdv2010.1
+ Revision: 508594
- BR glib1
- fix build
- fix str fmt
- new devel package policy

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Oct 11 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.8.1-5mdv2008.1
+ Revision: 96975
- Launch a rebuild
- Rebuild
- Import libgdome



* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-4mdk
- added fixes by Ville SkyttÃ¤
- lib64, deps and misc spec file fixes

* Mon May  9 2005 Götz Waschk <waschk@mandriva.org> 0.8.1-3mdk
- multiarch

* Tue Oct  5 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8.1-2mdk
- fix deps
- fix buildrequires

* Fri Aug 13 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.8.1-1mdk
- New release 0.8.1

* Wed Jul  9 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7.4-4mdk
- rebuild for new rpm

* Tue Jun 10 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7.4-3mdk
- fix buildrequires

* Tue Jun 10 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7.4-2mdk
- remove some obsolete requires
- rebuild for devel requires and provides

* Fri May  2 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7.4-1mdk
- dir ownership
- add source URL
- from Charles A Edwards <eslrahc@bellsouth.net>:
  - initial mdk release
