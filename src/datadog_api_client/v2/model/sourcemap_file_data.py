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
    from datadog_api_client.v2.model.sourcemap_file_attributes import SourcemapFileAttributes
    from datadog_api_client.v2.model.sourcemap_file_data_type import SourcemapFileDataType


class SourcemapFileData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sourcemap_file_attributes import SourcemapFileAttributes
        from datadog_api_client.v2.model.sourcemap_file_data_type import SourcemapFileDataType

        return {
            "attributes": (SourcemapFileAttributes,),
            "id": (str,),
            "type": (SourcemapFileDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: SourcemapFileAttributes, id: str, type: SourcemapFileDataType, **kwargs):
        """
        JavaScript source map file data object.

        :param attributes: Attributes of a JavaScript source map file.
        :type attributes: SourcemapFileAttributes

        :param id: The unique identifier of the source map file, typically the path to the file.
        :type id: str

        :param type: The resource type for source map file objects.
        :type type: SourcemapFileDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
