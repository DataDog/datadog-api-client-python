# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_test_restriction_policy_binding import (
        SyntheticsTestRestrictionPolicyBinding,
    )
    from datadog_api_client.v1.model.synthetics_test_ci_options import SyntheticsTestCiOptions
    from datadog_api_client.v1.model.synthetics_mobile_tests_mobile_application import (
        SyntheticsMobileTestsMobileApplication,
    )
    from datadog_api_client.v1.model.synthetics_test_options_monitor_options import SyntheticsTestOptionsMonitorOptions
    from datadog_api_client.v1.model.synthetics_restricted_roles import SyntheticsRestrictedRoles
    from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
    from datadog_api_client.v1.model.synthetics_test_options_scheduling import SyntheticsTestOptionsScheduling


class SyntheticsMobileTestOptions(ModelNormal):
    validations = {
        "default_step_timeout": {
            "inclusive_maximum": 300,
            "inclusive_minimum": 1,
        },
        "min_failure_duration": {
            "inclusive_maximum": 7200,
            "inclusive_minimum": 0,
        },
        "monitor_priority": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 1,
        },
        "tick_every": {
            "inclusive_maximum": 604800,
            "inclusive_minimum": 300,
        },
        "verbosity": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_test_restriction_policy_binding import (
            SyntheticsTestRestrictionPolicyBinding,
        )
        from datadog_api_client.v1.model.synthetics_test_ci_options import SyntheticsTestCiOptions
        from datadog_api_client.v1.model.synthetics_mobile_tests_mobile_application import (
            SyntheticsMobileTestsMobileApplication,
        )
        from datadog_api_client.v1.model.synthetics_test_options_monitor_options import (
            SyntheticsTestOptionsMonitorOptions,
        )
        from datadog_api_client.v1.model.synthetics_restricted_roles import SyntheticsRestrictedRoles
        from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
        from datadog_api_client.v1.model.synthetics_test_options_scheduling import SyntheticsTestOptionsScheduling

        return {
            "allow_application_crash": (bool,),
            "bindings": ([SyntheticsTestRestrictionPolicyBinding],),
            "ci": (SyntheticsTestCiOptions,),
            "default_step_timeout": (int,),
            "device_ids": ([str],),
            "disable_auto_accept_alert": (bool,),
            "min_failure_duration": (int,),
            "mobile_application": (SyntheticsMobileTestsMobileApplication,),
            "monitor_name": (str,),
            "monitor_options": (SyntheticsTestOptionsMonitorOptions,),
            "monitor_priority": (int,),
            "no_screenshot": (bool,),
            "restricted_roles": (SyntheticsRestrictedRoles,),
            "retry": (SyntheticsTestOptionsRetry,),
            "scheduling": (SyntheticsTestOptionsScheduling,),
            "tick_every": (int,),
            "verbosity": (int,),
        }

    attribute_map = {
        "allow_application_crash": "allowApplicationCrash",
        "bindings": "bindings",
        "ci": "ci",
        "default_step_timeout": "defaultStepTimeout",
        "device_ids": "device_ids",
        "disable_auto_accept_alert": "disableAutoAcceptAlert",
        "min_failure_duration": "min_failure_duration",
        "mobile_application": "mobileApplication",
        "monitor_name": "monitor_name",
        "monitor_options": "monitor_options",
        "monitor_priority": "monitor_priority",
        "no_screenshot": "noScreenshot",
        "restricted_roles": "restricted_roles",
        "retry": "retry",
        "scheduling": "scheduling",
        "tick_every": "tick_every",
        "verbosity": "verbosity",
    }

    def __init__(
        self_,
        device_ids: List[str],
        mobile_application: SyntheticsMobileTestsMobileApplication,
        tick_every: int,
        allow_application_crash: Union[bool, UnsetType] = unset,
        bindings: Union[List[SyntheticsTestRestrictionPolicyBinding], UnsetType] = unset,
        ci: Union[SyntheticsTestCiOptions, UnsetType] = unset,
        default_step_timeout: Union[int, UnsetType] = unset,
        disable_auto_accept_alert: Union[bool, UnsetType] = unset,
        min_failure_duration: Union[int, UnsetType] = unset,
        monitor_name: Union[str, UnsetType] = unset,
        monitor_options: Union[SyntheticsTestOptionsMonitorOptions, UnsetType] = unset,
        monitor_priority: Union[int, UnsetType] = unset,
        no_screenshot: Union[bool, UnsetType] = unset,
        restricted_roles: Union[SyntheticsRestrictedRoles, UnsetType] = unset,
        retry: Union[SyntheticsTestOptionsRetry, UnsetType] = unset,
        scheduling: Union[SyntheticsTestOptionsScheduling, UnsetType] = unset,
        verbosity: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing the extra options for a Synthetic test.

        :param allow_application_crash: A boolean to set if an application crash would mark the test as failed.
        :type allow_application_crash: bool, optional

        :param bindings: Array of bindings used for the mobile test.
        :type bindings: [SyntheticsTestRestrictionPolicyBinding], optional

        :param ci: CI/CD options for a Synthetic test.
        :type ci: SyntheticsTestCiOptions, optional

        :param default_step_timeout: The default timeout for steps in the test (in seconds).
        :type default_step_timeout: int, optional

        :param device_ids: For mobile test, array with the different device IDs used to run the test.
        :type device_ids: [str]

        :param disable_auto_accept_alert: A boolean to disable auto accepting alerts.
        :type disable_auto_accept_alert: bool, optional

        :param min_failure_duration: Minimum amount of time in failure required to trigger an alert.
        :type min_failure_duration: int, optional

        :param mobile_application: Mobile application for mobile synthetics test.
        :type mobile_application: SyntheticsMobileTestsMobileApplication

        :param monitor_name: The monitor name is used for the alert title as well as for all monitor dashboard widgets and SLOs.
        :type monitor_name: str, optional

        :param monitor_options: Object containing the options for a Synthetic test as a monitor
            (for example, renotification).
        :type monitor_options: SyntheticsTestOptionsMonitorOptions, optional

        :param monitor_priority: Integer from 1 (high) to 5 (low) indicating alert severity.
        :type monitor_priority: int, optional

        :param no_screenshot: A boolean set to not take a screenshot for the step.
        :type no_screenshot: bool, optional

        :param restricted_roles: A list of role identifiers that can be pulled from the Roles API, for restricting read and write access.
        :type restricted_roles: SyntheticsRestrictedRoles, optional

        :param retry: Object describing the retry strategy to apply to a Synthetic test.
        :type retry: SyntheticsTestOptionsRetry, optional

        :param scheduling: Object containing timeframes and timezone used for advanced scheduling.
        :type scheduling: SyntheticsTestOptionsScheduling, optional

        :param tick_every: The frequency at which to run the Synthetic test (in seconds).
        :type tick_every: int

        :param verbosity: The level of verbosity for the mobile test. This field can not be set by a user.
        :type verbosity: int, optional
        """
        if allow_application_crash is not unset:
            kwargs["allow_application_crash"] = allow_application_crash
        if bindings is not unset:
            kwargs["bindings"] = bindings
        if ci is not unset:
            kwargs["ci"] = ci
        if default_step_timeout is not unset:
            kwargs["default_step_timeout"] = default_step_timeout
        if disable_auto_accept_alert is not unset:
            kwargs["disable_auto_accept_alert"] = disable_auto_accept_alert
        if min_failure_duration is not unset:
            kwargs["min_failure_duration"] = min_failure_duration
        if monitor_name is not unset:
            kwargs["monitor_name"] = monitor_name
        if monitor_options is not unset:
            kwargs["monitor_options"] = monitor_options
        if monitor_priority is not unset:
            kwargs["monitor_priority"] = monitor_priority
        if no_screenshot is not unset:
            kwargs["no_screenshot"] = no_screenshot
        if restricted_roles is not unset:
            kwargs["restricted_roles"] = restricted_roles
        if retry is not unset:
            kwargs["retry"] = retry
        if scheduling is not unset:
            kwargs["scheduling"] = scheduling
        if verbosity is not unset:
            kwargs["verbosity"] = verbosity
        super().__init__(kwargs)

        self_.device_ids = device_ids
        self_.mobile_application = mobile_application
        self_.tick_every = tick_every
