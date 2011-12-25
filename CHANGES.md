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
