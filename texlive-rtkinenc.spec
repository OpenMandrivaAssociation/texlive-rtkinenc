Name:		texlive-rtkinenc
Version:	20003
Release:	2
Summary:	Input encoding with fallback procedures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rtkinenc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rtkinenc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rtkinenc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rtkinenc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The rtkinenc package is functionally similar to the standard
LaTeX package inputenc: both set up active characters so that
an input character outside the range of 7-bit visible ASCII is
coverted into one or more corresponding LaTeX commands. The
main difference lies in that rtkinenc allows the user to
specify a fallback procedure to use when the text command
corresponding to some input character isn't available. Names of
commands in rtkinenc have been selected so that it can read
inputenc encoding definition files, and the aim is that
rtkinenc should be backwards compatible with inputenc. rtkinenc
is not a new version of inputenc though, nor is it part of
standard LaTeX. For an example of how rtkinenc is used, the
user may look at the tclldoc class.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rtkinenc/rtkinenc.sty
%doc %{_texmfdistdir}/doc/latex/rtkinenc/README.txt
%doc %{_texmfdistdir}/doc/latex/rtkinenc/rtkinenc-doc.pdf
%doc %{_texmfdistdir}/doc/latex/rtkinenc/rtkinenc-doc.tex
#- source
%doc %{_texmfdistdir}/source/latex/rtkinenc/rtkinenc.dtx
%doc %{_texmfdistdir}/source/latex/rtkinenc/rtkinenc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
