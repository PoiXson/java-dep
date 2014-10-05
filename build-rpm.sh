# original script found at: http://deez.info/2013/05/29/creating-a-virtual-java-rpm/
clear



VERSION="1.7"
RELEASE="1"



PWD=`pwd`
SOURCE_ROOT="${PWD}"
BUILD_ROOT="${PWD}/rpmbuild-root"

SPEC_FILE="java-dep.spec"
OUTPUT_RPM="java-dep-%%{version}-%%{release}.noarch.rpm"



# ensure rpmbuild tool is available
which rpmbuild >/dev/null || { echo "rpmbuild not installed - yum install rpmdevtools"; exit 1; }
# ensure .spec file exists
[[ -f "${SPEC_FILE}" ]] || { echo "Spec file ${SPEC_FILE} not found!"; exit 1; }



# build space
for dir in BUILD RPMS SOURCE SPECS SRPMS tmp ; do
	if [ -d "${BUILD_ROOT}/${dir}" ]; then
		rm -rf --preserve-root "${BUILD_ROOT}/${dir}" \
			|| exit 1
	fi
	mkdir -p "${BUILD_ROOT}/${dir}" \
		|| exit 1
done

# copy .spec file
cp "${SPEC_FILE}" "${BUILD_ROOT}/SPECS/" \
	|| exit 1



# build rpm
rpmbuild -bb \
	--define="_topdir ${BUILD_ROOT}" \
	--define="_tmppath ${BUILD_ROOT}/tmp" \
	--define="VERSION ${VERSION}" \
	--define="RELEASE ${RELEASE}" \
	--define="_rpmfilename ${OUTPUT_RPM}" \
	"${BUILD_ROOT}/SPECS/${SPEC_FILE}" \
		|| exit 1


