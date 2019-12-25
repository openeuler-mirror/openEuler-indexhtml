%global vendor %{?_vendor:%{_vendor}}%{!?_vendor:openEuler}

Name:        %{vendor}-indexhtml
Version:     7
Release:     14
Source:      HTML.tar.gz
License:     CC-BY-SA
Summary:     Browser default start page for %{vendor}
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes: indexhtml <= 2:5-1
Provides: %{vendor}-indexhtml
Provides: generic-indexhtml

BuildRequires: sed

%description
The indexhtml package contains the welcome page shown by your Web browser,
which you'll see after you've successfully installed %{vendor} Linux

%prep
%setup -q -n HTML

lowercase_os_name=$(echo "%{vendor}" | sed 's/[A-Z]/\l&/g')
sed -i "s/lowercase_generic_os/$lowercase_os_name/g" index.html
sed -i "s/generic_os/%{vendor}/g" index.html

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/en-US
cp -a . $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/
pushd $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/en-US
ln -s ../index.html .
ln -s ../img/ .
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_defaultdocdir}/HTML/*

%changelog
* Mon Dec 23 2019 openEuler Buildteam <buildteam@openeuler.org> - 7-14
- Type:NA
- ID:NA
- SUG:NA
- DESC: delete unneeded provides

* Tue Oct 15 2019 fanghuiyu<fanghuiyu@huawei.com> - 7-13
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: change to generic-indexhtml

* Tue Sep 24 2019 hexiaowen <hexiaowen@huawei.com> - 7-12
- add copyright

* Fri Mar 29 2019 wuyou<wuyou88@huawei.com> - 7-11
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: supply provides of indexhtml

* Mon Mar 25 2019 wuyou<wuyou88@huawei.com> - 7-10
- Type: bugfix
- ID: NA
- SUG: NA
- DESC: Provides openEuler-indexhtml 
