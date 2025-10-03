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
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_table_request_data_attributes import PatchTableRequestDataAttributes
        from datadog_api_client.v2.model.patch_table_request_data_type import PatchTableRequestDataType

        return {
            "attributes": (PatchTableRequestDataAttributes,),
            "id": (str,),
            "type": (PatchTableRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchTableRequestDataType,
        attributes: Union[PatchTableRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``PatchTableRequestData`` object.

        :param attributes: The definition of ``PatchTableRequestDataAttributes`` object.
        :type attributes: PatchTableRequestDataAttributes, optional

        :param id: The ID of the reference table.
        :type id: str, optional

        :param type: Reference table resource type.
        :type type: PatchTableRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
