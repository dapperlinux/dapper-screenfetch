# dapper-screenfetch

## About
The Dapper Screenfetch package contains a nice unix script that prints decorative system information to the terminal.


## Building
To build this package, first install an RPM development chain:

```bash
$ sudo dnf install fedora-packager fedora-review

```

Next, setup rpmbuild directories with

```bash
$ rpmdev-setuptree
```
And place the file dapper-screenfetch.spec in the SPECS directory, and rename the dapper-screenfetch directory to dapper-screenfetch-3.8.1 and compress it:
```bash
$ mv dapper-screenfetch.spec ~/rpmbuild/SPECS/
$ mv dapper-screenfetch dapper-screenfetch-3.8.1
$ tar -cJvf dapper-screenfetch-3.8.1.tar.xz dapper-screenfetch-3.8.1
$ mv dapper-screenfetch-3.8.1.tar.xz ~/rpmbuild/SOURCES/
```

and finally, you can build RPMs and SRPMs with:
```bash
$ cd ~/rpmbuild/SPECS
$ rpmbuild -ba dapper-screenfetch.spec
```
