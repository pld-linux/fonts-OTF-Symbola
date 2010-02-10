# TODO:
# - pl description
Summary:	Free UCS font with various Unicode symbols
Summary(pl.UTF-8):	Wolnodostępny font UCS z różnymi symbolami unikodu
Name:		fonts-OTF-Symbola
Version:	2.53
%define	_ver	%(echo %{version} | tr -d .)
Release:	1
License:	Freeware
Group:		Fonts
Source0:	http://users.teilar.gr/~g1951d/Symbola%{_ver}.zip
# Source0-md5:	06554e9d579a954221f24b1842306fc5
URL:		http://users.teilar.gr/~g1951d/
BuildRequires:	iconv
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		otffontsdir	%{_fontsdir}/OTF

%description
Symbola covers the following scripts and symbols supported by The
Unicode Standard 5.2:

Basic Latin, Latin-1 Supplement, Latin Extended-A, IPA Extensions,
Spacing Modifier Letters, Greek and Coptic, Cyrillic, Cyrillic
Supplementary, General Punctuation, Superscripts and Subscripts,
Combining Diacritical Marks for Symbols, Letterlike Symbols, Number
Forms, Arrows, Mathematical Operators, Miscellaneous Technical,
Control Pictures, Optical Character Recognition, Box Drawing, Block
Elements, Geometric Shapes, Miscellaneous Symbols, Dingbats,
Miscellaneous Mathematical Symbols-A, Supplemental Arrows-A,
Supplemental Arrows-B, Miscellaneous Mathematical Symbols-B,
Supplemental Mathematical Operators, Miscellaneous Symbols and Arrows,
Supplemental Punctuation, CJK Symbols and Punctuation, Yijing Hexagram
Symbols, Vertical Forms, Combining Half Marks, CJK Compatibility
Forms, Specials, Tai Xuan Jing Symbols, Counting Rod Numerals,
Mathematical Alphanumeric Symbols, Mahjong Tile Symbols, Domino Tile
Symbols.

%prep
%setup -qc

%build
for i in *.txt; do
	iconv -f utf16 -t utf8 < $i > $i.
	mv -f $i. $i
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{otffontsdir}

install *.otf $RPM_BUILD_ROOT%{otffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc *.txt
%{otffontsdir}/Symbola.otf
