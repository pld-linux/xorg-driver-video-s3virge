Summary:	X.org video driver for S3 ViRGE and Trio3D video chips
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych S3 ViRGE i Trio3D
Name:		xorg-driver-video-s3virge
Version:	1.10.7
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3virge-%{version}.tar.bz2
# Source0-md5:	9d4dd8060544d95a1ce7d0ce0853cbe6
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-s3virge < 1:7.0.0
Obsoletes:	XFree86-S3V
Obsoletes:	XFree86-driver-s3virge < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for S3 ViRGE and Trio3D video chips. It supports
PCI and AGP video cards based on the following chips:
- ViRGE (86C325),
- ViRGE VX (86C988),
- ViRGE DX (86C375),
- ViRGE GX (86C385),
- ViRGE GX2 (86C357),
- ViRGE MX (86C260),
- ViRGE MX+ (86C280),
- Trio3D (86C365),
- Trio3D/2X (86C362, 86C368).

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych S3 ViRGE i Trio3D.
Obsługuje karty PCI i AGP oparte na następujących układach:
- ViRGE (86C325),
- ViRGE VX (86C988),
- ViRGE DX (86C375),
- ViRGE GX (86C385),
- ViRGE GX2 (86C357),
- ViRGE MX (86C260),
- ViRGE MX+ (86C280),
- Trio3D (86C365),
- Trio3D/2X (86C362, 86C368).

%prep
%setup -q -n xf86-video-s3virge-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/s3virge_drv.so
%{_mandir}/man4/s3virge.4*
