Summary:	Utility for wildcard renaming, copying, etc
Summary(pl.UTF-8):   Narzędzie do zmiany nazw i kopiowania wielu plików naraz
Name:		mmv
Version:	1.0.1b
Release:	6
License:	Freeware
Group:		Applications/File
Source0:	ftp://ftp.usg.edu/pub/unix/packages/%{name}-%{version}.tar.gz
# Source0-md5:	3bbf82c9e52a35183c5d596ae66fd9bc
Patch0:		%{name}-linux.patch
Patch1:		%{name}-cpp_macros.patch
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

%description -l pl.UTF-8
mmv jest programem do przenoszenia, kopiowania, łączenia wielu plików
według zestawu masek. Czynności te są wykonywane bezpiecznie, bez
przypadkowego skasowania plików z powodu konfliktu nazw z plikami
istniejącymi lub innymi docelowymi. Co więcej, przed wykonaniem
czegokolwiek mmv próbuje wykryć wszelkie błędy, które wynikłyby z
wykonania wszystkich podanych akcji i daje użytkownikowi wybór między
anulowaniem całości operacji lub wykonaniem z pominięciem błędnych
części.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE READ.ME ARTICLE
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
