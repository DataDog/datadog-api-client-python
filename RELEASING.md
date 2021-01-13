# Releasing
This document summarizes the process of doing a new release of this project.
Release can only be performed by Datadog maintainers of this repository.

## Schedule
This project does not have a strict release schedule. However, we would make a release at least every 2 months.
  - No release will be done if no changes got merged to the `master` branch during the above mentioned window.
  - Releases may be done more frequently than the above mentioned window.

## Release Process
Our team will trigger the release pipeline.

### Prerequisite 
- Install [datadog_checks_dev](https://datadog-checks-base.readthedocs.io/en/latest/datadog_checks_dev.cli.html#installation) using Python 3.

### Update Changelog
#### Commands
- See changes ready for release by running `ddev release show changes . --tag-prefix v --since <CURRENT_VERSION>` at the root of this project. Add any missing labels to PRs if needed.
- Run `ddev release changelog . <NEW_VERSION> <CURRENT_VERSION> --no-semver` to update the `CHANGELOG.md` file at the root of this repository
- Commit the changes to the repository in a release branch and open a PR.
    - Ensure CI passes fully here, this is the commit that will be released!
    - Ensure the [documentation builds](https://readthedocs.org/projects/datadog-api-client/builds/) are passing
    - Get this PR approved and merged

### Release
1. Create the release on GitHub. [Example](https://github.com/DataDog/datadog-api-client-python/releases/tag/1.0.0b1)
1. A github action will kick off that builds and publishes this tag to PyPI. Confirm the [release is available](https://pypi.org/project/datadog-api-client/#history)