# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union

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


class ExperimentsDatadogMetricMeasureInput(ModelNormal):
    validations = {
        "column_type": {
            "min_length": 1,
        },
        "name": {
            "min_length": 1,
        },
        "source_subtype": {
            "min_length": 1,
        },
        "source_type": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "column_name": (str,),
            "column_type": (str,),
            "filters": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "name": (str,),
            "query": (str,),
            "source_definition_filter": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "source_subtype": (str,),
            "source_type": (str,),
        }

    attribute_map = {
        "column_name": "column_name",
        "column_type": "column_type",
        "filters": "filters",
        "name": "name",
        "query": "query",
        "source_definition_filter": "source_definition_filter",
        "source_subtype": "source_subtype",
        "source_type": "source_type",
    }

    def __init__(
        self_,
        column_type: str,
        name: str,
        source_subtype: str,
        source_type: str,
        column_name: Union[str, UnsetType] = unset,
        filters: Union[Any, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        source_definition_filter: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        Datadog source and query that supply values for the metric.

        :param column_name: Name of the Datadog event field used by this measure.
        :type column_name: str, optional

        :param column_type: Data type of the source column.
        :type column_type: str

        :param filters: Conditions used to select the metric's source data.
        :type filters: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the Datadog measure.
        :type name: str

        :param query: Query used to retrieve the Datadog measure.
        :type query: str, optional

        :param source_definition_filter: Filter applied to the Datadog source definition.
        :type source_definition_filter: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param source_subtype: Subtype of the Datadog data source.
        :type source_subtype: str

        :param source_type: Type of Datadog data source used for the measure.
        :type source_type: str
        """
        if column_name is not unset:
            kwargs["column_name"] = column_name
        if filters is not unset:
            kwargs["filters"] = filters
        if query is not unset:
            kwargs["query"] = query
        if source_definition_filter is not unset:
            kwargs["source_definition_filter"] = source_definition_filter
        super().__init__(kwargs)

        self_.column_type = column_type
        self_.name = name
        self_.source_subtype = source_subtype
        self_.source_type = source_type
