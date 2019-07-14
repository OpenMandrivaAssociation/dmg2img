%define _disable_lto 1

Summary:	Uncompress the Apple compressed disk image files
Name:		dmg2img
Version:	1.6.7
Release:	1
# dmg2img is GPL without specific version
# vfdecrypt is MIT licensed
License:	GPLv+ and MIT
Group:		File tools
Source0:	http://vu1tur.eu.org/tools/%{name}-%{version}.tar.gz
Patch0:		dmg2img-1.6.2-nostrip.patch
Patch1:		dmg2img-1.6.7-openssl11.patch
URL:		http://vu1tur.eu.org/tools/
BuildRequires:	bzip2-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel

%description
This package contains dmg2img utility that is able to uncompress compressed dmg 
files into plain disk or filesystem images.

%prep
%setup -q
%autopatch -p1


%build
%make CC="%{__cc}" CFLAGS="%{optflags}"


%install
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_bindir}

install dmg2img %{buildroot}%{_bindir}
install vfdecrypt %{buildroot}%{_bindir}
install -pm644 vfdecrypt.1 %{buildroot}%{_mandir}/man1

%files
%{_bindir}/dmg2img
%{_bindir}/vfdecrypt
%{_mandir}/man1/vfdecrypt.1*
%doc README COPYING
