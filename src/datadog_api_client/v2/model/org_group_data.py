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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_group_attributes import OrgGroupAttributes
    from datadog_api_client.v2.model.org_group_relationships import OrgGroupRelationships
    from datadog_api_client.v2.model.org_group_type import OrgGroupType


class OrgGroupData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_attributes import OrgGroupAttributes
        from datadog_api_client.v2.model.org_group_relationships import OrgGroupRelationships
        from datadog_api_client.v2.model.org_group_type import OrgGroupType

        return {
            "attributes": (OrgGroupAttributes,),
            "id": (UUID,),
            "relationships": (OrgGroupRelationships,),
            "type": (OrgGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgGroupAttributes,
        id: UUID,
        type: OrgGroupType,
        relationships: Union[OrgGroupRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        An org group resource.

        :param attributes: Attributes of an org group.
        :type attributes: OrgGroupAttributes

        :param id: The ID of the org group.
        :type id: UUID

        :param relationships: Relationships of an org group.
        :type relationships: OrgGroupRelationships, optional

        :param type: Org groups resource type.
        :type type: OrgGroupType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
