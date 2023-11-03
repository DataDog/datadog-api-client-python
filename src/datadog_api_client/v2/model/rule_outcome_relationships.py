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
    from datadog_api_client.v2.model.relationship_to_outcome import RelationshipToOutcome


class RuleOutcomeRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_outcome import RelationshipToOutcome

        return {
            "rule": (RelationshipToOutcome,),
        }

    attribute_map = {
        "rule": "rule",
    }

    def __init__(self_, rule: Union[RelationshipToOutcome, UnsetType] = unset, **kwargs):
        """
        The JSON:API relationship to a scorecard rule.

        :param rule: The JSON:API relationship to a scorecard outcome.
        :type rule: RelationshipToOutcome, optional
        """
        if rule is not unset:
            kwargs["rule"] = rule
        super().__init__(kwargs)
