Summary:	Download file manager (official core)
Summary(pl):	¦ci±gacz plików (oficjalny)
Name:		edonkeyclc
Version:	1.0.2
Release:	1
License:	unknown
Group:		Applications/Communications
Source0:	http://www.zen18864.zen.co.uk/edonkey/1.0.2/%{name}-%{version}_i386.tgz
# Source0-md5:	21524c499fb95190f86913890e678a48
Source1:	edonkey2k-core.sh
URL:		http://ed2k-gtk-gui.sourceforge.net/core.shtml
Provides:	eDonkey-core
Obsoletes:	edonkey2k-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Download file manager hosted by http://www.edonkey2000.com/

%description -l pl
¦ci±gacz plików z http://www.edonkey2000.com/

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

install usr/bin/edonkeyclc 			$RPM_BUILD_ROOT%{_bindir}
install usr/share/edonkeyclc/server.met 	$RPM_BUILD_ROOT%{_datadir}/%{name}
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
%attr(644,root,root) %{_datadir}/%{name}/server.met
%attr(644,root,root) %{_datadir}/%{name}/contact.dat
