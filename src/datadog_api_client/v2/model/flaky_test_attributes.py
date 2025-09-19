# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.flaky_test_attributes_flaky_state import FlakyTestAttributesFlakyState
    from datadog_api_client.v2.model.flaky_test_pipeline_stats import FlakyTestPipelineStats
    from datadog_api_client.v2.model.flaky_test_run_metadata import FlakyTestRunMetadata
    from datadog_api_client.v2.model.flaky_test_stats import FlakyTestStats


class FlakyTestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.flaky_test_attributes_flaky_state import FlakyTestAttributesFlakyState
        from datadog_api_client.v2.model.flaky_test_pipeline_stats import FlakyTestPipelineStats
        from datadog_api_client.v2.model.flaky_test_run_metadata import FlakyTestRunMetadata
        from datadog_api_client.v2.model.flaky_test_stats import FlakyTestStats

        return {
            "attempt_to_fix_id": (str,),
            "codeowners": ([str],),
            "envs": ([str],),
            "first_flaked_branch": (str,),
            "first_flaked_sha": (str,),
            "first_flaked_ts": (int,),
            "flaky_category": (str, none_type),
            "flaky_state": (FlakyTestAttributesFlakyState,),
            "last_flaked_branch": (str,),
            "last_flaked_sha": (str,),
            "last_flaked_ts": (int,),
            "module": (str, none_type),
            "name": (str,),
            "pipeline_stats": (FlakyTestPipelineStats,),
            "services": ([str],),
            "suite": (str,),
            "test_run_metadata": (FlakyTestRunMetadata,),
            "test_stats": (FlakyTestStats,),
        }

    attribute_map = {
        "attempt_to_fix_id": "attempt_to_fix_id",
        "codeowners": "codeowners",
        "envs": "envs",
        "first_flaked_branch": "first_flaked_branch",
        "first_flaked_sha": "first_flaked_sha",
        "first_flaked_ts": "first_flaked_ts",
        "flaky_category": "flaky_category",
        "flaky_state": "flaky_state",
        "last_flaked_branch": "last_flaked_branch",
        "last_flaked_sha": "last_flaked_sha",
        "last_flaked_ts": "last_flaked_ts",
        "module": "module",
        "name": "name",
        "pipeline_stats": "pipeline_stats",
        "services": "services",
        "suite": "suite",
        "test_run_metadata": "test_run_metadata",
        "test_stats": "test_stats",
    }

    def __init__(
        self_,
        attempt_to_fix_id: Union[str, UnsetType] = unset,
        codeowners: Union[List[str], UnsetType] = unset,
        envs: Union[List[str], UnsetType] = unset,
        first_flaked_branch: Union[str, UnsetType] = unset,
        first_flaked_sha: Union[str, UnsetType] = unset,
        first_flaked_ts: Union[int, UnsetType] = unset,
        flaky_category: Union[str, none_type, UnsetType] = unset,
        flaky_state: Union[FlakyTestAttributesFlakyState, UnsetType] = unset,
        last_flaked_branch: Union[str, UnsetType] = unset,
        last_flaked_sha: Union[str, UnsetType] = unset,
        last_flaked_ts: Union[int, UnsetType] = unset,
        module: Union[str, none_type, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        pipeline_stats: Union[FlakyTestPipelineStats, UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        suite: Union[str, UnsetType] = unset,
        test_run_metadata: Union[FlakyTestRunMetadata, UnsetType] = unset,
        test_stats: Union[FlakyTestStats, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a flaky test.

        :param attempt_to_fix_id: Unique identifier for the attempt to fix this flaky test. Use this ID in the Git commit message in order to trigger the attempt to fix workflow.

            When the workflow is triggered the test is automatically retried by the tracer a certain number of configurable times. When all retries pass, the test is automatically marked as fixed in Flaky Test Management.
            Test runs are tagged with @test.test_management.attempt_to_fix_passed and @test.test_management.is_attempt_to_fix when the attempt to fix workflow is triggered.
        :type attempt_to_fix_id: str, optional

        :param codeowners: The name of the test's code owners as inferred from the repository configuration.
        :type codeowners: [str], optional

        :param envs: List of environments where this test has been flaky.
        :type envs: [str], optional

        :param first_flaked_branch: The branch name where the test exhibited flakiness for the first time.
        :type first_flaked_branch: str, optional

        :param first_flaked_sha: The commit SHA where the test exhibited flakiness for the first time.
        :type first_flaked_sha: str, optional

        :param first_flaked_ts: Unix timestamp when the test exhibited flakiness for the first time.
        :type first_flaked_ts: int, optional

        :param flaky_category: The category of a flaky test.
        :type flaky_category: str, none_type, optional

        :param flaky_state: The current state of the flaky test.
        :type flaky_state: FlakyTestAttributesFlakyState, optional

        :param last_flaked_branch: The branch name where the test exhibited flakiness for the last time.
        :type last_flaked_branch: str, optional

        :param last_flaked_sha: The commit SHA where the test exhibited flakiness for the last time.
        :type last_flaked_sha: str, optional

        :param last_flaked_ts: Unix timestamp when the test exhibited flakiness for the last time.
        :type last_flaked_ts: int, optional

        :param module: The name of the test module. The definition of module changes slightly per language:

            * In .NET, a test module groups every test that is run under the same unit test project.
            * In Swift, a test module groups every test that is run for a given bundle.
            * In JavaScript, the test modules map one-to-one to test sessions.
            * In Java, a test module groups every test that is run by the same Maven Surefire/Failsafe or Gradle Test task execution.
            * In Python, a test module groups every test that is run under the same ``.py`` file as part of a test suite, which is typically managed by a framework like ``unittest`` or ``pytest``.
            * In Ruby, a test module groups every test that is run within the same test file, which is typically managed by a framework like ``RSpec`` or ``Minitest``.
        :type module: str, none_type, optional

        :param name: The test name. A concise name for a test case. Defined in the test itself.
        :type name: str, optional

        :param pipeline_stats: CI pipeline related statistics for the flaky test. This information is only available if test runs are associated with CI pipeline events from CI Visibility.
        :type pipeline_stats: FlakyTestPipelineStats, optional

        :param services: List of test service names where this test has been flaky.

            A test service is a group of tests associated with a project or repository. It contains all the individual tests for your code, optionally organized into test suites, which are like folders for your tests.
        :type services: [str], optional

        :param suite: The name of the test suite. A group of tests exercising the same unit of code depending on your language and testing framework.
        :type suite: str, optional

        :param test_run_metadata: Metadata about the latest failed test run of the flaky test.
        :type test_run_metadata: FlakyTestRunMetadata, optional

        :param test_stats: Test statistics for the flaky test.
        :type test_stats: FlakyTestStats, optional
        """
        if attempt_to_fix_id is not unset:
            kwargs["attempt_to_fix_id"] = attempt_to_fix_id
        if codeowners is not unset:
            kwargs["codeowners"] = codeowners
        if envs is not unset:
            kwargs["envs"] = envs
        if first_flaked_branch is not unset:
            kwargs["first_flaked_branch"] = first_flaked_branch
        if first_flaked_sha is not unset:
            kwargs["first_flaked_sha"] = first_flaked_sha
        if first_flaked_ts is not unset:
            kwargs["first_flaked_ts"] = first_flaked_ts
        if flaky_category is not unset:
            kwargs["flaky_category"] = flaky_category
        if flaky_state is not unset:
            kwargs["flaky_state"] = flaky_state
        if last_flaked_branch is not unset:
            kwargs["last_flaked_branch"] = last_flaked_branch
        if last_flaked_sha is not unset:
            kwargs["last_flaked_sha"] = last_flaked_sha
        if last_flaked_ts is not unset:
            kwargs["last_flaked_ts"] = last_flaked_ts
        if module is not unset:
            kwargs["module"] = module
        if name is not unset:
            kwargs["name"] = name
        if pipeline_stats is not unset:
            kwargs["pipeline_stats"] = pipeline_stats
        if services is not unset:
            kwargs["services"] = services
        if suite is not unset:
            kwargs["suite"] = suite
        if test_run_metadata is not unset:
            kwargs["test_run_metadata"] = test_run_metadata
        if test_stats is not unset:
            kwargs["test_stats"] = test_stats
        super().__init__(kwargs)
