# original script found at: http://deez.info/2013/05/29/creating-a-virtual-java-rpm/
Name            : java-dep
Summary         : Virtual package provides proper dependency resolution for java packages using OpenJDK or Oracle Java
Version         : %{VERSION}
Release         : %{RELEASE}
BuildArch       : noarch
Provides        : java
Requires        : jre >= %{VERSION}
%define  _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm

Group           : Development/Java Development
License         : None



%description
Some people prefer to run the Oracle JRE/JDK instead of OpenJDK. Oracle provides RPMs named jre-version-linux-x64.rpm and jdk-version-linux-x64.rpm to make installing them easier. Unfortunately, these RPMs do *not* provide the capability java. This means that if you already have the Oracle JRE installed, and you install a RPM which requires the capability java, the OpenJDK will be unnecessarily installed (and might even become the default!). I solved this dilemma by creating a 'virtual' RPM package which provides the capability java by depending on the Oracle JRE.



%install
# delete existing rpm's
%{__rm} -fv "%{_rpmdir}/%{name}-%{version}-"*.noarch.rpm



%clean
if [ ! -z "%{_topdir}" ]; then
	%{__rm} -rf --preserve-root "%{_topdir}" \
		|| echo "Failed to delete build root!"
fi



%prep

%build

%files

%pre

%post

%changelog

