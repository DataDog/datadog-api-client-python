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
    from datadog_api_client.v2.model.synthetics_test_result_batch import SyntheticsTestResultBatch
    from datadog_api_client.v2.model.synthetics_test_result_ci import SyntheticsTestResultCI
    from datadog_api_client.v2.model.synthetics_test_result_device import SyntheticsTestResultDevice
    from datadog_api_client.v2.model.synthetics_test_result_git import SyntheticsTestResultGit
    from datadog_api_client.v2.model.synthetics_test_result_location import SyntheticsTestResultLocation
    from datadog_api_client.v2.model.synthetics_test_result_detail import SyntheticsTestResultDetail
    from datadog_api_client.v2.model.synthetics_test_sub_type import SyntheticsTestSubType
    from datadog_api_client.v2.model.synthetics_test_type import SyntheticsTestType


class SyntheticsTestResultAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_batch import SyntheticsTestResultBatch
        from datadog_api_client.v2.model.synthetics_test_result_ci import SyntheticsTestResultCI
        from datadog_api_client.v2.model.synthetics_test_result_device import SyntheticsTestResultDevice
        from datadog_api_client.v2.model.synthetics_test_result_git import SyntheticsTestResultGit
        from datadog_api_client.v2.model.synthetics_test_result_location import SyntheticsTestResultLocation
        from datadog_api_client.v2.model.synthetics_test_result_detail import SyntheticsTestResultDetail
        from datadog_api_client.v2.model.synthetics_test_sub_type import SyntheticsTestSubType
        from datadog_api_client.v2.model.synthetics_test_type import SyntheticsTestType

        return {
            "batch": (SyntheticsTestResultBatch,),
            "ci": (SyntheticsTestResultCI,),
            "device": (SyntheticsTestResultDevice,),
            "git": (SyntheticsTestResultGit,),
            "location": (SyntheticsTestResultLocation,),
            "result": (SyntheticsTestResultDetail,),
            "test_sub_type": (SyntheticsTestSubType,),
            "test_type": (SyntheticsTestType,),
        }

    attribute_map = {
        "batch": "batch",
        "ci": "ci",
        "device": "device",
        "git": "git",
        "location": "location",
        "result": "result",
        "test_sub_type": "test_sub_type",
        "test_type": "test_type",
    }

    def __init__(
        self_,
        batch: Union[SyntheticsTestResultBatch, UnsetType] = unset,
        ci: Union[SyntheticsTestResultCI, UnsetType] = unset,
        device: Union[SyntheticsTestResultDevice, UnsetType] = unset,
        git: Union[SyntheticsTestResultGit, UnsetType] = unset,
        location: Union[SyntheticsTestResultLocation, UnsetType] = unset,
        result: Union[SyntheticsTestResultDetail, UnsetType] = unset,
        test_sub_type: Union[SyntheticsTestSubType, UnsetType] = unset,
        test_type: Union[SyntheticsTestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Synthetic test result.

        :param batch: Batch information for the test result.
        :type batch: SyntheticsTestResultBatch, optional

        :param ci: CI information associated with the test result.
        :type ci: SyntheticsTestResultCI, optional

        :param device: Device information for the test result (browser and mobile tests).
        :type device: SyntheticsTestResultDevice, optional

        :param git: Git information associated with the test result.
        :type git: SyntheticsTestResultGit, optional

        :param location: Location information for a Synthetic test result.
        :type location: SyntheticsTestResultLocation, optional

        :param result: Full result details for a Synthetic test execution.
        :type result: SyntheticsTestResultDetail, optional

        :param test_sub_type: Subtype of the Synthetic test that produced this result.
        :type test_sub_type: SyntheticsTestSubType, optional

        :param test_type: Type of the Synthetic test that produced this result.
        :type test_type: SyntheticsTestType, optional
        """
        if batch is not unset:
            kwargs["batch"] = batch
        if ci is not unset:
            kwargs["ci"] = ci
        if device is not unset:
            kwargs["device"] = device
        if git is not unset:
            kwargs["git"] = git
        if location is not unset:
            kwargs["location"] = location
        if result is not unset:
            kwargs["result"] = result
        if test_sub_type is not unset:
            kwargs["test_sub_type"] = test_sub_type
        if test_type is not unset:
            kwargs["test_type"] = test_type
        super().__init__(kwargs)
