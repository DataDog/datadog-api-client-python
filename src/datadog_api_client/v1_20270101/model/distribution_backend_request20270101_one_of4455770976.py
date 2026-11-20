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
    from datadog_api_client.v1_20270101.model.request_style import RequestStyle
    from datadog_api_client.v1_20270101.model.log_query_definition import LogQueryDefinition


class DistributionBackendRequest20270101OneOf4455770976(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.request_style import RequestStyle
        from datadog_api_client.v1_20270101.model.log_query_definition import LogQueryDefinition

        return {
            "style": (RequestStyle,),
            "synthetics_batches": (LogQueryDefinition,),
        }

    attribute_map = {
        "style": "style",
        "synthetics_batches": "synthetics_batches",
    }

    def __init__(
        self_, synthetics_batches: LogQueryDefinition, style: Union[RequestStyle, UnsetType] = unset, **kwargs
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: RequestStyle, optional

        :param synthetics_batches: Test-only generated schema for the dashboard versioning proof of concept.
        :type synthetics_batches: LogQueryDefinition
        """
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.synthetics_batches = synthetics_batches
