# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class QueryResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hits": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
            "total": (int,),
        }

    attribute_map = {
        "hits": "hits",
        "total": "total",
    }

    def __init__(self_, hits: Union[List[Any], UnsetType] = unset, total: Union[int, UnsetType] = unset, **kwargs):
        """


        :param hits:
        :type hits: [bool, date, datetime, dict, float, int, list, str, UUID, none_type], optional

        :param total:
        :type total: int, optional
        """
        if hits is not unset:
            kwargs["hits"] = hits
        if total is not unset:
            kwargs["total"] = total
        super().__init__(kwargs)
