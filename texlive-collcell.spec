# revision 21539
# category Package
# catalog-ctan /macros/latex/contrib/collcell
# catalog-date 2011-02-27 21:54:29 +0100
# catalog-license lppl1.3
# catalog-version 0.5
Name:		texlive-collcell
Version:	0.5
Release:	9
Summary:	Collect contents of a tabular cell as argument to a macro
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/collcell
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collcell.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collcell.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collcell.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros that collect the content of a
tabular cell, and offer them as an argument to a macro. Special
care is taken to remove all aligning macros inserted by tabular
from the cell content. The macros also work in the last column
of a table, but do not support verbatim material inside the
cells.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5-2
+ Revision: 750334
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5-1
+ Revision: 718092
- texlive-collcell
- texlive-collcell
- texlive-collcell
- texlive-collcell
- texlive-collcell

