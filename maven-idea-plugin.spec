%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-idea-plugin
Version:        2.2
Release:        14.0%{?dist}
Summary:        Maven IDEA Plugin


License:        ASL 2.0
URL:            https://maven.apache.org/plugins/%{name}
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-idea-plugin-2.2
# tar caf maven-idea-plugin-2.2.tar.xz maven-idea-plugin-2.2
Source0:        %{name}-%{version}.tar.xz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

Obsoletes:      maven2-plugin-idea <= 0:2.0.8
Provides:       maven2-plugin-idea = 1:%{version}-%{release}

%description
The IDEA Plugin is used to generate files (ipr, iml, and iws) for a
project so you can work on it using the IDE, IntelliJ IDEA.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q 
cp %{SOURCE1} .
%pom_add_dep org.apache.maven:maven-compat

%build
# we skip test because even with binary mvn release these fail for
# various reasons.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-13
- Simplify build dependencies
- Replace POM patch with POM macro
- Update to current packaging guidelines

* Tue Feb 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-12
- Use default packaging layout

* Tue Feb 12 2013 Michal Srb <msrb@redhat.com> - 2.2-11
- Build with xmvn

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-9
- Add license text to packages (#879379)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 5 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2-6
- Fix working in pure maven 3 environment.

* Fri Jun 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2-5
- Build with maven 3.x

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep  7 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-2
- Add dom4j to BRs

* Fri May 28 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-1
- Initial package
