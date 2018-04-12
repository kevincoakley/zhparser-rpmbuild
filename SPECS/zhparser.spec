Name:		zhparser
Version:	0.2.0
Release:	1%{?dist}
Summary:	Zhparser is a PostgreSQL extension for full-text search of Chinese. It implements a Chinese parser base on the Simple Chinese Word Segmentation(SCWS).
License:	BSD
URL:		http://blog.amutu.com/zhparser/
Source0:	https://github.com/amutu/zhparser/archive/v%{version}.tar.gz
BuildRequires:	scws >= 1.2.3, postgresql10, postgresql10-server, postgresql10-libs, postgresql10-devel
Requires:	scws >= 1.2.3, postgresql10, postgresql10-server, postgresql10-libs

%description
Zhparser is a PostgreSQL extension for full-text search of Chinese. It implements a Chinese parser base on the Simple Chinese Word Segmentation(SCWS).

Project home page: http://blog.amutu.com/zhparser/


%prep
%setup

%build
SCWS_HOME=/usr/local PG_CONFIG=/usr/pgsql-10/bin/pg_config make %{?_smp_mflags}


%install
SCWS_HOME=/usr/local PG_CONFIG=/usr/pgsql-10/bin/pg_config make install DESTDIR=%{buildroot}


%files
/usr/pgsql-10/lib/zhparser.so
/usr/pgsql-10/share/extension/zhparser--1.0.sql
/usr/pgsql-10/share/extension/zhparser--unpackaged--1.0.sql
/usr/pgsql-10/share/extension/zhparser.control
/usr/pgsql-10/share/tsearch_data/dict.utf8.xdb
/usr/pgsql-10/share/tsearch_data/rules.utf8.ini


%changelog
* Thu Apr 12 2018 Kevin Coakley <kcoakley@sdsc.edu>
– Initial rpm build
