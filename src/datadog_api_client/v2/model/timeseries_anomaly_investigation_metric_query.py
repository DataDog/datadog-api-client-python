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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_data_source import (
        TimeseriesAnomalyInvestigationDataSource,
    )


class TimeseriesAnomalyInvestigationMetricQuery(ModelNormal):
    validations = {
        "cross_org_uuids": {
            "max_items": 1,
        },
        "name": {
            "min_length": 1,
        },
        "query": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_data_source import (
            TimeseriesAnomalyInvestigationDataSource,
        )

        return {
            "aggregator": (str,),
            "cross_org_uuids": ([str],),
            "data_source": (TimeseriesAnomalyInvestigationDataSource,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "aggregator": "aggregator",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "name": "name",
        "query": "query",
    }

    def __init__(
        self_,
        data_source: TimeseriesAnomalyInvestigationDataSource,
        name: str,
        query: str,
        aggregator: Union[str, UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Metrics query referenced by a formula.

        :param aggregator: Optional scalar aggregator accepted for request compatibility. This field is ignored for timeseries queries.
        :type aggregator: str, optional

        :param cross_org_uuids: Optional organization UUID used for a cross-organization query. Each query accepts at most one UUID; use separate queries for separate organizations. Influential-tag analysis is currently unsupported for cross-organization queries, but anomaly detection still runs.
        :type cross_org_uuids: [str], optional

        :param data_source: Data source for an anomaly investigation query.
        :type data_source: TimeseriesAnomalyInvestigationDataSource

        :param name: Name used to reference this query from formulas.
        :type name: str

        :param query: Datadog metrics query expression.
        :type query: str
        """
        if aggregator is not unset:
            kwargs["aggregator"] = aggregator
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.name = name
        self_.query = query
