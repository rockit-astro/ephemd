RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} -ba observatory-ephem-server.spec
	${RPMBUILD} -ba python3-warwick-observatory-ephemeris.spec
	mv build/noarch/*.rpm .
	rm -rf build

install:
	@python3 setup.py install
	@cp ephemd /bin/
	@cp ephemd@.service /usr/lib/systemd/system/
	@install -d /etc/ephemd
	@echo ""
	@echo "Installed server and service files."
	@echo "Now copy the relevant json config files to /etc/ephemd/"
