Summary:	Utility for wildcard renaming, copying, etc.
Summary(pl):	Narzêdzie do zmiany nazw i kopiowania wielu plików naraz
Name:		mmv
Version:	1.0.1b
Release:	4
License:	Freeware
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	ftp://ftp.usg.edu/pub/unix/packages/%{name}-%{version}.tar.gz
Patch0:		%{name}-linux.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is mmv, a program to move/copy/append/link multiple files
according to a set of wildcard patterns. This multiple action is
performed safely, i.e. without any unexpected deletion of files due to
collisions of target names with existing filenames or with other
target names. Furthermore, before doing anything, mmv attempts to
detect any errors that would result from the entire set of actions
specified and gives the user the choice of either aborting before
beginning, or proceeding by avoiding the offending parts.

%description -l pl
mmv jest programem do przenoszenia, kopiowania, ³±czenia wielu plików
wed³ug zestawu masek. Czynno¶ci te s± wykonywane bezpiecznie, bez
przypadkowego skasowania plików z powodu konfliktu nazw.

%prep
%setup -q -c
%patch -p1

%build
%{__cc} %{rpmldflags} %{rpmcflags} -DIS_SYSV -DHAS_DIRENT -DHAS_RENAME -o mmv mmv.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mmv $RPM_BUILD_ROOT%{_bindir}
ln -sf mmv $RPM_BUILD_ROOT%{_bindir}/mad
ln -sf mmv $RPM_BUILD_ROOT%{_bindir}/mcp
ln -sf mmv $RPM_BUILD_ROOT%{_bindir}/mln

install mmv.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so mmv.1" > $RPM_BUILD_ROOT%{_mandir}/man1/mad.1
echo ".so mmv.1" > $RPM_BUILD_ROOT%{_mandir}/man1/mcp.1
echo ".so mmv.1" > $RPM_BUILD_ROOT%{_mandir}/man1/mln.1

gzip -9nf ANNOUNCE READ.ME ARTICLE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
