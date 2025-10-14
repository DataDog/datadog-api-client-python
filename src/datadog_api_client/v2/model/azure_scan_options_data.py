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
    from datadog_api_client.v2.model.azure_scan_options_data_attributes import AzureScanOptionsDataAttributes
    from datadog_api_client.v2.model.azure_scan_options_data_type import AzureScanOptionsDataType


class AzureScanOptionsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.azure_scan_options_data_attributes import AzureScanOptionsDataAttributes
        from datadog_api_client.v2.model.azure_scan_options_data_type import AzureScanOptionsDataType

        return {
            "attributes": (AzureScanOptionsDataAttributes,),
            "id": (str,),
            "type": (AzureScanOptionsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: AzureScanOptionsDataType,
        attributes: Union[AzureScanOptionsDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Single Azure scan options entry.

        :param attributes: Attributes for Azure scan options configuration.
        :type attributes: AzureScanOptionsDataAttributes, optional

        :param id: The Azure subscription ID.
        :type id: str

        :param type: The type of the resource. The value should always be ``azure_scan_options``.
        :type type: AzureScanOptionsDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
