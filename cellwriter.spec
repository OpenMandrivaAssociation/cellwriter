#define debug_package %{nil}

Name:           cellwriter
Summary:        Character-based hardwriting input panel
Version:        1.3.6
Release:        1
Source0:        https://github.com/risujin/cellwriter/archive/%{version}/%{name}-%{version}.tar.gz
URL:            https://risujin.org/cellwriter/ 
Group:          Accessibility
License:        GPLv2
BuildRequires:   pkgconfig(xtst)
BuildRequires:   pkgconfig(gdk-2.0)
BuildRequires:   pkgconfig(libgnome-2.0)

%description
CellWriter is a grid-entry natural handwriting input panel. As you write
characters into the cells, your writing is instantly recognized at the
character level. When you press Enter on the panel, the input you entered is
sent to the currently focused application as if typed on the keyboard.

%prep 
%setup -q


%build 
%configure
%make_build LIBS="$LIBS -lX11 -lm -lXtst"

%install
%make_install


%files  
%doc README NEWS COPYING AUTHORS 
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%name
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/scalable/apps/cellwriter.svg
%{_datadir}/applications/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-5mdv2011.0
+ Revision: 610129
- rebuild

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 1.3.4-4mdv2010.1
+ Revision: 541555
- fix perm

* Tue Feb 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.4-3mdv2010.1
+ Revision: 502678
- fix licence

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.3.4-2mdv2010.0
+ Revision: 436989
- rebuild

* Sun Mar 15 2009 Funda Wang <fwang@mandriva.org> 1.3.4-1mdv2009.1
+ Revision: 355280
- New version 1.3.4

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.2.4-3mdv2009.0
+ Revision: 243472
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Oct 18 2007 Austin Acton <austin@mandriva.org> 1.2.4-1mdv2008.1
+ Revision: 99984
- fix buildrequires
- import cellwriter



