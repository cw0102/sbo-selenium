sbo-selenium Changelog
======================

0.7.3 (2019-02-14)
------------------
* Remove pip as a requirement. (RAMP-146)

0.7.2 (2016-05-05)
------------------
* Clarify and demonstrate how to successfully run tests via a Docker-based
  Selenium server in a virtual machine while using tox.

0.7.1 (2016-04-22)
------------------
* Fixed support for specifying which tests to run on the command line.  This
  seems to have been broken for Django versions which use argparse to parse
  management command options since support was added for them.

0.7.0 (2016-04-21)
------------------
* Added the ``--command-executor`` option for specifying which Selenium server
  to use, if not localhost
* Added the ``--docker`` option to automatically start and stop a Docker
  container for a standalone Selenium server to be used, and added a few
  related Django settings
* Fixed handling of custom parameters to work with recent versions of
  django-nose
* Changed monitoring of the Selenium server auto-launching to watch stderr
  instead of stdout for the startup complete message, as recent versions of
  Selenium seem to have moved the startup output there
* Fixed a bug where the code for timing out attempts to start certain services
  (like a standalone Selenium server or Sauce Connect) was taking far longer
  than intended to time out

0.6.0 (2016-03-29)
------------------
* Removed the ``-p`` alias for ``--platform``, as it now conflicts with
  the ``--plugins`` parameter in the base Django test command
* Fixed support for the underlying test command's standard options under
  Django 1.8 and above
* Confirmed compatibility with Django 1.9 and current master
* Fixed a minor incompatibility in ``audit_accessibility()`` with
  accessibility developer tools 2.10.1

0.5.1 (2016-03-03)
------------------
* Support accessibility developer tools 2.10.1

0.5.0 (2015-06-29)
------------------
* Support Django 1.7 and 1.8
* Support Python 3 when using Django 1.6 and above
* Removed dependency on nose and django-nose, now also works with the default
  Django test runner
* Fixed SELENIUM_DEFAULT_BROWSER behavior (was always defaulting to chrome)
* Added the SELENIUM_TEST_COMMAND_OPTIONS setting

0.4.4 (2015-01-30)
------------------
* Add a hook to allow sub classes to specify a firefox profile (from emperorcezar)
* Fixed compatibility with pip 6.x

0.4.3 (2014-06-01)
------------------
* More robust SeleniumTestCase.click() implementation (retry until success or timeout)

0.4.2 (2014-05-20)
------------------
* Page load timeout support (default is 10 seconds, override via SELENIUM_PAGE_LOAD_TIMEOUT)
* Support for Internet Explorer Sauce OnDemand sessions (from qpfiffer)

0.4.1 (2014-04-18)
------------------
* Added support for Sauce Connect tunnel identifiers
* Added the SELENIUM_SAUCE_VERSION setting to tell Sauce Labs which Selenium
  version to use
* More reliable output of Sauce OnDemand session IDs for integration with
  the Jenkins plugin
* Better redirection of error messages to configured logging (the
  SELENIUM_LOG_FILE setting is no longer needed and has been removed)

0.4.0 (2014-03-29)
------------------
* Initial public release
