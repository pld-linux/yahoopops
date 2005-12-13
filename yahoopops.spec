Summary:	YPOPs! - Emulates a POP3/SMTP mail server and provides free access to Yahoo! Mail
Summary(pl):	YPOPs! - emulacja serwera pocztowego POP3/SMTP i swobodny dostêp do Yahoo! Mail
Name:		yahoopops
Version:	0.6
Release:	0.3
License:	GPL v2+ (yp6) / MIME++ Software License Agreement
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/yahoopops/yp6.tar.bz2
# Source0-md5:	1b09ec7493db7589bb9f9428c2d48a12
# ftp://ftp.library.tver.ru/pub/unix/libs/mimepp-1.3.3.tar.gz
%define		_mimepp_ver	1.3.3
Source1:	mimepp-%{_mimepp_ver}.tar.gz
# Source1-md5:	e963dadb38e4dbc9f49368696aad11ca
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-gcc34.patch
URL:		http://yahoopops.sourceforge.net/
BuildRequires:	curl-devel >= 7.11.2
BuildRequires:	libxml-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YPOPs! is an application that provides POP3 access to Yahoo! Mail. It
is available on the Windows, Linux, Solaris and Mac platforms.

Yahoo! Mail disabled free access to its POP3 service on 24th April,
2002. This application emulates a POP3 server and enables popular
email clients like Outlook, Netscape, Eudora, Mozilla, etc., to
download email from Yahoo! accounts. We do not go against the license
agreements of Yahoo! Mail. This application is completely legitimate
and well within the realms of legal software.

How do we do it you ask? Well, this application is more like a
gateway. It provides a POP3 server interface at one end to talk to
email clients and an HTTP client (browser) interface at the other
which allows it to talk to Yahoo!

YPOPs! was inspired by a Perl script called FetchYahoo written by Ravi
Ramkissoon.

%description -l pl
YPOPs! to aplikacja daj±ca dostêp POP3 do us³ugi Yahoo! Mail. Jest
dostêpna na platformach Windows, Linux, Solaris i Mac.

Yahoo! Mail wy³±czy³ swobodny dostêp do us³ugi POP3 24 kwietnia 2002.
Ta aplikacja emuluje serwer POP3 i umo¿liwia popularnym klientom
pocztowym, takim jak Outlook, Netscape, Eudora, Mozilla itp. ¶ci±ganie
poczty z kont Yahoo!. Ten program nie jest sprzeczny z licencj± Yahoo!
Mail, aplikacja jest w pe³ni legalna.

Jak to dzia³a? Aplikacja dzia³a bardziej jako bramka. Dostarcza
interfejs serwera POP3 z jednej strony w celu komunikacji z klientami
pocztowymi oraz interfejs klienta HTTP ("przegl±darkê") z drugiej w
celu komunikacji z Yahoo!.

YPOPs! by³ zainspirowany skryptem Perla o nazwie FetchYahoo napisanym
przez Ravi Ramkissoona.

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ypopsrc
