# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DataProjectionQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "data_source": (str,),
            "indexes": ([str],),
            "query_string": (str,),
            "storage": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "indexes": "indexes",
        "query_string": "query_string",
        "storage": "storage",
    }

    def __init__(
        self_,
        data_source: str,
        query_string: str,
        indexes: Union[List[str], UnsetType] = unset,
        storage: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query configuration for a data projection request.

        :param data_source: Data source for the query.
        :type data_source: str

        :param indexes: List of indexes to query.
        :type indexes: [str], optional

        :param query_string: The query string to filter events.
        :type query_string: str

        :param storage: Storage location for the query.
        :type storage: str, optional
        """
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
