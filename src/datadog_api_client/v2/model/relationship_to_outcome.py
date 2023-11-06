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
    from datadog_api_client.v2.model.relationship_to_outcome_data import RelationshipToOutcomeData


class RelationshipToOutcome(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_outcome_data import RelationshipToOutcomeData

        return {
            "data": (RelationshipToOutcomeData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[RelationshipToOutcomeData, UnsetType] = unset, **kwargs):
        """
        The JSON:API relationship to a scorecard outcome.

        :param data: The JSON:API relationship to an outcome, which returns the related rule id.
        :type data: RelationshipToOutcomeData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
