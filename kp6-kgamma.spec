#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.3.0
%define		qtver		5.15.2
%define		kpname		kgamma
Summary:	kgamma
Name:		kp6-kgamma
Version:	6.3.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/kgamma-%{version}.tar.xz
# Source0-md5:	d9f49526bbe624b4d8d6b6f90f891f5b
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 1.4.0
BuildRequires:	kf6-kdoctools-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xz
Obsoletes:	kp6-kgamma5 < 5.93.0
Obsoletes:	kp5-%{kpname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a tool for monitor gamma correction. With proper gamma
settings, your display (websites, images, etc.) will look the same on
your monitor as on other monitors. It allows you to alter the
monitor's gamma correction of the X-Server. But that's not all to do.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcminit/kcm_kgamma_init.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kgamma.so
%{_desktopdir}/kcm_kgamma.desktop
%{_datadir}/kgamma
