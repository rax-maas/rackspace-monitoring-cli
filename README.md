# Rackspace Monitoring CLI

Command line utility for rackspace-monitoring library.

## Installation

Utility can be installed using `pip`:

```bash
sudo pip install rackspace-monitoring-cli
```

Note: If you don't use a virtual environment the library needs to be installed
under the user which has a write permission to `/usr/local/bin` where the script
files are installed.

## Settings Credentials

Credentials can be set in a configuration file (`~/.raxrc`) or you can pass
them manually to each command.

### Example configuration file

```
[api]
url=http://www.test.com/v1.0

[credentials]
username=foo
api_key=bar
```

# Certificate verification

Libcloud verifies server SSL certificate by default. This means you need to
have the correct CA certificate files installed on your computer for this
library to work.

If Libcloud cannot find CA ertificate files, you will see an error similar to
the one bellow:

`"RuntimeError: No CA Certificates were found in CA_CERTS_PATH."`

This can be addresses by installing the CA certificate files. Bellow you can
find the names of the packages which include CA certificate files.

* **openssl** on CentOS/Fedora (yum)
* **ca-certificates** on Debian/Ubuntu/Arch/Gentoo (apt-get)
* **ca_root_nss** on FreeBSD (ports)
* **curl-ca-bundle** on Mac OS X (ports)

## Using bash completion

`source contrib/optcomplete.sh`

## Usage

### General

`command [--username=<username>] [--api-key=<api key>] [..options..]`

## View available options

`command --help`

### Specifying lists and dictionaries

#### List

Use a comma delimited string. For example:

`raxmon-checks-create --monitoring-zones=mzA,mzB,mzC`

#### Dictionary

Use a comma delimited string of key=value pairs. For example

`raxmon-entities-create --metadata="location=server room,tag=foobar"`

## Commands

### List

* `raxmon-monitoring-zones-list [--details]`
* `raxmon-entities-list [--details]`
* `raxmon-checks-list --entity-id=<enId> [--details]`
* `raxmon-alarms-list --entity-id=<enId> [--details]`
* `raxmon-check-types-list [--details]`
* `raxmon-notifications-list [--details]`
* `raxmon-notification-types-list [--details]`
* `raxmon-alarm-changelogs-list [--details]`
* `raxmon-audits-list [--details]`
* `raxmon-limits-list [--details]`

### Create

* `raxmon-entities-create --label=<label> --ip_address=<ip1=127.0.0.1,ip2=127.0.0.2>
                        --metadata=<foo=bar,bar=foo>`
* `raxmon-checks-create --label=<label> --type=<check type>
                      --monitoring-zones=<monitoring zones>
                      --details=<details>
                      [--target-alias=<target alias>]
                      [--target-resolver=<target resolver>]
                      [--timeout=<timeout>]
                      [--period=<period>]`
* `raxmon-alarms-create --entity-id=<entity id>
                      --criteria=<criteria>
                      --notification-plan-id=<notification plan id>
                      [--check-type=<check type>]
                      [--check-id=<check id>]`
* `raxmon-notifications-create --label
                      --type=<type>
                      --details=<details>`
* `raxmon-notification-plans-create --label=<label>
                      [--critical-state=<critical state notification object ids>]
                      [--warning-state=<warning state notification object ids>]
                      [--ok-state=<ok state notification object ids>]`

### Update

* `raxmon-entities-update --id=<entity id> [--label=<label>]
                        [--ip_address=<ip1=127.0.0.1,ip2=127.0.0.2>]
                        [--metadata=<foo=bar,bar=foo>]`
* `raxmon-checks-update --entity-id=<entity id> --id=<check id>
                      [--label=<label>] [--type=<check type>]
                      [--monitoring-zones=<monitoring zones>]
                      [--details=<details>]
                      [--target-alias=<target alias>]
                      [--target-resolver=<target resolver>]
                      [--timeout=<timeout>]
                      [--period=<period>]`
* `raxmon-alarms-update --entity-id=<entity id>
                      --id=<alarm id>\
                      [--criteria=<criteria>]
                      [--notification-plan-id=<notification plan id>]
                      [--check-type=<check type>]
                      [--check-id=<check id>]`
* `raxmon-notifications-update --id=<notification id>
                      [--label=<label>]
                      [--type=<type>]
                      [--details=<details>]`
* `raxmon-notification-plans-update --id=<notification plan id>
                      [--label=<label>]
                      [--critical-state=<critical state notification object ids>]
                      [--warning-state=<warning state notification object ids>]
                      [--ok-state=<ok state notification object ids>]`

### Delete

* `raxmon-entities-delete --id=<entity id> [--delete-children]`
* `raxmon-checks-delete --entity-id=<parent entity id> --id=<check id>`
* `raxmon-alarms-delete --entity-id=<parent entity id> --id=<alarm id>`
* `raxmon-notifications-delete --id=<notification id>`
* `raxmon-notification-plans-delete --id=<notification plan id>`

### Other

* `raxmon-views-overview`

# Issues, Feedback

Please use Github issue tracker or send an email to `cmbeta@rackspace.com`.
