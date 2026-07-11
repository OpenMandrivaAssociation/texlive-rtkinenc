%global tl_name rtkinenc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Input encoding with fallback procedures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rtkinenc
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rtkinenc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rtkinenc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rtkinenc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The rtkinenc package is functionally similar to the standard LaTeX
package inputenc: both set up active characters so that an input
character outside the range of 7-bit visible ASCII is converted into one
or more corresponding LaTeX commands. The main difference lies in that
rtkinenc allows the user to specify a fallback procedure to use when the
text command corresponding to some input character isn't available.
Names of commands in rtkinenc have been selected so that it can read
inputenc encoding definition files, and the aim is that rtkinenc should
be backwards compatible with inputenc. rtkinenc is not a new version of
inputenc though, nor is it part of standard LaTeX. For an example of how
rtkinenc is used, the user may look at the tclldoc class.

