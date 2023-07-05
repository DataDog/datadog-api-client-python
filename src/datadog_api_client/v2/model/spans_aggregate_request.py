# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.spans_aggregate_data import SpansAggregateData
    from datadog_api_client.v2.model.spans_compute import SpansCompute
    from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter
    from datadog_api_client.v2.model.spans_group_by import SpansGroupBy
    from datadog_api_client.v2.model.spans_query_options import SpansQueryOptions


@dataclass
class SpansAggregateRequestJSON:
    compute: Union[List[SpansCompute], UnsetType] = unset
    filter: Union[SpansQueryFilter, UnsetType] = unset
    group_by: Union[List[SpansGroupBy], UnsetType] = unset
    options: Union[SpansQueryOptions, UnsetType] = unset


class SpansAggregateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_aggregate_data import SpansAggregateData

        return {
            "data": (SpansAggregateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = SpansAggregateRequestJSON

    def __init__(self_, data: Union[SpansAggregateData, UnsetType] = unset, **kwargs):
        """
        The object sent with the request to retrieve a list of aggregated spans from your organization.

        :param data: The object containing the query content.
        :type data: SpansAggregateData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
