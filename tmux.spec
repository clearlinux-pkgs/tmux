#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tmux
Version  : 2.2
Release  : 16
URL      : https://github.com/tmux/tmux/releases/download/2.2/tmux-2.2.tar.gz
Source0  : https://github.com/tmux/tmux/releases/download/2.2/tmux-2.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : ISC
Requires: tmux-bin
Requires: tmux-doc
BuildRequires : pkgconfig(libevent)
BuildRequires : pkgconfig(ncurses)

%description
Welcome to tmux!
tmux is a "terminal multiplexer", it enables a number of terminals (or windows)
to be accessed and controlled from a single terminal. tmux is intended to be a
simple, modern, BSD-licensed alternative to programs such as GNU screen.

%package bin
Summary: bin components for the tmux package.
Group: Binaries

%description bin
bin components for the tmux package.


%package doc
Summary: doc components for the tmux package.
Group: Documentation

%description doc
doc components for the tmux package.


%prep
%setup -q -n tmux-2.2

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tmux

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
