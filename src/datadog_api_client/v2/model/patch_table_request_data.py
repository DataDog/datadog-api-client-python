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
    from datadog_api_client.v2.model.patch_table_request_data_attributes import PatchTableRequestDataAttributes
    from datadog_api_client.v2.model.patch_table_request_data_type import PatchTableRequestDataType


class PatchTableRequestData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_table_request_data_attributes import PatchTableRequestDataAttributes
        from datadog_api_client.v2.model.patch_table_request_data_type import PatchTableRequestDataType

        return {
            "attributes": (PatchTableRequestDataAttributes,),
            "type": (PatchTableRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchTableRequestDataType,
        attributes: Union[PatchTableRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object containing the partial table definition updates.

        :param attributes: Attributes that define the updates to the reference table's configuration and properties.
        :type attributes: PatchTableRequestDataAttributes, optional

        :param type: Reference table resource type.
        :type type: PatchTableRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
