%define debug_package %nil

%global forgeurl https://github.com/yang991178/fluent-reader/
Version:	1.1.4
%global tag v%{Version}

%forgemeta

# Exclude private libraries
%global __requires_exclude libffmpeg.so

Name:		fluent-reader
Release:	1%?dist
License:	BSD-3-Clause
Summary:	A modern desktop RSS reader
URL:		%{forgeurl}
Group:		Applications/Internet
Source0:    %{forgesource}

Buildrequires: nodejs

%description %{Summary}

%prep
%forgeautosetup

cat <<EOF > fluent-reader.desktop
[Desktop Entry]
Name=fluent-reader
Comment=%summary
GenericName=RSS reader
Type=Application
Exec=/usr/bin/vencorddesktop
Icon=vesktop
Categories=Network;InstantMessaging;
Terminal=False


EOF


%build
npm install
npm run build
npm run package-linux

%install

mkdir -p %buildroot/usr/share/vesktop
cp -r dist/*-unpacked/. %buildroot/usr/share/vesktop/.

install -Dm755 dist/*-unpacked/vencorddesktop %buildroot/usr/bin/vencorddesktop
ln -sf /usr/share/vesktop/vencorddesktop %buildroot/usr/bin/vencorddesktop
install -Dm644 vesktop.desktop %buildroot/usr/share/applications/vesktop.desktop
install -Dm644 build/icon.png %buildroot/usr/share/pixmaps/vesktop.png

%files
%doc README.md
%doc docs/
%license LICENSE
/usr/bin/vencorddesktop
/usr/share/applications/vesktop.desktop
/usr/share/pixmaps/vesktop.png
/usr/share/vesktop/*
