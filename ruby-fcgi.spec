# TODO: optflags
Summary:	Ruby FastCGI Library
Summary(pl.UTF-8):	Biblioteka FastCGI dla języka Ruby
Name:		ruby-fcgi
Version:	0.8.7
Release:	10
License:	GPL
Group:		Development/Libraries
Source0:	http://www.moonwolf.com/ruby/archive/%{name}-%{version}.tar.gz
# Source0-md5:	fe4d4a019785e8108668a3e81a5df5e1
Patch0:		%{name}-ruby1.9.patch
URL:		http://sugi.nemui.org/prod/ruby-fcgi/
BuildRequires:	fcgi-devel
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.729
BuildRequires:	ruby-devel >= 1:1.8.4
BuildRequires:	setup.rb >= 3.4.1-6
Obsoletes:	ruby-fcgi-minero
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby FastCGI Library.

%description -l pl.UTF-8
Biblioteka FastCGI dla języka Ruby.

%package rdoc
Summary:	HTML documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{name}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description rdoc
HTML documentation for %{name}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{name}.

%package ri
Summary:	ri documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{name}
Group:		Documentation
Requires:	ruby
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description ri
ri documentation for %{name}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{name}.

%prep
%setup -q
%patch0 -p1

cp %{_datadir}/setup.rb .

%build
%{__ruby} setup.rb config \
	--site-ruby=%{ruby_vendorlibdir} \
	--so-dir=%{ruby_vendorarchdir}

%{__ruby} setup.rb setup

rdoc --ri --op ri lib ext
rdoc --op rdoc lib ext
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_ridir},%{ruby_rdocdir}}
%{__ruby} setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_vendorarchdir}/fcgi.so
%{ruby_vendorlibdir}/fcgi.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/FCGI
