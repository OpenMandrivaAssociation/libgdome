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
URL:		http://gdome2.cs.unibo.it
Source0:	http://gdome2.cs.unibo.it/tarball/%{src_name}-%{version}.tar.bz2
Patch0:		gdome2-0.8.1-gdome-config_lib64.diff
Patch1:		gdome2-0.8.1-fix-str-fmt.patch

BuildRequires:	intltool
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

