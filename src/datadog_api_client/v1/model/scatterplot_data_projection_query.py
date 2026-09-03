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
    from datadog_api_client.v1.model.formula_and_function_events_data_source import FormulaAndFunctionEventsDataSource
    from datadog_api_client.v1.model.scatterplot_data_projection_query_storage import (
        ScatterplotDataProjectionQueryStorage,
    )


class ScatterplotDataProjectionQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.formula_and_function_events_data_source import (
            FormulaAndFunctionEventsDataSource,
        )
        from datadog_api_client.v1.model.scatterplot_data_projection_query_storage import (
            ScatterplotDataProjectionQueryStorage,
        )

        return {
            "data_source": (FormulaAndFunctionEventsDataSource,),
            "indexes": ([str],),
            "query_string": (str,),
            "storage": (ScatterplotDataProjectionQueryStorage,),
        }

    attribute_map = {
        "data_source": "data_source",
        "indexes": "indexes",
        "query_string": "query_string",
        "storage": "storage",
    }

    def __init__(
        self_,
        data_source: FormulaAndFunctionEventsDataSource,
        query_string: str,
        indexes: Union[List[str], UnsetType] = unset,
        storage: Union[ScatterplotDataProjectionQueryStorage, UnsetType] = unset,
        **kwargs,
    ):
        """
        The query for a scatterplot data projection request.

        :param data_source: Data source for event platform-based queries.
        :type data_source: FormulaAndFunctionEventsDataSource

        :param indexes: Indexes to search.
        :type indexes: [str], optional

        :param query_string: The search query string.
        :type query_string: str

        :param storage: Storage tier to query.
        :type storage: ScatterplotDataProjectionQueryStorage, optional
        """
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
