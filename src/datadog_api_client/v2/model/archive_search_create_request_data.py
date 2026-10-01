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
    from datadog_api_client.v2.model.archive_search_create_request_attributes import (
        ArchiveSearchCreateRequestAttributes,
    )
    from datadog_api_client.v2.model.archive_search_type import ArchiveSearchType


class ArchiveSearchCreateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.archive_search_create_request_attributes import (
            ArchiveSearchCreateRequestAttributes,
        )
        from datadog_api_client.v2.model.archive_search_type import ArchiveSearchType

        return {
            "attributes": (ArchiveSearchCreateRequestAttributes,),
            "type": (ArchiveSearchType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: ArchiveSearchCreateRequestAttributes, type: ArchiveSearchType, **kwargs):
        """
        Archive Search object to create.

        :param attributes: Attributes accepted when creating an Archive Search.
        :type attributes: ArchiveSearchCreateRequestAttributes

        :param type: Archive Search resource type.
        :type type: ArchiveSearchType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
