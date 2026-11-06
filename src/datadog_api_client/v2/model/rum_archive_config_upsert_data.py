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
    from datadog_api_client.v2.model.rum_archive_config_upsert_attributes import RumArchiveConfigUpsertAttributes
    from datadog_api_client.v2.model.rum_archive_config_type import RumArchiveConfigType


class RumArchiveConfigUpsertData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_archive_config_upsert_attributes import RumArchiveConfigUpsertAttributes
        from datadog_api_client.v2.model.rum_archive_config_type import RumArchiveConfigType

        return {
            "attributes": (RumArchiveConfigUpsertAttributes,),
            "id": (str,),
            "type": (RumArchiveConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RumArchiveConfigUpsertAttributes, id: str, type: RumArchiveConfigType, **kwargs):
        """
        JSON:API resource.

        :param attributes: Archive configuration to save. When enabled is true, retention_days is required and must be 30, 90, or 180. When disabled, retention_days can be omitted.
        :type attributes: RumArchiveConfigUpsertAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: JSON:API resource type.
        :type type: RumArchiveConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
