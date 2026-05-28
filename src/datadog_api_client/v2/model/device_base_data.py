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
    from datadog_api_client.v2.model.device_base_data_attributes import DeviceBaseDataAttributes
    from datadog_api_client.v2.model.device_details_data_type import DeviceDetailsDataType


class DeviceBaseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.device_base_data_attributes import DeviceBaseDataAttributes
        from datadog_api_client.v2.model.device_details_data_type import DeviceDetailsDataType

        return {
            "attributes": (DeviceBaseDataAttributes,),
            "id": (str,),
            "type": (DeviceDetailsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: DeviceDetailsDataType,
        attributes: Union[DeviceBaseDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single device entry as returned by the list devices endpoint.

        :param attributes: Common health and identity attributes shared by every End User Device Monitoring device record.
        :type attributes: DeviceBaseDataAttributes, optional

        :param id: Unique identifier of the device. Matches the Datadog host identifier.
        :type id: str

        :param type: Devices resource type.
        :type type: DeviceDetailsDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
