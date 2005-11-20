Summary:	X.org video driver for S3 ViRGE and Trio3D video chips
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych S3 ViRGE i Trio3D
Name:		xorg-driver-video-s3virge
Version:	1.8.6.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/driver/xf86-video-s3virge-%{version}.tar.bz2
# Source0-md5:	f85f8d129c0ae2f92d53372e81c0d6a3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for S3 ViRGE and Trio3D video chips. It supports
PCI and AGP video cards based on the following chips: ViRGE (86C325),
ViRGE VX (86C988), ViRGE DX (86C375), ViRGE GX (86C385), ViRGE GX2
(86C357), ViRGE MX (86C260), ViRGE MX+ (86C280), Trio3D (86C365),
Trio3D/2X (86C362, 86C368).

%description -l pl
Sterownik obrazu X.org dla uk³adów graficznych S3 ViRGE i Trio3D.
Obs³uguje karty PCI i AGP oparte na nastêpuj±cych uk³adach: ViRGE
(86C325), ViRGE VX (86C988), ViRGE DX (86C375), ViRGE GX (86C385),
ViRGE GX2 (86C357), ViRGE MX (86C260), ViRGE MX+ (86C280), Trio3D
(86C365), Trio3D/2X (86C362, 86C368).

%prep
%setup -q -n xf86-video-s3virge-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO_NOTES
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/s3virge_drv.so
%{_mandir}/man4/s3virge.4x*
