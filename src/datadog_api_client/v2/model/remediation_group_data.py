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
    from datadog_api_client.v2.model.remediation_group_attributes import RemediationGroupAttributes
    from datadog_api_client.v2.model.remediation_group_relationships import RemediationGroupRelationships
    from datadog_api_client.v2.model.remediation_group_type import RemediationGroupType


class RemediationGroupData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_group_attributes import RemediationGroupAttributes
        from datadog_api_client.v2.model.remediation_group_relationships import RemediationGroupRelationships
        from datadog_api_client.v2.model.remediation_group_type import RemediationGroupType

        return {
            "attributes": (RemediationGroupAttributes,),
            "id": (str,),
            "relationships": (RemediationGroupRelationships,),
            "type": (RemediationGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: RemediationGroupAttributes,
        id: str,
        relationships: RemediationGroupRelationships,
        type: RemediationGroupType,
        **kwargs,
    ):
        """
        A remediation group.

        :param attributes: Attributes of a remediation group. Each group includes one kind object, depending on its grouping definition.
        :type attributes: RemediationGroupAttributes

        :param id: Remediation key of the group: the grouping definition ID, a colon, and the group's dimensions
            encoded in base64url. It identifies the group across searches.
        :type id: str

        :param relationships: Relationships of a remediation group.
        :type relationships: RemediationGroupRelationships

        :param type: Remediation groups resource type.
        :type type: RemediationGroupType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
