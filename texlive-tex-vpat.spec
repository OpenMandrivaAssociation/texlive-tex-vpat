%global tl_name tex-vpat
%global tl_revision 72067

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	TeX Accessibility Conformance Report
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/tex-vpat
License:	cc-by-3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-vpat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-vpat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX Accessibility Conformance Report based on ITI VPAT(R) guidelines.
Currently it covers TeX Live. Other distributions can be added if
needed.

