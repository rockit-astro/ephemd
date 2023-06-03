## Ephemeris daemon

`ephemd` calculates the current sun and moon positions for [environmentd](https://github.com/warwick-one-metre/enivronmentd/).

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the observatory software architecture and instructions for developing and deploying the code.

### Software setup
After installing `observatory-ephem-server`, the `ephemd` must be enabled using:
```
sudo systemctl enable ephemd@lapalma.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start ephemd@lapalma.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9029/tcp --permanent
sudo firewall-cmd --reload
```
