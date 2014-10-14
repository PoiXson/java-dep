# original script found at: http://deez.info/2013/05/29/creating-a-virtual-java-rpm/



JAVA_VERSION="1.7"
SPEC_FILE="java-dep.spec"



# load build_utils.sh script
if [ -e build_utils.sh ]; then
	source ./build_utils.sh
elif [ -e /usr/local/bin/pxn/build_utils.sh ]; then
	source /usr/local/bin/pxn/build_utils.sh
else
	wget https://raw.githubusercontent.com/PoiXson/shellscripts/master/pxn/build_utils.sh \
		|| exit 1
	source ./build_utils.sh
fi



# build rpm
rpmbuild -bb \
	--define="_topdir ${BUILD_ROOT}" \
	--define="_tmppath ${BUILD_ROOT}/tmp" \
	--define="_rpmdir ${OUTPUT_DIR}" \
	--define="JAVA_VERSION ${JAVA_VERSION}" \
	--define="BUILD_NUMBER ${BUILD_NUMBER}" \
	"${BUILD_ROOT}/SPECS/${SPEC_FILE}" \
		|| exit 1

