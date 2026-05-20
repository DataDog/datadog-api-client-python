# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LLMObsDataDeletionRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "delay": (int,),
            "_from": (int,),
            "query": ({str: (str,)},),
            "to": (int,),
        }

    attribute_map = {
        "delay": "delay",
        "_from": "from",
        "query": "query",
        "to": "to",
    }

    def __init__(self_, _from: int, query: Dict[str, str], to: int, delay: Union[int, UnsetType] = unset, **kwargs):
        """
        Attributes for an LLM Observability data deletion request.

        :param delay: Optional delay in seconds before the deletion is executed.
        :type delay: int, optional

        :param _from: Start of the deletion time range in milliseconds since Unix epoch.
        :type _from: int

        :param query: Query filters selecting the data to delete. Must include a ``query`` key with an ``@trace_id`` filter.
        :type query: {str: (str,)}

        :param to: End of the deletion time range in milliseconds since Unix epoch.
        :type to: int
        """
        if delay is not unset:
            kwargs["delay"] = delay
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
