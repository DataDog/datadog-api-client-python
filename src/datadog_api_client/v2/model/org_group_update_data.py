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
    from datadog_api_client.v2.model.org_group_update_attributes import OrgGroupUpdateAttributes
    from datadog_api_client.v2.model.org_group_type import OrgGroupType


class OrgGroupUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_update_attributes import OrgGroupUpdateAttributes
        from datadog_api_client.v2.model.org_group_type import OrgGroupType

        return {
            "attributes": (OrgGroupUpdateAttributes,),
            "id": (UUID,),
            "type": (OrgGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OrgGroupUpdateAttributes, id: UUID, type: OrgGroupType, **kwargs):
        """
        Data for updating an org group.

        :param attributes: Attributes for updating an org group.
        :type attributes: OrgGroupUpdateAttributes

        :param id: The ID of the org group.
        :type id: UUID

        :param type: Org groups resource type.
        :type type: OrgGroupType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
