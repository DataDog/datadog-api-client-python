# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CaseLinkAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "child_entity_id": (str,),
            "child_entity_type": (str,),
            "parent_entity_id": (str,),
            "parent_entity_type": (str,),
            "relationship": (str,),
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
        child_entity_type: str,
        parent_entity_id: str,
        parent_entity_type: str,
        relationship: str,
        **kwargs,
    ):
        """
        Attributes describing a directional relationship between two entities (cases, incidents, or pages).

        :param child_entity_id: The UUID of the child (target) entity in the relationship.
        :type child_entity_id: str

        :param child_entity_type: The type of the child entity. Allowed values: ``CASE`` , ``INCIDENT`` , ``PAGE`` , ``AGENT_CONVERSATION``.
        :type child_entity_type: str

        :param parent_entity_id: The UUID of the parent (source) entity in the relationship.
        :type parent_entity_id: str

        :param parent_entity_type: The type of the parent entity. Allowed values: ``CASE`` , ``INCIDENT`` , ``PAGE`` , ``AGENT_CONVERSATION``.
        :type parent_entity_type: str

        :param relationship: The type of directional relationship. Allowed values: ``RELATES_TO`` (bidirectional association), ``CAUSES`` (parent causes child), ``BLOCKS`` (parent blocks child), ``DUPLICATES`` (parent duplicates child), ``PARENT_OF`` (hierarchical), ``SUCCESSOR_OF`` (sequence), ``ESCALATES_TO`` (priority escalation).
        :type relationship: str
        """
        super().__init__(kwargs)

        self_.child_entity_id = child_entity_id
        self_.child_entity_type = child_entity_type
        self_.parent_entity_id = parent_entity_id
        self_.parent_entity_type = parent_entity_type
        self_.relationship = relationship
