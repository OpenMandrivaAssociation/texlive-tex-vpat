Name:		texlive-tex-vpat
Version:	63560
Release:	1
Summary:	TeX Accessibility Conformance Report
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tex-vpat
License:	cc-by-3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-vpat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-vpat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeX Accessibility Conformance Report based on ITI VPAT(R)
guidelines. Currently it covers TeX Live. Other distributions
can be added if needed.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/tex-vpat

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
