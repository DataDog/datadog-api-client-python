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
    from datadog_api_client.v2.model.teams_ownership_rule_response_attributes import (
        TeamsOwnershipRuleResponseAttributes,
    )
    from datadog_api_client.v2.model.teams_ownership_rule_type import TeamsOwnershipRuleType


class TeamsOwnershipRuleResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_ownership_rule_response_attributes import (
            TeamsOwnershipRuleResponseAttributes,
        )
        from datadog_api_client.v2.model.teams_ownership_rule_type import TeamsOwnershipRuleType

        return {
            "attributes": (TeamsOwnershipRuleResponseAttributes,),
            "id": (str,),
            "type": (TeamsOwnershipRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: TeamsOwnershipRuleResponseAttributes, id: str, type: TeamsOwnershipRuleType, **kwargs
    ):
        """
        The JSON:API data envelope for a teams ownership rule.

        :param attributes: The attributes of a teams ownership rule.
        :type attributes: TeamsOwnershipRuleResponseAttributes

        :param id: A deterministic identifier derived from the rule's grouping key.
            This ID cannot be used to delete the rule directly; delete individual mappings
            using the ``mapping_id`` under ``teams`` instead.
        :type id: str

        :param type: The type of the resource. The value should always be teams_ownership_grouped_mappings.
        :type type: TeamsOwnershipRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
