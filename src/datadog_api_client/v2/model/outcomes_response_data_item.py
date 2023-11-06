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
    from datadog_api_client.v2.model.outcomes_batch_response_attributes import OutcomesBatchResponseAttributes
    from datadog_api_client.v2.model.rule_outcome_relationships import RuleOutcomeRelationships
    from datadog_api_client.v2.model.outcome_type import OutcomeType


class OutcomesResponseDataItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.outcomes_batch_response_attributes import OutcomesBatchResponseAttributes
        from datadog_api_client.v2.model.rule_outcome_relationships import RuleOutcomeRelationships
        from datadog_api_client.v2.model.outcome_type import OutcomeType

        return {
            "attributes": (OutcomesBatchResponseAttributes,),
            "id": (str,),
            "relationships": (RuleOutcomeRelationships,),
            "type": (OutcomeType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[OutcomesBatchResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[RuleOutcomeRelationships, UnsetType] = unset,
        type: Union[OutcomeType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single rule outcome.

        :param attributes: The JSON:API attributes for an outcome.
        :type attributes: OutcomesBatchResponseAttributes, optional

        :param id: The unique ID for a rule outcome.
        :type id: str, optional

        :param relationships: The JSON:API relationship to a scorecard rule.
        :type relationships: RuleOutcomeRelationships, optional

        :param type: The JSON:API type for an outcome.
        :type type: OutcomeType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
