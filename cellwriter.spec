%define name    cellwriter
%define version 1.3.4
%define release %mkrel 1

Name:           %{name} 
Summary:        Character-based hardwriting input panel
Version:        %{version} 
Release:        %{release} 
Source0:        http://pub.risujin.org/cellwriter/%{name}-%{version}.tar.gz
Patch0:		cellwriter-1.3.4-fix-str-fmt.patch
URL:            http://risujin.org/cellwriter/ 
Group:          Accessibility
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:        GPL
BuildRequires:  libxtst-devel gtk2-devel libgnome2-devel

%description
CellWriter is a grid-entry natural handwriting input panel. As you write
characters into the cells, your writing is instantly recognized at the
character level. When you press Enter on the panel, the input you entered is
sent to the currently focused application as if typed on the keyboard.

%prep 
%setup -q
%patch0 -p0

%build 
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean 
rm -rf %buildroot

%files 
%defattr(0755,root,root) 
%doc README NEWS COPYING AUTHORS 
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%name
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/scalable/apps/cellwriter.svg
%{_datadir}/applications/*
