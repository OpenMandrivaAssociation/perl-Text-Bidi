%define upstream_name    Text-Bidi
%define upstream_version 2.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Dual-life long arrays
License:    GPL or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Encode)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(List::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Tie::Array)
BuildRequires: perl(base)
BuildRequires: perl(integer)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(version)
BuildRequires: perl(warnings)
BuildRequires: pkgconfig(fribidi)

%description
This module provides basic support for the Unicode bidirectional (Bidi)
text algorithm, for displaying text consisting of both left-to-right and
right-to-left written languages (such as Hebrew and Arabic.) It does so via
a _swig_ interface file to the _libfribidi_ library.

The fundamental purpose of the bidi algorithm is to reorder text given in
logical order into text in visually correct order, suitable for display
using standard printing commands. ``Logical order'' means that the
characters are given in the order in which they would be read if printed
correctly. The direction of the text is determined by properties of the
Unicode characters, usually without additional hints. See the
http://www.unicode.org/unicode/reports/tr9/ manpage for more details on the
problem and the algorithm.

Standard usage
    The bidi algorithm works in two stages. The first is on the level of a
    paragraph, where the direction of each character is computed. The
    second is on the level of the lines to be displayed. The main practical
    difference is that the first stage requires only the text of the
    paragraph, while the second requires knowledge of the width of the
    displayed lines. The module (or the library) does not determine how the
    text is broken into paragraphs.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml LICENSE Changes META.json
%{_bindir}/fribidi.pl
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
