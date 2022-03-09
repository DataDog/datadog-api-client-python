# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_browser_test_result_short_result import (
        SyntheticsBrowserTestResultShortResult,
    )
    from datadog_api_client.v1.model.synthetics_test_monitor_status import SyntheticsTestMonitorStatus

    globals()["SyntheticsBrowserTestResultShortResult"] = SyntheticsBrowserTestResultShortResult
    globals()["SyntheticsTestMonitorStatus"] = SyntheticsTestMonitorStatus


class SyntheticsBrowserTestResultShort(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "check_time": (float,),
            "probe_dc": (str,),
            "result": (SyntheticsBrowserTestResultShortResult,),
            "result_id": (str,),
            "status": (SyntheticsTestMonitorStatus,),
        }

    attribute_map = {
        "check_time": "check_time",
        "probe_dc": "probe_dc",
        "result": "result",
        "result_id": "result_id",
        "status": "status",
    }

    def __init__(self, *args, **kwargs):
        """
        Object with the results of a single Synthetic browser test.

        :param check_time: Last time the browser test was performed.
        :type check_time: float, optional

        :param probe_dc: Location from which the Browser test was performed.
        :type probe_dc: str, optional

        :param result: Object with the result of the last browser test run.
        :type result: SyntheticsBrowserTestResultShortResult, optional

        :param result_id: ID of the browser test result.
        :type result_id: str, optional

        :param status: The status of your Synthetic monitor.
            * `O` for not triggered
            * `1` for triggered
            * `2` for no data
        :type status: SyntheticsTestMonitorStatus, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBrowserTestResultShort, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
