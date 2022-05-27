# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsAPITestResultShort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_api_test_result_short_result import (
            SyntheticsAPITestResultShortResult,
        )
        from datadog_api_client.v1.model.synthetics_test_monitor_status import SyntheticsTestMonitorStatus

        return {
            "check_time": (float,),
            "probe_dc": (str,),
            "result": (SyntheticsAPITestResultShortResult,),
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
        Object with the results of a single Synthetic API test.

        :param check_time: Last time the API test was performed.
        :type check_time: float, optional

        :param probe_dc: Location from which the API test was performed.
        :type probe_dc: str, optional

        :param result: Result of the last API test run.
        :type result: SyntheticsAPITestResultShortResult, optional

        :param result_id: ID of the API test result.
        :type result_id: str, optional

        :param status: The status of your Synthetic monitor.


            * ``O`` for not triggered
            * ``1`` for triggered
            * ``2`` for no data
        :type status: SyntheticsTestMonitorStatus, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAPITestResultShort, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
