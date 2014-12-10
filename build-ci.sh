# sh build-ci.sh  --dl-path=/home/pxn/www/dl/java-dep  --yum-path=/home/pxn/www/yum/extras-testing/noarch


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


NAMEo="java-dep-opn"
NAMEr="java-dep-jre"
NAMEd="java-dep-jdk"
[ -z "${WORKSPACE}" ] && WORKSPACE=`pwd`
rm -vf "${WORKSPACE}/${NAMEo}"-*.noarch.rpm
rm -vf "${WORKSPACE}/${NAMEr}"-*.noarch.rpm
rm -vf "${WORKSPACE}/${NAMEd}"-*.noarch.rpm


title "Build.."
( cd "${WORKSPACE}/" && sh build-rpm.sh --build-number ${BUILD_NUMBER} ) || exit 1


title "Deploy.."
cp -fv "${WORKSPACE}/${NAMEo}"-*.noarch.rpm "${DL_PATH}/" || exit 1
cp -fv "${WORKSPACE}/${NAMEr}"-*.noarch.rpm "${DL_PATH}/" || exit 1
cp -fv "${WORKSPACE}/${NAMEd}"-*.noarch.rpm "${DL_PATH}/" || exit 1
# open jdk
latest_version "${DL_PATH}/${NAMEo}-*.noarch.rpm"         || exit 1
echo "Latest version: "${LATEST_FILE}
ln -fs "${LATEST_FILE}" "${YUM_PATH}/${NAMEo}.noarch.rpm" || exit 1
# jre
latest_version "${DL_PATH}/${NAMEr}-*.noarch.rpm"         || exit 1
echo "Latest version: "${LATEST_FILE}
ln -fs "${LATEST_FILE}" "${YUM_PATH}/${NAMEr}.noarch.rpm" || exit 1
# jdk
latest_version "${DL_PATH}/${NAMEd}-*.noarch.rpm"         || exit 1
echo "Latest version: "${LATEST_FILE}
ln -fs "${LATEST_FILE}" "${YUM_PATH}/${NAMEd}.noarch.rpm" || exit 1

