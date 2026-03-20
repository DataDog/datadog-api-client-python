# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LogsExclusionFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "query": (str,),
            "sample_attribute": (str,),
            "sample_rate": (float,),
        }

    attribute_map = {
        "query": "query",
        "sample_attribute": "sample_attribute",
        "sample_rate": "sample_rate",
    }

    def __init__(
        self_,
        sample_rate: float,
        query: Union[str, UnsetType] = unset,
        sample_attribute: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Exclusion filter is defined by a query, a sampling rule, and a active/inactive toggle.

        :param query: Default query is ``*`` , meaning all logs flowing in the index would be excluded.
            Scope down exclusion filter to only a subset of logs with a log query.
        :type query: str, optional

        :param sample_attribute: Sample attribute to use for the sampling of logs going through this exclusion filter.
            When set, only the logs with the specified attribute are sampled.
        :type sample_attribute: str, optional

        :param sample_rate: Sample rate to apply to logs going through this exclusion filter,
            a value of 1.0 excludes all logs matching the query.
        :type sample_rate: float
        """
        if query is not unset:
            kwargs["query"] = query
        if sample_attribute is not unset:
            kwargs["sample_attribute"] = sample_attribute
        super().__init__(kwargs)

        self_.sample_rate = sample_rate
