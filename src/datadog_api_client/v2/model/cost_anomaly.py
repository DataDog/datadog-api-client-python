# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_anomaly_correlated_tags import CostAnomalyCorrelatedTags
    from datadog_api_client.v2.model.cost_anomaly_dimensions import CostAnomalyDimensions
    from datadog_api_client.v2.model.cost_anomaly_dismissal import CostAnomalyDismissal


class CostAnomaly(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_anomaly_correlated_tags import CostAnomalyCorrelatedTags
        from datadog_api_client.v2.model.cost_anomaly_dimensions import CostAnomalyDimensions
        from datadog_api_client.v2.model.cost_anomaly_dismissal import CostAnomalyDismissal

        return {
            "actual_cost": (float,),
            "anomalous_cost_change": (float,),
            "anomaly_end": (int,),
            "anomaly_start": (int,),
            "correlated_tags": (CostAnomalyCorrelatedTags,),
            "dimensions": (CostAnomalyDimensions,),
            "dismissal": (CostAnomalyDismissal,),
            "max_cost": (float,),
            "provider": (str,),
            "query": (str,),
            "uuid": (str,),
        }

    attribute_map = {
        "actual_cost": "actual_cost",
        "anomalous_cost_change": "anomalous_cost_change",
        "anomaly_end": "anomaly_end",
        "anomaly_start": "anomaly_start",
        "correlated_tags": "correlated_tags",
        "dimensions": "dimensions",
        "dismissal": "dismissal",
        "max_cost": "max_cost",
        "provider": "provider",
        "query": "query",
        "uuid": "uuid",
    }

    def __init__(
        self_,
        actual_cost: float,
        anomalous_cost_change: float,
        anomaly_end: int,
        anomaly_start: int,
        correlated_tags: Union[CostAnomalyCorrelatedTags, none_type],
        dimensions: CostAnomalyDimensions,
        max_cost: float,
        provider: str,
        query: str,
        uuid: str,
        dismissal: Union[CostAnomalyDismissal, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single detected Cloud Cost Management anomaly.

        :param actual_cost: Actual cost incurred during the anomaly window.
        :type actual_cost: float

        :param anomalous_cost_change: Anomalous cost change relative to the expected baseline.
        :type anomalous_cost_change: float

        :param anomaly_end: Anomaly end timestamp in Unix milliseconds.
        :type anomaly_end: int

        :param anomaly_start: Anomaly start timestamp in Unix milliseconds.
        :type anomaly_start: int

        :param correlated_tags: Map of correlated tag keys to the list of correlated tag values.
        :type correlated_tags: CostAnomalyCorrelatedTags, none_type

        :param dimensions: Map of cost dimension keys to their values for the anomaly grouping.
        :type dimensions: CostAnomalyDimensions

        :param dismissal: Resolution metadata for an anomaly that has been dismissed.
        :type dismissal: CostAnomalyDismissal, optional

        :param max_cost: Maximum cost observed during the anomaly window.
        :type max_cost: float

        :param provider: Cloud or SaaS provider associated with the anomaly (for example ``aws`` , ``gcp`` , ``azure`` ).
        :type provider: str

        :param query: The metrics query that detected the anomaly.
        :type query: str

        :param uuid: The unique identifier of the anomaly.
        :type uuid: str
        """
        if dismissal is not unset:
            kwargs["dismissal"] = dismissal
        super().__init__(kwargs)

        self_.actual_cost = actual_cost
        self_.anomalous_cost_change = anomalous_cost_change
        self_.anomaly_end = anomaly_end
        self_.anomaly_start = anomaly_start
        self_.correlated_tags = correlated_tags
        self_.dimensions = dimensions
        self_.max_cost = max_cost
        self_.provider = provider
        self_.query = query
        self_.uuid = uuid
