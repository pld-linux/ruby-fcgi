%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby FastCGI Library
Summary(pl):	Biblioteka FastCGI dla jêzyka Ruby
Name:		ruby-fcgi
Version:	0.8.5
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.moonwolf.com/ruby/archive/%{name}-%{version}.tar.gz
# Source0-md5:	896007e727153c6d05c380dd2d7fb109
Patch0:		%{name}-dirs.patch
URL:		http://rwiki.moonwolf.com/rw-cgi.cgi?cmd=view;name=fcgi
BuildRequires:	ruby
BuildRequires:	fcgi-devel
BuildArch:	noarch
Obsoletes:	ruby-fcgi-minero
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby FastCGI Library.

%description -l pl
Biblioteka FastCGI dla jêzyka Ruby.

%prep
%setup -q
%patch0 -p1

%build
ruby install.rb config --site-ruby=%{ruby_rubylibdir} --so-dir=%{ruby_archdir}
ruby install.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby install.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/fcgi.rb
%attr(755,root,root) %{ruby_archdir}/fcgi.so
