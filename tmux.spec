#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tmux
Version  : 3.3a
Release  : 41
URL      : https://github.com/tmux/tmux/releases/download/3.3a/tmux-3.3a.tar.gz
Source0  : https://github.com/tmux/tmux/releases/download/3.3a/tmux-3.3a.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause ISC
Requires: tmux-bin = %{version}-%{release}
Requires: tmux-license = %{version}-%{release}
Requires: tmux-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : pkgconfig(libevent)
BuildRequires : pkgconfig(libevent_core)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(tinfo)

%description
Welcome to tmux!
tmux is a terminal multiplexer: it enables a number of terminals to be created,
accessed, and controlled from a single screen. tmux may be detached from a
screen and continue running in the background, then later reattached.

%package bin
Summary: bin components for the tmux package.
Group: Binaries
Requires: tmux-license = %{version}-%{release}

%description bin
bin components for the tmux package.


%package license
Summary: license components for the tmux package.
Group: Default

%description license
license components for the tmux package.


%package man
Summary: man components for the tmux package.
Group: Default

%description man
man components for the tmux package.


%prep
%setup -q -n tmux-3.3a
cd %{_builddir}/tmux-3.3a

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664898387
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664898387
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tmux
cp %{_builddir}/tmux-%{version}/COPYING %{buildroot}/usr/share/package-licenses/tmux/a8d32eee6673ecc60a6b42b9f33211ba184950db || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tmux

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tmux/a8d32eee6673ecc60a6b42b9f33211ba184950db

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tmux.1
