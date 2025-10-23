# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LogsSchemaCategoryMapperFallback(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "sources": ({str: ([str],)},),
            "values": ({str: (str,)},),
        }

    attribute_map = {
        "sources": "sources",
        "values": "values",
    }

    def __init__(
        self_,
        sources: Union[Dict[str, List[str]], UnsetType] = unset,
        values: Union[Dict[str, str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Used to override hardcoded category values with a value pulled from a source attribute on the log.

        :param sources: Fallback sources used to populate value of field.
        :type sources: {str: ([str],)}, optional

        :param values: Values that define when the fallback is used.
        :type values: {str: (str,)}, optional
        """
        if sources is not unset:
            kwargs["sources"] = sources
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
