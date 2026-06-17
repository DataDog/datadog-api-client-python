# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_insight_event_compute import GovernanceInsightEventCompute


class GovernanceInsightEventQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_insight_event_compute import GovernanceInsightEventCompute

        return {
            "compute": (GovernanceInsightEventCompute,),
            "indexes": ([str],),
            "query": (str,),
        }

    attribute_map = {
        "compute": "compute",
        "indexes": "indexes",
        "query": "query",
    }

    def __init__(
        self_,
        indexes: List[str],
        query: str,
        compute: Union[GovernanceInsightEventCompute, UnsetType] = unset,
        **kwargs,
    ):
        """
        An event query used to compute an insight value.

        :param compute: The aggregation applied to an event query.
        :type compute: GovernanceInsightEventCompute, optional

        :param indexes: The event indexes the query runs against.
        :type indexes: [str]

        :param query: The event search query string.
        :type query: str
        """
        if compute is not unset:
            kwargs["compute"] = compute
        super().__init__(kwargs)

        self_.indexes = indexes
        self_.query = query
