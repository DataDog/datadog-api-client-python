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
    from datadog_api_client.v2.model.on_call_page_link_entity_type import OnCallPageLinkEntityType
    from datadog_api_client.v2.model.on_call_page_link_relationship_type import OnCallPageLinkRelationshipType


class OnCallPageLinkAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_link_entity_type import OnCallPageLinkEntityType
        from datadog_api_client.v2.model.on_call_page_link_relationship_type import OnCallPageLinkRelationshipType

        return {
            "child_entity_id": (str,),
            "child_entity_type": (OnCallPageLinkEntityType,),
            "parent_entity_id": (str,),
            "parent_entity_type": (OnCallPageLinkEntityType,),
            "relationship": (OnCallPageLinkRelationshipType,),
        }

    attribute_map = {
        "child_entity_id": "child_entity_id",
        "child_entity_type": "child_entity_type",
        "parent_entity_id": "parent_entity_id",
        "parent_entity_type": "parent_entity_type",
        "relationship": "relationship",
    }

    def __init__(
        self_,
        child_entity_id: str,
        child_entity_type: OnCallPageLinkEntityType,
        parent_entity_id: str,
        parent_entity_type: OnCallPageLinkEntityType,
        relationship: OnCallPageLinkRelationshipType,
        **kwargs,
    ):
        """
        The attributes of a page link. A page can be the child of another Datadog resource
        (for example, when an incident triggers it), or the parent of one (for example, when the
        page is escalated to an incident).

        :param child_entity_id: The ID of the child resource.
        :type child_entity_id: str

        :param child_entity_type: The type of a resource linked to a page.
        :type child_entity_type: OnCallPageLinkEntityType

        :param parent_entity_id: The ID of the parent resource.
        :type parent_entity_id: str

        :param parent_entity_type: The type of a resource linked to a page.
        :type parent_entity_type: OnCallPageLinkEntityType

        :param relationship: How the parent resource relates to the child resource.
        :type relationship: OnCallPageLinkRelationshipType
        """
        super().__init__(kwargs)

        self_.child_entity_id = child_entity_id
        self_.child_entity_type = child_entity_type
        self_.parent_entity_id = parent_entity_id
        self_.parent_entity_type = parent_entity_type
        self_.relationship = relationship
