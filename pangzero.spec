Summary:	Pang Zero - clone of Super Pang
Summary(pl):	Pang Zero - klon Super Panga
Name:		pangzero
Version:	0.13
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/pangzero/%{name}-%{version}.tar.gz
# Source0-md5:	eec0717ecbb1cf0a78211f2ef2ca688b
Patch0:		%{name}-SDL.patch
URL:		http://apocalypse.rulez.org/pangzero
BuildRequires:	perl-SDL
BuildRequires:	autoconf
BuildRequires:	automake
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