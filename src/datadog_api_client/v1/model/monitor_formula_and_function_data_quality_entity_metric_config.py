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


class MonitorFormulaAndFunctionDataQualityEntityMetricConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "custom_sql": (str,),
            "custom_where": (str,),
            "entity_id": (str,),
            "entity_type": (str,),
            "group_by_columns": ([str],),
        }

    attribute_map = {
        "custom_sql": "custom_sql",
        "custom_where": "custom_where",
        "entity_id": "entity_id",
        "entity_type": "entity_type",
        "group_by_columns": "group_by_columns",
    }

    def __init__(
        self_,
        entity_id: str,
        entity_type: str,
        custom_sql: Union[str, UnsetType] = unset,
        custom_where: Union[str, UnsetType] = unset,
        group_by_columns: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Measure configuration for one side of a source to target comparison.

        :param custom_sql: Custom SQL query used to compute the measure for this entity.
        :type custom_sql: str, optional

        :param custom_where: Custom WHERE clause applied when computing the measure for this entity.
        :type custom_where: str, optional

        :param entity_id: Identifier of the data entity to measure.
        :type entity_id: str

        :param entity_type: Type of the data entity to measure.
        :type entity_type: str

        :param group_by_columns: Columns to group results by when computing the measure for this entity.
        :type group_by_columns: [str], optional
        """
        if custom_sql is not unset:
            kwargs["custom_sql"] = custom_sql
        if custom_where is not unset:
            kwargs["custom_where"] = custom_where
        if group_by_columns is not unset:
            kwargs["group_by_columns"] = group_by_columns
        super().__init__(kwargs)

        self_.entity_id = entity_id
        self_.entity_type = entity_type
