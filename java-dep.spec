Name            : java-dep
Summary         : Virtual package provides proper dependency resolution for java packages using Oracle Java
Version         : 1.8.%{BUILD_NUMBER}
Release         : 2
BuildArch       : noarch
%define  _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm

Group           : Development/Java Development
License         : None
Packager        : PoiXson <support@poixson.com>
URL             : http://deez.info/2013/05/29/creating-a-virtual-java-rpm/



### Packages ###
%package opn
Summary         : Virtual package provides proper dependency resolution for OpenJDK (provides: jdk)
Requires        : java-openjdk >= 1.8
Provides        : java, jre, jdk

%package jre
Summary         : Virtual package provides proper dependency resolution for Oracle Java Runtime Environment (jre)
Requires        : jre >= 1.8
Requires        : jaxp_parser_impl
Provides        : java, jre

%package jdk
Summary         : Virtual package provides proper dependency resolution for Oracle Java Development Kit (jdk)
Requires        : jdk >= 1.8
Requires        : jaxp_parser_impl
Provides        : java, jre, jdk



%description
Some people prefer to run the Oracle JRE/JDK instead of OpenJDK. Oracle provides RPMs named jre-version-linux-x64.rpm and jdk-version-linux-x64.rpm to make installing them easier. Unfortunately, these RPMs do *not* provide the capability 'java'. Likewise, the OpenJDK package contains the jdk, however doesn't provide proper dependency resolution. This means that if you already have the Oracle JRE installed, and you install a RPM which requires the capability 'java', the OpenJDK will be unnecessarily installed (and might even become the default!). We can solve this dilemma by creating a virtual RPM package which provides the capability 'java' by depending on the Oracle JRE, or provides 'jdk' by depending on the OpenJDK. Original script found at: http://deez.info/2013/05/29/creating-a-virtual-java-rpm/

%description opn
Some people prefer to run the Oracle JRE/JDK instead of OpenJDK. Oracle provides RPMs named jre-version-linux-x64.rpm and jdk-version-linux-x64.rpm to make installing them easier. Unfortunately, these RPMs do *not* provide the capability 'java'. Likewise, the OpenJDK package contains the jdk, however doesn't provide proper dependency resolution. This means that if you already have the Oracle JRE installed, and you install a RPM which requires the capability 'java', the OpenJDK will be unnecessarily installed (and might even become the default!). We can solve this dilemma by creating a virtual RPM package which provides the capability 'java' by depending on the Oracle JRE, or provides 'jdk' by depending on the OpenJDK.

%description jre
Some people prefer to run the Oracle JRE/JDK instead of OpenJDK. Oracle provides RPMs named jre-version-linux-x64.rpm and jdk-version-linux-x64.rpm to make installing them easier. Unfortunately, these RPMs do *not* provide the capability 'java'. Likewise, the OpenJDK package contains the jdk, however doesn't provide proper dependency resolution. This means that if you already have the Oracle JRE installed, and you install a RPM which requires the capability 'java', the OpenJDK will be unnecessarily installed (and might even become the default!). We can solve this dilemma by creating a virtual RPM package which provides the capability 'java' by depending on the Oracle JRE, or provides 'jdk' by depending on the OpenJDK.

%description jdk
Some people prefer to run the Oracle JRE/JDK instead of OpenJDK. Oracle provides RPMs named jre-version-linux-x64.rpm and jdk-version-linux-x64.rpm to make installing them easier. Unfortunately, these RPMs do *not* provide the capability 'java'. Likewise, the OpenJDK package contains the jdk, however doesn't provide proper dependency resolution. This means that if you already have the Oracle JRE installed, and you install a RPM which requires the capability 'java', the OpenJDK will be unnecessarily installed (and might even become the default!). We can solve this dilemma by creating a virtual RPM package which provides the capability 'java' by depending on the Oracle JRE, or provides 'jdk' by depending on the OpenJDK.



%install
# delete existing rpm's
%{__rm} -fv "%{_rpmdir}/%{name}-"*.noarch.rpm



%clean
if [ ! -z "%{_topdir}" ]; then
	%{__rm} -rf --preserve-root "%{_topdir}" \
		|| echo "Failed to delete build root (probably fine..)"
fi



%files opn
%files jre
%files jdk

