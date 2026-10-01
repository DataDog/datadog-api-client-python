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
    from datadog_api_client.v2.model.archive_search_response_attributes import ArchiveSearchResponseAttributes
    from datadog_api_client.v2.model.archive_search_type import ArchiveSearchType


class ArchiveSearchResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.archive_search_response_attributes import ArchiveSearchResponseAttributes
        from datadog_api_client.v2.model.archive_search_type import ArchiveSearchType

        return {
            "attributes": (ArchiveSearchResponseAttributes,),
            "id": (str,),
            "type": (ArchiveSearchType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ArchiveSearchResponseAttributes, id: str, type: ArchiveSearchType, **kwargs):
        """
        Archive Search object.

        :param attributes: Attributes of an Archive Search.
        :type attributes: ArchiveSearchResponseAttributes

        :param id: Unique identifier of the Archive Search.
        :type id: str

        :param type: Archive Search resource type.
        :type type: ArchiveSearchType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
