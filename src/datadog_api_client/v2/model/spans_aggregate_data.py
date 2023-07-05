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
    from datadog_api_client.v2.model.spans_aggregate_request_attributes import SpansAggregateRequestAttributes
    from datadog_api_client.v2.model.spans_aggregate_request_type import SpansAggregateRequestType


class SpansAggregateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_aggregate_request_attributes import SpansAggregateRequestAttributes
        from datadog_api_client.v2.model.spans_aggregate_request_type import SpansAggregateRequestType

        return {
            "attributes": (SpansAggregateRequestAttributes,),
            "type": (SpansAggregateRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SpansAggregateRequestAttributes, UnsetType] = unset,
        type: Union[SpansAggregateRequestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object containing the query content.

        :param attributes: The object containing all the query parameters.
        :type attributes: SpansAggregateRequestAttributes, optional

        :param type: The type of resource. The value should always be aggregate_request.
        :type type: SpansAggregateRequestType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
