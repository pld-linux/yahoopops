Summary:	YPOPs!  - Emulates a POP3/SMTP mail server and provides free access to Yahoo! Mail
Name:		yahoopops
Version:	0.6
Release:	0.1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/sourceforge/yahoopops/yp6.tar.bz2
# Source0-md5:	1b09ec7493db7589bb9f9428c2d48a12
# Source0-size:	399620
URL:		http://yahoopops.sourceforge.net/
BuildRequires:	curl-devel
BuildRequires:	libxml-devel
BuildRequires:	openssl-devel
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{name}

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}

export BIN_LOC=%{_bindir}
export LIB_LOC=%{_libdir}
export CONFIG_LOC=%{_sysconfdir}
export CURL_INC="%{_includedir}/curl"
export CURL_LIB="%(curl-config --libs)"
export SSL_INC="%(pkg-config openssl --cflags)"
export SSL_LIB="%(pkg-config openssl --libs)"
export XML_INC="%(xml-config --cflags)"
export XML_LIB="%(xml-config --libs)"

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
#doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
#attr(755,root,root) %{_bindir}/*
#{_datadir}/%{name}
