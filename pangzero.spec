Summary:	Pang Zero - clone of Super Pang
Summary(pl):	Pang Zero - klon Super Panga
Name:		pangzero
Version:	0.15
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/pangzero/%{name}-%{version}.tar.gz
# Source0-md5:	3bf5ba7b5b794c68fa39b3f618941ddf
Patch0:		%{name}-SDL.patch
URL:		http://apocalypse.rulez.org/pangzero
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-SDL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pang Zero is a clone and enhancement of Super Pang.

%description -l pl
Pang Zero jest ulepszonym klonem Super Panga.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
