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
    from datadog_api_client.v2.model.synthetics_test_result_device_browser import SyntheticsTestResultDeviceBrowser
    from datadog_api_client.v2.model.synthetics_test_result_device_platform import SyntheticsTestResultDevicePlatform
    from datadog_api_client.v2.model.synthetics_test_result_device_resolution import (
        SyntheticsTestResultDeviceResolution,
    )


class SyntheticsTestResultDevice(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_device_browser import SyntheticsTestResultDeviceBrowser
        from datadog_api_client.v2.model.synthetics_test_result_device_platform import (
            SyntheticsTestResultDevicePlatform,
        )
        from datadog_api_client.v2.model.synthetics_test_result_device_resolution import (
            SyntheticsTestResultDeviceResolution,
        )

        return {
            "browser": (SyntheticsTestResultDeviceBrowser,),
            "id": (str,),
            "name": (str,),
            "platform": (SyntheticsTestResultDevicePlatform,),
            "resolution": (SyntheticsTestResultDeviceResolution,),
            "type": (str,),
        }

    attribute_map = {
        "browser": "browser",
        "id": "id",
        "name": "name",
        "platform": "platform",
        "resolution": "resolution",
        "type": "type",
    }

    def __init__(
        self_,
        browser: Union[SyntheticsTestResultDeviceBrowser, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        platform: Union[SyntheticsTestResultDevicePlatform, UnsetType] = unset,
        resolution: Union[SyntheticsTestResultDeviceResolution, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Device information for the test result (browser and mobile tests).

        :param browser: Browser information for the device used to run the test.
        :type browser: SyntheticsTestResultDeviceBrowser, optional

        :param id: Device identifier.
        :type id: str, optional

        :param name: Device name.
        :type name: str, optional

        :param platform: Platform information for the device used to run the test.
        :type platform: SyntheticsTestResultDevicePlatform, optional

        :param resolution: Screen resolution of the device used to run the test.
        :type resolution: SyntheticsTestResultDeviceResolution, optional

        :param type: Device type.
        :type type: str, optional
        """
        if browser is not unset:
            kwargs["browser"] = browser
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if platform is not unset:
            kwargs["platform"] = platform
        if resolution is not unset:
            kwargs["resolution"] = resolution
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
