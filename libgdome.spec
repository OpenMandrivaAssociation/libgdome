%define src_name gdome2

%define major 0
%define libname  %mklibname gdome %{major}

Summary:	A DOM level2 library for accessing XML files
Name:		libgdome
Version:	0.8.1
Release:	%mkrel 9
License:	LGPL
Group:		System/Libraries
URL:		http://gdome2.cs.unibo.it
Source0:	http://gdome2.cs.unibo.it/tarball/%{src_name}-%{version}.tar.bz2
Patch0:		gdome2-0.8.1-gdome-config_lib64.diff
BuildRequires:	pkgconfig
BuildRequires:	libxml2-devel >= 2.4.26
BuildRequires:	glib2-devel
Provides:	gdome2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{libname}-devel
Summary:	DOM level2 library for accessing XML files
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{src_name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
This package contains the header files and static libraries for
developing with libgdome.

%prep

%setup -qn %{src_name}-%{version}
%patch0 -p0

%build
# to fix gdome-config(1)
export GLIB_CONFIG="pkg-config glib-2.0"

%configure

%make

# xpath check don't work unless libxml2-2.6.20
#make check

%install
rm -rf %{buildroot}

%makeinstall
%multiarch_binaries %{buildroot}%{_bindir}/gdome-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS MAINTAINERS ChangeLog INSTALL README COPYING COPYING.LIB
%{_bindir}/gdome-config
%multiarch %multiarch_bindir/gdome-config
%dir %{_datadir}/gtk-doc/html/%{src_name}-%{version}/
%{_datadir}/gtk-doc/html/%{src_name}-%{version}/*.html
%{_datadir}/gtk-doc/html/%{src_name}-%{version}/*.sgml
%{_datadir}/aclocal/gdome2.m4
%{_includedir}/*
%{_libdir}/pkgconfig/gdome2.pc
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/*.sh
%{_mandir}/man1/gdome-config.1*
