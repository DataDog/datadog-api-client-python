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
    from datadog_api_client.v2.model.spans_aggregate_bucket import SpansAggregateBucket
    from datadog_api_client.v2.model.spans_aggregate_response_metadata import SpansAggregateResponseMetadata


class SpansAggregateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_aggregate_bucket import SpansAggregateBucket
        from datadog_api_client.v2.model.spans_aggregate_response_metadata import SpansAggregateResponseMetadata

        return {
            "data": ([SpansAggregateBucket],),
            "meta": (SpansAggregateResponseMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[SpansAggregateBucket], UnsetType] = unset,
        meta: Union[SpansAggregateResponseMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        The response object for the spans aggregate API endpoint.

        :param data: The list of matching buckets, one item per bucket.
        :type data: [SpansAggregateBucket], optional

        :param meta: The metadata associated with a request.
        :type meta: SpansAggregateResponseMetadata, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
