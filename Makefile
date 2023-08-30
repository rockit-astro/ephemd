RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} --define "_version $$(date --utc +%Y%m%d%H%M%S)" -ba rockit-ephemeris.spec
	mv build/noarch/*.rpm .
	rm -rf build

install:
	@cp ephemd /bin/
	@cp ephemd@.service /usr/lib/systemd/system/
	@install -d /etc/ephemd
	@echo ""
	@echo "Installed server, client, and service files."
	@echo "Now copy the relevant json config files to /etc/ephemd/"
