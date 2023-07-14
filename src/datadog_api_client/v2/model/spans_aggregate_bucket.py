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
    from datadog_api_client.v2.model.spans_aggregate_bucket_attributes import SpansAggregateBucketAttributes
    from datadog_api_client.v2.model.spans_aggregate_bucket_type import SpansAggregateBucketType


class SpansAggregateBucket(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_aggregate_bucket_attributes import SpansAggregateBucketAttributes
        from datadog_api_client.v2.model.spans_aggregate_bucket_type import SpansAggregateBucketType

        return {
            "attributes": (SpansAggregateBucketAttributes,),
            "id": (str,),
            "type": (SpansAggregateBucketType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SpansAggregateBucketAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SpansAggregateBucketType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Spans aggregate.

        :param attributes: A bucket values.
        :type attributes: SpansAggregateBucketAttributes, optional

        :param id: ID of the spans aggregate.
        :type id: str, optional

        :param type: The spans aggregate bucket type.
        :type type: SpansAggregateBucketType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
