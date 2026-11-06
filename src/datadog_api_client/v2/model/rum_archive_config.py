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
    from datadog_api_client.v2.model.rum_archive_config_attributes import RumArchiveConfigAttributes
    from datadog_api_client.v2.model.rum_archive_config_type import RumArchiveConfigType


class RumArchiveConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_archive_config_attributes import RumArchiveConfigAttributes
        from datadog_api_client.v2.model.rum_archive_config_type import RumArchiveConfigType

        return {
            "attributes": (RumArchiveConfigAttributes,),
            "id": (str,),
            "type": (RumArchiveConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RumArchiveConfigAttributes, id: str, type: RumArchiveConfigType, **kwargs):
        """
        JSON:API resource.

        :param attributes: Archive configuration.
        :type attributes: RumArchiveConfigAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: JSON:API resource type.
        :type type: RumArchiveConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
