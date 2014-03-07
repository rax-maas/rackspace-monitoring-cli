rackspace-monitoring-cli v0.6.1 - 2014-03-07:

* Add a hack to setup.py to enable backwards compat with old versions of
  pip.

rackspace-monitoring-cli v0.6.1 - 2014-03-06:

* Add requirements.txt to MANIFEST

rackspace-monitoring-cli v0.6.0 - 2014-03-06:

* Add support for suppressions

rackspace-monitoring-cli v0.5.2 - 2013-06-19:

* Fix typo in raxmon-entities-create command

rackspace-monitoring-cli v0.5.1 - 2013-06-17:

* Add raxmon-agent-installer

rackspace-monitoring-cli v0.5.0 - 2013-06-06:

* Depend on rackspace-monitoring v0.5

rackspace-monitoring-cli v0.4.6 - 2013-10-01:

* Include new updated CA certificate file
* Remove monitoring_zones and label from required options for the checks-create
  command

rackspace-monitoring-cli v0.4.4 - 2012-07-23:

* Add new agent related commands.
* Remove `delete-children` option from the `raxmon-entities-delete commands`

rackspace-monitoring-cli v0.4.3 - 2012-06-29:

* Fix a typo in raxmon-agent-tokens-delete

rackspace-monitoring-cli v0.4.2 - 2012-06-12:

* Add new `raxmon-monitoring-zones-traceroute` command

rackspace-monitoring-cli v0.4.1 - 2012-06-06:

* Add new [ssl] section with the verify option to the config.
  [Brandon Philips]
* Add new hidden agent-id field to the entities command.
  [Brandon Philips]

rackspace-monitoring-cli v0.4.0 - 2012-05-24:

* Add new `raxmon-checks-test-existing` command.
* Add new `raxmon-alarms-notification-history-list` command.
* Add new `raxmon-alarms-notification-history-list-checks` command.
* Allow user to specify path to the `.raxrc` file using `RAXMON_RAXRC`
  environment variable.
* Print help if user doesn't pass enough arguments to the command.
  [Ryan Phillips]

rackspace-monitoring-cli v0.3.1 - 2012-03-29:

* Add missing `--label` option to raxmon-alarms-create command
* Add new commands for testing notifications:
  * `raxmon-notifications-test`
  * `raxmon-notifications-test-existing`

rackspace-monitoring-cli v0.3.0 - 2012-03-27:

* Update the API URL to be https://monitoring.api.rackspacecloud.com
* Allow user to pass `--no-ssl-verify` option to all the commands.
  When this option is used, SSL certificates aren't verified.
* Allow user to specify a custom auth url using `--auth-url` option

rackspace-monitoring-cli v0.2.5 - 2012-02-24:

* Add a `raxmon` command which lists all the available commands
* Add `raxmon-notification-types-list` command

rackspace-monitoring-cli v0.2.4 - 2012-01-11:

* Bundle CA certificates file with the distribution.

rackspace-monitoring-cli v0.2.3 - 2012-01-03:

* Add `RAXMON_` prefix to the environment variables so they don't conflict with
 rackspace-monitoring-cli v0.2.3 - 2012-01-03:

* Add `RAXMON_` prefix to the environment variables so they don't conflict with
  other environment variables.
  [Pedro Padron]

* Add `raxmon-checks-disable` and `raxmon-checks-enable` command.

rackspace-monitoring-cli v0.2.2 - 2011-12-25:

* Add `--json` option to the `raxmon-checks-test` command. This way response
  can be directly piped to a file and used with `raxmon-alarms-test` command.
* Add `raxmon-alarms-test` command
* Change `rackspace-monitoring` dependency version to 0.2.1

rackspace-monitoring-cli v0.2.1 - 2011-12-22:

* Add missing `target-hostname` option to the checks create, update and test
  command.
* Add `raxmon-checks-test` command
* Add global `--why` and `--who` option to all the create, update and delete
  commands. If `--who` is not provided it defaults to the current user username.

rackspace-monitoring-cli v0.2.0 - 2011-12-19:

 * Add support for commands option bash auto-completion.
 * Allow user to provide credentials using environment variables
   (`USERNAME`, `API_KEY`, `API_URL`)
 * Allow user to pass `--marker` option to the list commands

rackspace-monitoring-cli v0.1.0 - 2011-12-14:

 * Initial release.
