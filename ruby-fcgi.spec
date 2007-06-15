# TODO: optflags
Summary:	Ruby FastCGI Library
Summary(pl.UTF-8):	Biblioteka FastCGI dla języka Ruby
Name:		ruby-fcgi
Version:	0.8.7
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.moonwolf.com/ruby/archive/%{name}-%{version}.tar.gz
# Source0-md5:	fe4d4a019785e8108668a3e81a5df5e1
URL:		http://sugi.nemui.org/prod/ruby-fcgi/
BuildRequires:	fcgi-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8.4
Obsoletes:	ruby-fcgi-minero
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby FastCGI Library.

%description -l pl.UTF-8
Biblioteka FastCGI dla języka Ruby.

%prep
%setup -q

%build
ruby install.rb config --site-ruby=%{ruby_rubylibdir} --so-dir=%{ruby_archdir}
ruby install.rb setup

mkdir rdoc

rdoc -o rdoc/c ext/*
rdoc -o rdoc/ruby lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby install.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/fcgi.rb
%attr(755,root,root) %{ruby_archdir}/fcgi.so
