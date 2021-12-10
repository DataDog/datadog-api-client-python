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
    from datadog_api_client.v1.model.synthetics_browser_test_result_data import SyntheticsBrowserTestResultData
    from datadog_api_client.v1.model.synthetics_browser_test_result_full_check import (
        SyntheticsBrowserTestResultFullCheck,
    )
    from datadog_api_client.v1.model.synthetics_test_monitor_status import SyntheticsTestMonitorStatus

    globals()["SyntheticsBrowserTestResultData"] = SyntheticsBrowserTestResultData
    globals()["SyntheticsBrowserTestResultFullCheck"] = SyntheticsBrowserTestResultFullCheck
    globals()["SyntheticsTestMonitorStatus"] = SyntheticsTestMonitorStatus


class SyntheticsBrowserTestResultFull(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "check": (SyntheticsBrowserTestResultFullCheck,),
            "check_time": (float,),
            "check_version": (int,),
            "probe_dc": (str,),
            "result": (SyntheticsBrowserTestResultData,),
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
        """SyntheticsBrowserTestResultFull - a model defined in OpenAPI

        Keyword Args:
            check (SyntheticsBrowserTestResultFullCheck): [optional]
            check_time (float): [optional] When the browser test was conducted.
            check_version (int): [optional] Version of the browser test used.
            probe_dc (str): [optional] Location from which the browser test was performed.
            result (SyntheticsBrowserTestResultData): [optional]
            result_id (str): [optional] ID of the browser test result.
            status (SyntheticsTestMonitorStatus): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBrowserTestResultFull, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
