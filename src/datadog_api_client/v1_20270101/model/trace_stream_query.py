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
    from datadog_api_client.v1_20270101.model.events_context import EventsContext
    from datadog_api_client.v1_20270101.model.trace_stream_query_data_source import TraceStreamQueryDataSource
    from datadog_api_client.v1_20270101.model.formula_semantic_mode import FormulaSemanticMode
    from datadog_api_client.v1_20270101.model.trace_stream_query20270101_sort import TraceStreamQuery20270101Sort
    from datadog_api_client.v1_20270101.model.list_stream_sort import ListStreamSort


class TraceStreamQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_context import EventsContext
        from datadog_api_client.v1_20270101.model.trace_stream_query_data_source import TraceStreamQueryDataSource
        from datadog_api_client.v1_20270101.model.formula_semantic_mode import FormulaSemanticMode
        from datadog_api_client.v1_20270101.model.trace_stream_query20270101_sort import TraceStreamQuery20270101Sort

        return {
            "context": (EventsContext,),
            "cross_org_uuids": ([str],),
            "data_source": (TraceStreamQueryDataSource,),
            "indexes": ([str],),
            "query_string": (str,),
            "semantic_mode": (FormulaSemanticMode,),
            "sort": (TraceStreamQuery20270101Sort,),
        }

    attribute_map = {
        "context": "context",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "indexes": "indexes",
        "query_string": "query_string",
        "semantic_mode": "semantic_mode",
        "sort": "sort",
    }

    def __init__(
        self_,
        data_source: TraceStreamQueryDataSource,
        query_string: str,
        context: Union[EventsContext, UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        semantic_mode: Union[FormulaSemanticMode, UnsetType] = unset,
        sort: Union[TraceStreamQuery20270101Sort, ListStreamSort, List[ListStreamSort], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param context: Test-only generated schema for the dashboard versioning proof of concept.
        :type context: EventsContext, optional

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: TraceStreamQueryDataSource

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str

        :param semantic_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type semantic_mode: FormulaSemanticMode, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: TraceStreamQuery20270101Sort, optional
        """
        if context is not unset:
            kwargs["context"] = context
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if semantic_mode is not unset:
            kwargs["semantic_mode"] = semantic_mode
        if sort is not unset:
            kwargs["sort"] = sort
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
