
%define plugin	mailbox
%define name	vdr-plugin-%plugin
%define version	0.5.0
%define rel	3

Summary:	VDR plugin: Display emails of IMAP/POP3 accounts
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://sites.inka.de/~W1222/vdr/
Source:		http://sites.inka.de/~W1222/vdr/download/vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	c-client-devel
BuildRequires:	pam-devel
BuildRequires:	openssl-devel
Requires:	vdr-abi = %vdr_abi

%description
Mailbox is a plugin for the Video Disk Recorder (VDR) by Klaus Schmidinger.

The Mailbox-plugin provides access to multiple e-mail accounts to display the
contained e-mails on the On-Screen-Display (OSD) of the Video Disk Recorder.

This plugin uses the c-client-library of the IMAP server of University of
Washington (UW IMAP) to access e-mail accounts.

As the c-client library supports the IMAP and POP3 protocol the Mailbox-
plugin is able to access both types of mail accounts. Due to the fact that
IMAP provides more features than POP3, several plugin functions are only
available when working with IMAP accounts.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# script to call when number of new mails changes
var=MAILCMD
param="-m MAILCMD"
%vdr_plugin_params_end

%build
# fixes build
VDR_PLUGIN_FLAGS="%vdr_plugin_flags -fno-operator-names"
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY mailcmd.sh


