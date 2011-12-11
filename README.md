# Libcloud Monitoring CLI

Command line utility for rackspace-monitoring library.

## Installation

pip install rackspace-monitoring-cli

## Commands

### List

* `lcmon-monitoring-zones-list [--details]`
* `lcmon-entities-list [--details]`
* `lcmon-checks-list --entity-id=<enId> [--details]`
* `lcmon-alarms-list --entity-id=<enId> [--details]`
* `lcmon-check-types-list [--details]`
* `lcmon-notifications-list [--details]`
* `lcmon-notification-types-list [--details]`
* `lcmon-alarm-changelogs-list [--details]`
* `lcmon-audits-list [--details]`
* `lcmon-list-limits [--details]`

### Create

* `lcmon-entities-create --label=<label> --ip_address=<ip1=127.0.0.1,ip2=127.0.0.2> \
                        --metadata=<foo=bar,bar=foo>`
* `lcmon-checks-create --label=<label> --type=<check type> \
                      --monitoring-zones=<monitoring zones> \
                      --details=<details> \
                      [--target-alias=<target alias>] \
                      [--target-resolver=<target resolver>] \
                      [--timeout=<timeout>] \
                      [--period=<period>]`
* `lcmon-alarms-create --entity-id=<entity id> \
                      --criteria=<criteria> \
                      --notification-plan-id=<notification plan id> \
                      [--check-type=<check type>] \
                      [--check-id=<check id>]`
* `lcmon-notifications-create --label \
                      --type=<type> \
                      --details=<details>`
* `lcmon-notification-plans-create --label=<label> \
                      [--critical-state=<critical state notification object ids>] \
                      [--warning-state=<warning state notification object ids>] \
                      [--ok-state=<ok state notification object ids>]`

### Update

* `lcmon-entities-update --id=<entity id> [--label=<label>] \
                        [--ip_address=<ip1=127.0.0.1,ip2=127.0.0.2>] \
                        [--metadata=<foo=bar,bar=foo>]`
* `lcmon-checks-update --entity-id=<entity id> --id=<check id> \
                      [--label=<label>] [--type=<check type>] \
                      [--monitoring-zones=<monitoring zones>] \
                      [--details=<details>] \
                      [--target-alias=<target alias>] \
                      [--target-resolver=<target resolver>] \
                      [--timeout=<timeout>] \
                      [--period=<period>]`
* `lcmon-alarms-update --entity-id=<entity id> \
                      --id=<alarm id>\
                      [--criteria=<criteria>] \
                      [--notification-plan-id=<notification plan id>] \
                      [--check-type=<check type>] \
                      [--check-id=<check id>]`
* `lcmon-notifications-update --id=<notification id> \
                      [--label=<label>] \
                      [--type=<type>] \
                      [--details=<details>]`
* `lcmon-notification-plans-update --id=<notification plan id>
                      [--label=<label>] \
                      [--critical-state=<critical state notification object ids>] \
                      [--warning-state=<warning state notification object ids>] \
                      [--ok-state=<ok state notification object ids>]`

### Delete

* `lcmon-entities-delete --id=<entity id> [--delete-children]`
* `lcmon-checks-delete --entity-id=<parent entity id> --id=<check id>`
* `lcmon-alarms-delete --entity-id=<parent entity id> --id=<alarm id>`
* `lcmon-notifications-delete --id=<notification id>`
* `lcmon-notification-plans-delete --id=<notification plan id>`

### Other

* `lcmon-views-overview`
