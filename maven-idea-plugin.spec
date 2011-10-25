Name:           maven-idea-plugin
Version:        2.2
Release:        3
Summary:        Maven IDEA Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-idea-plugin-2.2
# tar caf maven-idea-plugin-2.2.tar.xz maven-idea-plugin-2.2
Source0:        %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: java-devel >= 0:1.6.0
BuildRequires: plexus-utils
BuildRequires: ant-nodeps
BuildRequires: maven2
BuildRequires: maven-wagon
BuildRequires: plexus-container-default
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-shared-plugin-testing-harness
BuildRequires: dom4j
Requires: ant-nodeps
Requires: maven2
Requires: jpackage-utils
Requires: java
Requires(post): jpackage-utils
Requires(postun): jpackage-utils

Obsoletes: maven2-plugin-idea <= 0:2.0.8
Provides: maven2-plugin-idea = 1:%{version}-%{release}

%description
The IDEA Plugin is used to generate files (ipr, iml, and iws) for a
project so you can work on it using the IDE, IntelliJ IDEA.


%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils

%description javadoc
%{summary}.


%prep
%setup -q #You may need to update this according to your Source0

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
# we skip test because even with binary mvn release these fail for
# various reasons.
mvn-jpp -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven.test.skip=true \
        install javadoc:javadoc

%install
rm -rf %{buildroot}

# jars
install -Dpm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}-%{version}.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; \
    do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_to_maven_depmap org.apache.maven.plugins %{name} %{version} JPP %{name}

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
rm -rf target/site/api*

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

