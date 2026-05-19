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
    from datadog_api_client.v2.model.case_aggregate_response_attributes import CaseAggregateResponseAttributes


class CaseAggregateResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_aggregate_response_attributes import CaseAggregateResponseAttributes

        return {
            "attributes": (CaseAggregateResponseAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CaseAggregateResponseAttributes, id: str, type: str, **kwargs):
        """
        Data object containing the aggregation results, including total count and per-group breakdowns.

        :param attributes: Attributes of the aggregation result, including the total count across all groups and the per-group breakdowns.
        :type attributes: CaseAggregateResponseAttributes

        :param id: Aggregate response identifier.
        :type id: str

        :param type: Aggregate resource type.
        :type type: str
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
