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


class CreateDataDeletionRequestBodyAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (int,),
            "indexes": ([str],),
            "query": ({str: (str,)},),
            "to": (int,),
        }

    attribute_map = {
        "_from": "from",
        "indexes": "indexes",
        "query": "query",
        "to": "to",
    }

    def __init__(
        self_, _from: int, query: Dict[str, str], to: int, indexes: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Attributes for creating a data deletion request.

        :param _from: Start of requested time window, milliseconds since Unix epoch.
        :type _from: int

        :param indexes: List of indexes for the search. If not provided, the search is performed in all indexes.
        :type indexes: [str], optional

        :param query: Query for creating a data deletion request.
        :type query: {str: (str,)}

        :param to: End of requested time window, milliseconds since Unix epoch.
        :type to: int
        """
        if indexes is not unset:
            kwargs["indexes"] = indexes
        super().__init__(kwargs)

        self_._from = _from
        self_.query = query
        self_.to = to
