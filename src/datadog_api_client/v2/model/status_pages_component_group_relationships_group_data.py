# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType


class StatusPagesComponentGroupRelationshipsGroupData(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_pages_component_group_type import StatusPagesComponentGroupType

        return {
            "id": (UUID,),
            "type": (StatusPagesComponentGroupType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: StatusPagesComponentGroupType, **kwargs):
        """


        :param id:
        :type id: UUID

        :param type: Components resource type.
        :type type: StatusPagesComponentGroupType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
