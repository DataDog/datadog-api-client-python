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
    from datadog_api_client.v2.model.azure_scan_options_input_update_data_attributes import (
        AzureScanOptionsInputUpdateDataAttributes,
    )
    from datadog_api_client.v2.model.azure_scan_options_input_update_data_type import (
        AzureScanOptionsInputUpdateDataType,
    )


class AzureScanOptionsInputUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.azure_scan_options_input_update_data_attributes import (
            AzureScanOptionsInputUpdateDataAttributes,
        )
        from datadog_api_client.v2.model.azure_scan_options_input_update_data_type import (
            AzureScanOptionsInputUpdateDataType,
        )

        return {
            "attributes": (AzureScanOptionsInputUpdateDataAttributes,),
            "id": (str,),
            "type": (AzureScanOptionsInputUpdateDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: AzureScanOptionsInputUpdateDataType,
        attributes: Union[AzureScanOptionsInputUpdateDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating the scan options of a single Azure subscription.

        :param attributes: Attributes for updating Azure scan options configuration.
        :type attributes: AzureScanOptionsInputUpdateDataAttributes, optional

        :param id: The Azure subscription ID.
        :type id: str

        :param type: Azure scan options resource type.
        :type type: AzureScanOptionsInputUpdateDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
