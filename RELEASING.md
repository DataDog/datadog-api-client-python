# Releasing
This document summarizes the process of doing a new release of this project.
Release can only be performed by Datadog maintainers of this repository.

## Schedule
This project does not have a strict release schedule. However, we would make a release at least every 2 months.
  - No release will be done if no changes got merged to the `master` branch during the above mentioned window.
  - Releases may be done more frequently than the above mentioned window.

## Make Sure Everything Works
* Make sure tests are passing.
  - Locally and in the continuous integration system.
* Make sure documentation is up-to-date and building correctly.
* Build the package locally (e.g. `python3 setup.py sdist`), install it into a fresh virtualenv and test the changes that have been made since the last release.

## Release Process
Our team will trigger the release pipeline.

### Prerequisite 
- Install [datadog_checks_dev](https://datadog-checks-base.readthedocs.io/en/latest/datadog_checks_dev.cli.html#installation) using Python 3.
- Setup PyPI, see the internal documentation for more details

### Update Changelog
#### Commands
- See changes ready for release by running `ddev release show changes .` at the root of this project. Add any missing labels to PRs if needed.
- Run `ddev release changelog . <NEW_VERSION>` to update the `CHANGELOG.md` file at the root of this repository
- Commit the changes to the repository in a release branch and open a PR. Do not merge yet.

### Release
1. Create the release on GitHub. [Example](https://github.com/DataDog/datadog-api-client-python/releases/tag/1.0.0b1)
1. Checkout the tag created at the previous step.
1. Run `ddev release build .` and `ddev release upload . `.
   - Make sure that both an `sdist` and a [universal wheel](https://packaging.python.org/guides/distributing-packages-using-setuptools/#universal-wheels) have been uploaded to [PyPI](https://pypi.python.org/pypi/datadog/).
