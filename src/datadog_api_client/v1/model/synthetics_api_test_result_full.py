# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_api_test_result_data import SyntheticsAPITestResultData
    from datadog_api_client.v1.model.synthetics_api_test_result_full_check import SyntheticsAPITestResultFullCheck
    from datadog_api_client.v1.model.synthetics_test_monitor_status import SyntheticsTestMonitorStatus

    globals()["SyntheticsAPITestResultData"] = SyntheticsAPITestResultData
    globals()["SyntheticsAPITestResultFullCheck"] = SyntheticsAPITestResultFullCheck
    globals()["SyntheticsTestMonitorStatus"] = SyntheticsTestMonitorStatus


class SyntheticsAPITestResultFull(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
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

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SyntheticsAPITestResultFull - a model defined in OpenAPI

        Keyword Args:
            check (SyntheticsAPITestResultFullCheck): [optional]
            check_time (float): [optional] When the API test was conducted.
            check_version (int): [optional] Version of the API test used.
            probe_dc (str): [optional] Locations for which to query the API test results.
            result (SyntheticsAPITestResultData): [optional]
            result_id (str): [optional] ID of the API test result.
            status (SyntheticsTestMonitorStatus): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAPITestResultFull, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
