# revision 20003
# category Package
# catalog-ctan /macros/latex/contrib/rtkinenc
# catalog-date 2010-10-04 11:23:12 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-rtkinenc
Version:	1.0
Release:	6
Summary:	Input encoding with fallback procedures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rtkinenc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rtkinenc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rtkinenc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rtkinenc.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755765
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719469
- texlive-rtkinenc
- texlive-rtkinenc
- texlive-rtkinenc
- texlive-rtkinenc

