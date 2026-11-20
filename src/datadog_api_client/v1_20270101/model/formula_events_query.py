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
    from datadog_api_client.v1_20270101.model.events_calculated_field import EventsCalculatedField
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_definition_compute import (
        FormulaAndFunctionEventQueryDefinitionCompute,
    )
    from datadog_api_client.v1_20270101.model.formula_and_function_events_data_source import (
        FormulaAndFunctionEventsDataSource,
    )
    from datadog_api_client.v1_20270101.model.events_data_extraction import EventsDataExtraction
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by_config import (
        FormulaAndFunctionEventQueryGroupByConfig,
    )
    from datadog_api_client.v1_20270101.model.formula_events_query_search import FormulaEventsQuerySearch
    from datadog_api_client.v1_20270101.model.formula_semantic_mode import FormulaSemanticMode
    from datadog_api_client.v1_20270101.model.storage_type import StorageType
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by import (
        FormulaAndFunctionEventQueryGroupBy,
    )
    from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by_fields import (
        FormulaAndFunctionEventQueryGroupByFields,
    )


class FormulaEventsQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_calculated_field import EventsCalculatedField
        from datadog_api_client.v1_20270101.model.formula_and_function_event_query_definition_compute import (
            FormulaAndFunctionEventQueryDefinitionCompute,
        )
        from datadog_api_client.v1_20270101.model.formula_and_function_events_data_source import (
            FormulaAndFunctionEventsDataSource,
        )
        from datadog_api_client.v1_20270101.model.events_data_extraction import EventsDataExtraction
        from datadog_api_client.v1_20270101.model.formula_and_function_event_query_group_by_config import (
            FormulaAndFunctionEventQueryGroupByConfig,
        )
        from datadog_api_client.v1_20270101.model.formula_events_query_search import FormulaEventsQuerySearch
        from datadog_api_client.v1_20270101.model.formula_semantic_mode import FormulaSemanticMode
        from datadog_api_client.v1_20270101.model.storage_type import StorageType

        return {
            "calculated_fields": ([EventsCalculatedField],),
            "compute": (FormulaAndFunctionEventQueryDefinitionCompute,),
            "cross_org_uuids": ([str],),
            "data_source": (FormulaAndFunctionEventsDataSource,),
            "extractions": ([EventsDataExtraction],),
            "group_by": (FormulaAndFunctionEventQueryGroupByConfig,),
            "indexes": ([str],),
            "name": (str,),
            "search": (FormulaEventsQuerySearch,),
            "semantic_mode": (FormulaSemanticMode,),
            "storage": (StorageType,),
        }

    attribute_map = {
        "calculated_fields": "calculated_fields",
        "compute": "compute",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "extractions": "extractions",
        "group_by": "group_by",
        "indexes": "indexes",
        "name": "name",
        "search": "search",
        "semantic_mode": "semantic_mode",
        "storage": "storage",
    }

    def __init__(
        self_,
        compute: FormulaAndFunctionEventQueryDefinitionCompute,
        data_source: FormulaAndFunctionEventsDataSource,
        name: str,
        calculated_fields: Union[List[EventsCalculatedField], UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        extractions: Union[List[EventsDataExtraction], UnsetType] = unset,
        group_by: Union[
            FormulaAndFunctionEventQueryGroupByConfig,
            List[FormulaAndFunctionEventQueryGroupBy],
            FormulaAndFunctionEventQueryGroupByFields,
            UnsetType,
        ] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        search: Union[FormulaEventsQuerySearch, UnsetType] = unset,
        semantic_mode: Union[FormulaSemanticMode, UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param calculated_fields: Test-only generated schema for the dashboard versioning proof of concept.
        :type calculated_fields: [EventsCalculatedField], optional

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: FormulaAndFunctionEventQueryDefinitionCompute

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaAndFunctionEventsDataSource

        :param extractions: Test-only generated schema for the dashboard versioning proof of concept.
        :type extractions: [EventsDataExtraction], optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: FormulaAndFunctionEventQueryGroupByConfig, optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: FormulaEventsQuerySearch, optional

        :param semantic_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type semantic_mode: FormulaSemanticMode, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional
        """
        if calculated_fields is not unset:
            kwargs["calculated_fields"] = calculated_fields
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if extractions is not unset:
            kwargs["extractions"] = extractions
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if search is not unset:
            kwargs["search"] = search
        if semantic_mode is not unset:
            kwargs["semantic_mode"] = semantic_mode
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
