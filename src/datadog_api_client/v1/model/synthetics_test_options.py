# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID
    from datadog_api_client.v1.model.synthetics_test_options_monitor_options import SyntheticsTestOptionsMonitorOptions
    from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry

    globals()["SyntheticsDeviceID"] = SyntheticsDeviceID
    globals()["SyntheticsTestOptionsMonitorOptions"] = SyntheticsTestOptionsMonitorOptions
    globals()["SyntheticsTestOptionsRetry"] = SyntheticsTestOptionsRetry


class SyntheticsTestOptions(ModelNormal):

    validations = {
        "monitor_priority": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 1,
        },
        "tick_every": {
            "inclusive_maximum": 604800,
            "inclusive_minimum": 30,
        },
    }

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "accept_self_signed": (bool,),
            "allow_insecure": (bool,),
            "check_certificate_revocation": (bool,),
            "device_ids": ([SyntheticsDeviceID],),
            "disable_cors": (bool,),
            "follow_redirects": (bool,),
            "min_failure_duration": (int,),
            "min_location_failed": (int,),
            "monitor_name": (str,),
            "monitor_options": (SyntheticsTestOptionsMonitorOptions,),
            "monitor_priority": (int,),
            "no_screenshot": (bool,),
            "retry": (SyntheticsTestOptionsRetry,),
            "tick_every": (int,),
        }

    attribute_map = {
        "accept_self_signed": "accept_self_signed",
        "allow_insecure": "allow_insecure",
        "check_certificate_revocation": "checkCertificateRevocation",
        "device_ids": "device_ids",
        "disable_cors": "disableCors",
        "follow_redirects": "follow_redirects",
        "min_failure_duration": "min_failure_duration",
        "min_location_failed": "min_location_failed",
        "monitor_name": "monitor_name",
        "monitor_options": "monitor_options",
        "monitor_priority": "monitor_priority",
        "no_screenshot": "noScreenshot",
        "retry": "retry",
        "tick_every": "tick_every",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Object describing the extra options for a Synthetic test.

        :param accept_self_signed: For SSL test, whether or not the test should allow self signed
            certificates.
        :type accept_self_signed: bool, optional

        :param allow_insecure: Allows loading insecure content for an HTTP request.
        :type allow_insecure: bool, optional

        :param check_certificate_revocation: For SSL test, whether or not the test should fail on revoked certificate in stapled OCSP.
        :type check_certificate_revocation: bool, optional

        :param device_ids: For browser test, array with the different device IDs used to run the test.
        :type device_ids: [SyntheticsDeviceID], optional

        :param disable_cors: Whether or not to disable CORS mechanism.
        :type disable_cors: bool, optional

        :param follow_redirects: For API HTTP test, whether or not the test should follow redirects.
        :type follow_redirects: bool, optional

        :param min_failure_duration: Minimum amount of time in failure required to trigger an alert.
        :type min_failure_duration: int, optional

        :param min_location_failed: Minimum number of locations in failure required to trigger
            an alert.
        :type min_location_failed: int, optional

        :param monitor_name: The monitor name is used for the alert title as well as for all monitor dashboard widgets and SLOs.
        :type monitor_name: str, optional

        :param monitor_options: Object containing the options for a Synthetic test as a monitor
            (for example, renotification).
        :type monitor_options: SyntheticsTestOptionsMonitorOptions, optional

        :param monitor_priority: Integer from 1 (high) to 5 (low) indicating alert severity.
        :type monitor_priority: int, optional

        :param no_screenshot: Prevents saving screenshots of the steps.
        :type no_screenshot: bool, optional

        :param retry: Object describing the retry strategy to apply to a Synthetic test.
        :type retry: SyntheticsTestOptionsRetry, optional

        :param tick_every: The frequency at which to run the Synthetic test (in seconds).
        :type tick_every: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTestOptions, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
