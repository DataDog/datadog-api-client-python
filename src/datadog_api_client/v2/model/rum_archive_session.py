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
    from datadog_api_client.v2.model.rum_archive_session_attributes import RUMArchiveSessionAttributes
    from datadog_api_client.v2.model.rum_archive_session_type import RUMArchiveSessionType


class RUMArchiveSession(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_archive_session_attributes import RUMArchiveSessionAttributes
        from datadog_api_client.v2.model.rum_archive_session_type import RUMArchiveSessionType

        return {
            "attributes": (RUMArchiveSessionAttributes,),
            "id": (str,),
            "type": (RUMArchiveSessionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: RUMArchiveSessionAttributes, id: str, type: RUMArchiveSessionType, **kwargs):
        """
        JSON:API resource.

        :param attributes: Archived session metadata.
        :type attributes: RUMArchiveSessionAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: JSON:API resource type.
        :type type: RUMArchiveSessionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
