# revision 21539
# category Package
# catalog-ctan /macros/latex/contrib/collcell
# catalog-date 2011-02-27 21:54:29 +0100
# catalog-license lppl1.3
# catalog-version 0.5
Name:		texlive-collcell
Version:	0.5
Release:	1
Summary:	Collect contents of a tabular cell as argument to a macro
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/collcell
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collcell.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collcell.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collcell.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides macros that collect the content of a
tabular cell, and offer them as an argument to a macro. Special
care is taken to remove all aligning macros inserted by tabular
from the cell content. The macros also work in the last column
of a table, but do not support verbatim material inside the
cells.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/collcell/collcell.sty
%doc %{_texmfdistdir}/doc/latex/collcell/collcell.pdf
#- source
%doc %{_texmfdistdir}/source/latex/collcell/Makefile
%doc %{_texmfdistdir}/source/latex/collcell/README
%doc %{_texmfdistdir}/source/latex/collcell/collcell.dtx
%doc %{_texmfdistdir}/source/latex/collcell/collcell.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
