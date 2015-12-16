%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name arel

Summary: Arel is a Relational Algebra for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 5.0.0
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/rails/%{gem_name}
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygem(bigdecimal)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(bigdecimal)
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Arel is a Relational Algebra for Ruby. It 1) simplifies the generation complex
of SQL queries and it 2) adapts to various RDBMS systems. It is intended to be
a framework framework; that is, you can build your own ORM with it, focusing
on innovative object and collection modeling as opposed to database
compatibility and query generation.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires:%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
%{?scl:scl enable %scl - << \EOF}
ruby -Ilib:test -e 'Dir.glob "./test/test_*.rb", &method(:require)'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%doc %{gem_instdir}/MIT-LICENSE.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test
%{gem_instdir}/arel.gemspec
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%doc %{gem_docdir}


%changelog
* Wed Jan 14 2015 Vít Ondruch <vondruch@redhat.com> - 5.0.0-2
- Update to arel 5.0.0.

* Thu Mar 20 2014 Vít Ondruch <vondruch@redhat.com> - 4.0.0-2
- Rebuid against new scl-utils to depend on -runtime package.
  Resolves: rhbz#1069109

* Mon Oct 14 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to arel 4.0.0

* Tue Jun 18 2013 Josef Stribny <jstribny@redhat.com> - 3.0.2-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.2-3
- Exclude the cached gem.

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.2-2
- Specfile cleanup

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.2-1
- Rebuilt for scl.
- Updated to 3.0.2.

* Fri Mar 09 2012 Vít Ondruch <vondruch@redhat.com> - 2.0.9-4
- Fix dependency on BigDecimal.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 2.0.9-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.9-1
- Update to Arel 2.0.9
- Removed unnecessary cleanup

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.7-1
- Updated to Arel 2.0.7 
- Removed some build dependencies

* Fri Jan 07 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.6-3
- Move all documentation into subpackage

* Fri Jan 07 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.6-2
- Clean buildroot

* Fri Jan 7 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.6-1
- Initial package
