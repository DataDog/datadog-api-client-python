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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_rule_data import RelationshipToRuleData


class RelationshipToRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_rule_data import RelationshipToRuleData

        return {
            "scorecard": (RelationshipToRuleData,),
        }

    attribute_map = {
        "scorecard": "scorecard",
    }

    def __init__(self_, scorecard: Union[RelationshipToRuleData, UnsetType] = unset, **kwargs):
        """
        Scorecard create rule response relationship.

        :param scorecard: Relationship data for a rule.
        :type scorecard: RelationshipToRuleData, optional
        """
        if scorecard is not unset:
            kwargs["scorecard"] = scorecard
        super().__init__(kwargs)
