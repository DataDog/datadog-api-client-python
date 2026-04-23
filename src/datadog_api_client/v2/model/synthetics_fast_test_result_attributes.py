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
    from datadog_api_client.v2.model.synthetics_test_result_location import SyntheticsTestResultLocation
    from datadog_api_client.v2.model.synthetics_fast_test_result_detail import SyntheticsFastTestResultDetail
    from datadog_api_client.v2.model.synthetics_fast_test_sub_type import SyntheticsFastTestSubType
    from datadog_api_client.v2.model.synthetics_fast_test_type import SyntheticsFastTestType


class SyntheticsFastTestResultAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_device import SyntheticsTestResultDevice
        from datadog_api_client.v2.model.synthetics_test_result_location import SyntheticsTestResultLocation
        from datadog_api_client.v2.model.synthetics_fast_test_result_detail import SyntheticsFastTestResultDetail
        from datadog_api_client.v2.model.synthetics_fast_test_sub_type import SyntheticsFastTestSubType
        from datadog_api_client.v2.model.synthetics_fast_test_type import SyntheticsFastTestType

        return {
            "device": (SyntheticsTestResultDevice,),
            "location": (SyntheticsTestResultLocation,),
            "result": (SyntheticsFastTestResultDetail,),
            "test_sub_type": (SyntheticsFastTestSubType,),
            "test_type": (SyntheticsFastTestType,),
            "test_version": (int,),
        }

    attribute_map = {
        "device": "device",
        "location": "location",
        "result": "result",
        "test_sub_type": "test_sub_type",
        "test_type": "test_type",
        "test_version": "test_version",
    }

    def __init__(
        self_,
        device: Union[SyntheticsTestResultDevice, UnsetType] = unset,
        location: Union[SyntheticsTestResultLocation, UnsetType] = unset,
        result: Union[SyntheticsFastTestResultDetail, UnsetType] = unset,
        test_sub_type: Union[SyntheticsFastTestSubType, UnsetType] = unset,
        test_type: Union[SyntheticsFastTestType, UnsetType] = unset,
        test_version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the fast test result.

        :param device: Device information for the test result (browser and mobile tests).
        :type device: SyntheticsTestResultDevice, optional

        :param location: Location information for a Synthetic test result.
        :type location: SyntheticsTestResultLocation, optional

        :param result: Detailed result data for the fast test run. The exact shape of nested fields
            ( ``request`` , ``response`` , ``assertions`` , etc.) depends on the test subtype.
        :type result: SyntheticsFastTestResultDetail, optional

        :param test_sub_type: Subtype of the Synthetic test that produced this result.
        :type test_sub_type: SyntheticsFastTestSubType, optional

        :param test_type: Type of the Synthetic fast test that produced this result.
        :type test_type: SyntheticsFastTestType, optional

        :param test_version: Version of the test at the time the fast test was triggered.
        :type test_version: int, optional
        """
        if device is not unset:
            kwargs["device"] = device
        if location is not unset:
            kwargs["location"] = location
        if result is not unset:
            kwargs["result"] = result
        if test_sub_type is not unset:
            kwargs["test_sub_type"] = test_sub_type
        if test_type is not unset:
            kwargs["test_type"] = test_type
        if test_version is not unset:
            kwargs["test_version"] = test_version
        super().__init__(kwargs)
