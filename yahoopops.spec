Summary:	YPOPs! - Emulates a POP3/SMTP mail server and provides free access to Yahoo! Mail
Summary(pl):	YPOPs! - emulacja serwera pocztowego POP3/SMTP i swobodny dostêp do Yahoo! Mail
Name:		yahoopops
Version:	0.6
Release:	0.3
License:	GPL v2+ (yp6) / MIME++ Software License Agreement
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/yahoopops/yp6.tar.bz2
# Source0-md5:	1b09ec7493db7589bb9f9428c2d48a12
# Source0-size:	399620
# ftp://ftp.library.tver.ru/pub/unix/libs/mimepp-1.3.3.tar.gz
%define		_mimepp_ver	1.3.3
Source1:	mimepp-%{_mimepp_ver}.tar.gz
# Source1-md5:	e963dadb38e4dbc9f49368696aad11ca
# Source1-size:	353943
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-gcc34.patch
URL:		http://yahoopops.sourceforge.net/
BuildRequires:	curl-devel >= 7.11.2
BuildRequires:	libxml-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{name} -a1
%patch0 -p1
%patch1 -p1

%build
export BIN_LOC=%{_bindir}
export LIB_LOC=%{_libdir}
export CONFIG_LOC=%{_sysconfdir}
export CURL_INC="%{_includedir}/curl"
export CURL_LIB="%(curl-config --libs)"
export SSL_INC="%(pkg-config openssl --cflags)"
export SSL_LIB="%(pkg-config openssl --libs)"
export XML_INC="%(xml-config --cflags)"
export XML_LIB="%(xml-config --libs)"
export MIMEPP="$PWD/mimepp-%{_mimepp_ver}"

export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"

cd src
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D src/ypops \
	$RPM_BUILD_ROOT%{_bindir}/ypops
install -D src/ypops_samplerc \
	$RPM_BUILD_ROOT%{_sysconfdir}/ypopsrc

mv mimepp-%{_mimepp_ver}/{License.txt,mimepp-license.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/{credits.txt,history.txt} mimepp-%{_mimepp_ver}/mimepp-license.txt
%attr(755,root,root) %{_bindir}/ypops
%{_sysconfdir}/ypopsrc
