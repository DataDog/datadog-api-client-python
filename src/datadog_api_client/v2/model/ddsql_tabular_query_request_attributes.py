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
    from datadog_api_client.v2.model.ddsql_tabular_query_time_window import DdsqlTabularQueryTimeWindow


class DdsqlTabularQueryRequestAttributes(ModelNormal):
    validations = {
        "row_limit": {
            "inclusive_maximum": 10000,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ddsql_tabular_query_time_window import DdsqlTabularQueryTimeWindow

        return {
            "query": (str,),
            "row_limit": (int,),
            "time": (DdsqlTabularQueryTimeWindow,),
        }

    attribute_map = {
        "query": "query",
        "row_limit": "row_limit",
        "time": "time",
    }

    def __init__(
        self_, query: str, time: DdsqlTabularQueryTimeWindow, row_limit: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Attributes describing the DDSQL query to execute.

        :param query: The DDSQL statement to execute. DDSQL is Datadog's SQL dialect, which is a subset
            of PostgreSQL, scoped to Datadog data sources.
        :type query: str

        :param row_limit: Cap on the number of rows returned. Defaults to 5,000 when omitted. Must be
            between 1 and 10,000 inclusive; values outside this range are rejected with 400.
        :type row_limit: int, optional

        :param time: Time window scoping the underlying data sources, expressed in Unix milliseconds
            since the epoch. Inclusive on ``from_timestamp`` , exclusive on ``to_timestamp``.
            Results from static tables (for example, ``dd.hosts`` ) are not affected by the
            time window, but the field must still be provided.
        :type time: DdsqlTabularQueryTimeWindow
        """
        if row_limit is not unset:
            kwargs["row_limit"] = row_limit
        super().__init__(kwargs)

        self_.query = query
        self_.time = time
