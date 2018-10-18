#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tmux
Version  : 2.8
Release  : 28
URL      : https://github.com/tmux/tmux/releases/download/2.8/tmux-2.8.tar.gz
Source0  : https://github.com/tmux/tmux/releases/download/2.8/tmux-2.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC
Requires: tmux-bin = %{version}-%{release}
Requires: tmux-license = %{version}-%{release}
Requires: tmux-man = %{version}-%{release}
BuildRequires : pkgconfig(libevent)
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
Requires: tmux-man = %{version}-%{release}

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
%setup -q -n tmux-2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539873510
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1539873510
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tmux
cp COPYING %{buildroot}/usr/share/package-licenses/tmux/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tmux

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tmux/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tmux.1
