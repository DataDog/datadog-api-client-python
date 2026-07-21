# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ddsql_tabular_query_column import DdsqlTabularQueryColumn
    from datadog_api_client.v2.model.ddsql_tabular_query_state import DdsqlTabularQueryState


class DdsqlTabularQueryResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ddsql_tabular_query_column import DdsqlTabularQueryColumn
        from datadog_api_client.v2.model.ddsql_tabular_query_state import DdsqlTabularQueryState

        return {
            "columns": ([DdsqlTabularQueryColumn],),
            "query_id": (str,),
            "state": (DdsqlTabularQueryState,),
            "warnings": ([str],),
        }

    attribute_map = {
        "columns": "columns",
        "query_id": "query_id",
        "state": "state",
        "warnings": "warnings",
    }

    def __init__(
        self_,
        state: DdsqlTabularQueryState,
        columns: Union[List[DdsqlTabularQueryColumn], UnsetType] = unset,
        query_id: Union[str, UnsetType] = unset,
        warnings: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a DDSQL tabular query response. ``query_id`` is set when
        ``state`` is ``running`` ; ``columns`` is set when ``state`` is ``completed``.

        :param columns: Column-major result set. Each element carries one column's name, type, and values,
            with one value per row of the result. Set when ``state`` is ``completed``.
        :type columns: [DdsqlTabularQueryColumn], optional

        :param query_id: Opaque token to pass to the fetch endpoint to poll for results.
            Set when ``state`` is ``running`` and absent when ``state`` is ``completed``.
        :type query_id: str, optional

        :param state: Lifecycle state of a DDSQL tabular query response.
            ``running`` means the query is still executing and the client should poll
            the fetch endpoint with the returned ``query_id``. ``completed`` means the
            result set is inlined in ``columns`` and no further polling is required.
        :type state: DdsqlTabularQueryState

        :param warnings: Non-fatal messages emitted by the query engine while serving this response.
        :type warnings: [str], optional
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if query_id is not unset:
            kwargs["query_id"] = query_id
        if warnings is not unset:
            kwargs["warnings"] = warnings
        super().__init__(kwargs)

        self_.state = state
