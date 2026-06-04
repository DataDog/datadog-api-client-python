# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.il2_cpp_sourcemap_attributes import IL2CPPSourcemapAttributes
    from datadog_api_client.v2.model.sourcemap_data_type import SourcemapDataType


class IL2CPPSourcemapData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.il2_cpp_sourcemap_attributes import IL2CPPSourcemapAttributes
        from datadog_api_client.v2.model.sourcemap_data_type import SourcemapDataType

        return {
            "attributes": (IL2CPPSourcemapAttributes,),
            "id": (str,),
            "type": (SourcemapDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: IL2CPPSourcemapAttributes, id: str, type: SourcemapDataType, **kwargs):
        """
        IL2CPP mapping file data object.

        :param attributes: Attributes of an IL2CPP mapping file.
        :type attributes: IL2CPPSourcemapAttributes

        :param id: The unique identifier of the source map.
        :type id: str

        :param type: The resource type for source map objects.
        :type type: SourcemapDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
