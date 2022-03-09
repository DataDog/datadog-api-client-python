# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_api_test_result_full_check import SyntheticsAPITestResultFullCheck
    from datadog_api_client.v1.model.synthetics_api_test_result_data import SyntheticsAPITestResultData
    from datadog_api_client.v1.model.synthetics_test_monitor_status import SyntheticsTestMonitorStatus

    globals()["SyntheticsAPITestResultFullCheck"] = SyntheticsAPITestResultFullCheck
    globals()["SyntheticsAPITestResultData"] = SyntheticsAPITestResultData
    globals()["SyntheticsTestMonitorStatus"] = SyntheticsTestMonitorStatus


class SyntheticsAPITestResultFull(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "check": (SyntheticsAPITestResultFullCheck,),
            "check_time": (float,),
            "check_version": (int,),
            "probe_dc": (str,),
            "result": (SyntheticsAPITestResultData,),
            "result_id": (str,),
            "status": (SyntheticsTestMonitorStatus,),
        }

    attribute_map = {
        "check": "check",
        "check_time": "check_time",
        "check_version": "check_version",
        "probe_dc": "probe_dc",
        "result": "result",
        "result_id": "result_id",
        "status": "status",
    }

    def __init__(self, *args, **kwargs):
        """
        Object returned describing a API test result.

        :param check: Object describing the API test configuration.
        :type check: SyntheticsAPITestResultFullCheck, optional

        :param check_time: When the API test was conducted.
        :type check_time: float, optional

        :param check_version: Version of the API test used.
        :type check_version: int, optional

        :param probe_dc: Locations for which to query the API test results.
        :type probe_dc: str, optional

        :param result: Object containing results for your Synthetic API test.
        :type result: SyntheticsAPITestResultData, optional

        :param result_id: ID of the API test result.
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

        self = super(SyntheticsAPITestResultFull, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
