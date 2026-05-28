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
    from datadog_api_client.v2.model.device_details_data_attributes import DeviceDetailsDataAttributes
    from datadog_api_client.v2.model.device_details_data_type import DeviceDetailsDataType


class DeviceDetailsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.device_details_data_attributes import DeviceDetailsDataAttributes
        from datadog_api_client.v2.model.device_details_data_type import DeviceDetailsDataType

        return {
            "attributes": (DeviceDetailsDataAttributes,),
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
        attributes: Union[DeviceDetailsDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single device entry with full attribute detail.

        :param attributes: Extended set of attributes for a single End User Device Monitoring device,
            including detailed network and battery metrics.
        :type attributes: DeviceDetailsDataAttributes, optional

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
