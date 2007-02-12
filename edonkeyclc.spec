Summary:	Download file manager (official core)
Summary(pl.UTF-8):   Ściągacz plików (oficjalny)
Name:		edonkeyclc
Version:	1.1.0
Release:	1
License:	unknown
Group:		Applications/Communications
Source0:	http://www.zen18864.zen.co.uk/edonkey/%{version}/%{name}-%{version}_i386.tgz
# Source0-md5:	943d92390f63b349853f1847109c1a47
Source1:	edonkey2k-core.sh
Source2:	http://www.edonkey.com/server.met
URL:		http://ed2k-gtk-gui.sourceforge.net/core.shtml
Provides:	eDonkey-core
Obsoletes:	edonkey2k-core
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Download file manager hosted by http://www.edonkey2000.com/

%description -l pl.UTF-8
Ściągacz plików z http://www.edonkey2000.com/

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

install usr/bin/edonkeyclc 			$RPM_BUILD_ROOT%{_bindir}
install %{SOURCE2}			 	$RPM_BUILD_ROOT%{_datadir}/%{name}
install usr/share/edonkeyclc/contact.dat	$RPM_BUILD_ROOT%{_datadir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/edonkey-conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo""
echo "Please type edonkey-conf, when you'll be logged as user"
echo "It will prepare your donkey to use with ed2k :)"
echo ""
echo "You may also type overnet-conf, it will prepare overnet-core"
echo "to use with ed2k, more info at http://www.overnet.com/"
echo ""

%files
%defattr(644,root,root,755)
%doc usr/share/doc/%{name}/ChangeLog usr/share/doc/%{name}/README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/server.met
%{_datadir}/%{name}/contact.dat
