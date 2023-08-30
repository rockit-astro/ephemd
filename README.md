## Ephemeris daemon

`ephemd` calculates the current sun and moon positions for [environmentd](https://github.com/rockit-astro/enivronmentd/).

### Configuration

Configuration is read from json files that are installed by default to `/etc/ephemd`.
A configuration file is specified when launching the server.

```python
{
  "daemon": "observatory_ephemeris", # Run the server as this daemon. Daemon types are registered in `rockit.common.daemons`.
  "latitude": 28.7603135, # Site latitude in degrees.
  "longitude": -17.8796168, # Site longitude in degrees.
  "altitude": 2387 # Site altitude in metres.
}
```

### Initial Installation

The automated packaging scripts will push 3 RPM packages to the observatory package repository:

| Package                       | Description                                                                   |
|-------------------------------|-------------------------------------------------------------------------------|
| rockit-ephemeris-server       | Contains the `ephemd` server and systemd service file.                        |
| rockit-ephemeris-data-lapalma | Contains the json configuration for the La Palma telescopes.                  |
| rockit-ephemeris-data-warwick | Contains the json configuration and udev rules for the Windmill Hill station. |

Alternatively, perform a local installation using `sudo make install`.

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now ephemd@<config>
```

where `config` is the name of the json file for the appropriate unit.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `rockit.common.daemons` for the daemon specified in the config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart ephemd@<config>
```

### Testing Locally

The server can be run directly from a git clone:
```
./ephemd ./warwick.json
```
