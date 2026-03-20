Summary:	Ruby FastCGI Library
Summary(pl.UTF-8):	Biblioteka FastCGI dla języka Ruby
Name:		ruby-fcgi
Version:	0.9.2.2
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/fcgi-%{version}.gem
# Source0-md5:	2fd822dcd51814a575f07c5ae269e901
URL:		https://rubygems.org/gems/fcgi
BuildRequires:	fcgi-devel
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
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
BuildArch:	noarch

%description rdoc
HTML documentation for %{name}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{name}.

%package ri
Summary:	ri documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{name}
Group:		Documentation
Requires:	ruby
BuildArch:	noarch

%description ri
ri documentation for %{name}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{name}.

%prep
%setup -q -n fcgi-%{version}

%build
cd ext/fcgi
%{__ruby} extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

cd ../..
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_vendorarchdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
install -p ext/fcgi/fcgi.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rdoc README.signals
%attr(755,root,root) %{ruby_vendorarchdir}/fcgi.so
%{ruby_vendorlibdir}/fcgi.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/FCGI
