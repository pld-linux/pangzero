Summary:	Pang Zero - clone of Super Pang
Summary(pl.UTF-8):	Pang Zero - klon Super Panga
Name:		pangzero
Version:	1.2
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/pangzero/%{name}-%{version}.tar.gz
# Source0-md5:	9a6a81636532ca885f7dd5d5308628cc
Source1:	%{name}.desktop
URL:		http://apocalypse.rulez.org/pangzero/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-SDL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pang Zero is a clone of Super Pang, a fast-paced action game that
involves popping balloons with a harpoon. Currently, up to six people
can play together.

%description -l pl.UTF-8
Pang Zero jest klonem Super Panga, szybkiej gry akcji, w której gracz
przebija balony za pomocą harpuna. Aktualnie w grze może uczestniczyć
sześciu graczy.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install data/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/pangzero.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
