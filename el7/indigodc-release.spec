Name: indigodc-release
Version: 2.0.0
Release: 1%{?dist}
Summary: INDIGO-1 (MidnightBlue) Release
License: Apache Software License
Source: %{name}-%{version}.src.tgz
Vendor: INDIGO - DataCloud
Group: System Environment/Libraries
BuildArch: noarch
Requires: yum-protectbase
Requires: yum-priorities
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
#BuildRoot: %{_tmppath}/%{name}-%{version}-build


%description
INDIGO - DataCloud repository files

%prep
%setup -q

%build
#Nothing to build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf ${buildroot}

%post
if [ -f /etc/yum/pluginconf.d/priorities.conf ]; then grep -q -e "check_obsoletes" /etc/yum/pluginconf.d/priorities.conf || sed -i -e "/^\[main\]/{G;s/$/\# added by the indigodc-release package\\ncheck_obsoletes = 1/;}" /etc/yum/pluginconf.d/priorities.conf; fi

%postun
if [ "$1" = "0" ]; then grep -q -e "indigodc-release" /etc/yum/pluginconf.d/priorities.conf && sed -i '/indigodc-release/d;/check_obsoletes/d' /etc/yum/pluginconf.d/priorities.conf; fi

%files
%defattr(-,root,root,-)

/etc/indigodc-release
/etc/pki/rpm-gpg/RPM-GPG-KEY-indigodc
/etc/yum.repos.d/indigo2-base.repo
/etc/yum.repos.d/indigo2-third-party.repo
/etc/yum.repos.d/indigo2-updates.repo

%changelog
* Sun Jul 31 2016 Cristina Aiftimiei <aiftim@cnaf.infn.it>
- first release

