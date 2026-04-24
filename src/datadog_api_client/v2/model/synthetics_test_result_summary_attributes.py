# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_device import SyntheticsTestResultDevice
    from datadog_api_client.v2.model.synthetics_test_result_execution_info import SyntheticsTestResultExecutionInfo
    from datadog_api_client.v2.model.synthetics_test_result_location import SyntheticsTestResultLocation
    from datadog_api_client.v2.model.synthetics_test_result_run_type import SyntheticsTestResultRunType
    from datadog_api_client.v2.model.synthetics_test_result_status import SyntheticsTestResultStatus
    from datadog_api_client.v2.model.synthetics_test_result_steps_info import SyntheticsTestResultStepsInfo
    from datadog_api_client.v2.model.synthetics_test_sub_type import SyntheticsTestSubType
    from datadog_api_client.v2.model.synthetics_test_type import SyntheticsTestType


class SyntheticsTestResultSummaryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_device import SyntheticsTestResultDevice
        from datadog_api_client.v2.model.synthetics_test_result_execution_info import SyntheticsTestResultExecutionInfo
        from datadog_api_client.v2.model.synthetics_test_result_location import SyntheticsTestResultLocation
        from datadog_api_client.v2.model.synthetics_test_result_run_type import SyntheticsTestResultRunType
        from datadog_api_client.v2.model.synthetics_test_result_status import SyntheticsTestResultStatus
        from datadog_api_client.v2.model.synthetics_test_result_steps_info import SyntheticsTestResultStepsInfo
        from datadog_api_client.v2.model.synthetics_test_sub_type import SyntheticsTestSubType
        from datadog_api_client.v2.model.synthetics_test_type import SyntheticsTestType

        return {
            "device": (SyntheticsTestResultDevice,),
            "execution_info": (SyntheticsTestResultExecutionInfo,),
            "finished_at": (int,),
            "location": (SyntheticsTestResultLocation,),
            "run_type": (SyntheticsTestResultRunType,),
            "started_at": (int,),
            "status": (SyntheticsTestResultStatus,),
            "steps_info": (SyntheticsTestResultStepsInfo,),
            "test_sub_type": (SyntheticsTestSubType,),
            "test_type": (SyntheticsTestType,),
        }

    attribute_map = {
        "device": "device",
        "execution_info": "execution_info",
        "finished_at": "finished_at",
        "location": "location",
        "run_type": "run_type",
        "started_at": "started_at",
        "status": "status",
        "steps_info": "steps_info",
        "test_sub_type": "test_sub_type",
        "test_type": "test_type",
    }

    def __init__(
        self_,
        device: Union[SyntheticsTestResultDevice, UnsetType] = unset,
        execution_info: Union[SyntheticsTestResultExecutionInfo, UnsetType] = unset,
        finished_at: Union[int, UnsetType] = unset,
        location: Union[SyntheticsTestResultLocation, UnsetType] = unset,
        run_type: Union[SyntheticsTestResultRunType, UnsetType] = unset,
        started_at: Union[int, UnsetType] = unset,
        status: Union[SyntheticsTestResultStatus, UnsetType] = unset,
        steps_info: Union[SyntheticsTestResultStepsInfo, UnsetType] = unset,
        test_sub_type: Union[SyntheticsTestSubType, UnsetType] = unset,
        test_type: Union[SyntheticsTestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Synthetic test result summary.

        :param device: Device information for the test result (browser and mobile tests).
        :type device: SyntheticsTestResultDevice, optional

        :param execution_info: Execution details for a Synthetic test result.
        :type execution_info: SyntheticsTestResultExecutionInfo, optional

        :param finished_at: Timestamp of when the test finished (in milliseconds).
        :type finished_at: int, optional

        :param location: Location information for a Synthetic test result.
        :type location: SyntheticsTestResultLocation, optional

        :param run_type: The type of run for a Synthetic test result.
        :type run_type: SyntheticsTestResultRunType, optional

        :param started_at: Timestamp of when the test started (in milliseconds).
        :type started_at: int, optional

        :param status: Status of a Synthetic test result.
        :type status: SyntheticsTestResultStatus, optional

        :param steps_info: Step execution summary for a Synthetic test result.
        :type steps_info: SyntheticsTestResultStepsInfo, optional

        :param test_sub_type: Subtype of the Synthetic test that produced this result.
        :type test_sub_type: SyntheticsTestSubType, optional

        :param test_type: Type of the Synthetic test that produced this result.
        :type test_type: SyntheticsTestType, optional
        """
        if device is not unset:
            kwargs["device"] = device
        if execution_info is not unset:
            kwargs["execution_info"] = execution_info
        if finished_at is not unset:
            kwargs["finished_at"] = finished_at
        if location is not unset:
            kwargs["location"] = location
        if run_type is not unset:
            kwargs["run_type"] = run_type
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if status is not unset:
            kwargs["status"] = status
        if steps_info is not unset:
            kwargs["steps_info"] = steps_info
        if test_sub_type is not unset:
            kwargs["test_sub_type"] = test_sub_type
        if test_type is not unset:
            kwargs["test_type"] = test_type
        super().__init__(kwargs)
