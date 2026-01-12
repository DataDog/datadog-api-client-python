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
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_model_type_override import (
        MonitorFormulaAndFunctionDataQualityModelTypeOverride,
    )


class MonitorFormulaAndFunctionDataQualityMonitorOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_model_type_override import (
            MonitorFormulaAndFunctionDataQualityModelTypeOverride,
        )

        return {
            "crontab_override": (str,),
            "custom_sql": (str,),
            "custom_where": (str,),
            "group_by_columns": ([str],),
            "model_type_override": (MonitorFormulaAndFunctionDataQualityModelTypeOverride,),
        }

    attribute_map = {
        "crontab_override": "crontab_override",
        "custom_sql": "custom_sql",
        "custom_where": "custom_where",
        "group_by_columns": "group_by_columns",
        "model_type_override": "model_type_override",
    }

    def __init__(
        self_,
        crontab_override: Union[str, UnsetType] = unset,
        custom_sql: Union[str, UnsetType] = unset,
        custom_where: Union[str, UnsetType] = unset,
        group_by_columns: Union[List[str], UnsetType] = unset,
        model_type_override: Union[MonitorFormulaAndFunctionDataQualityModelTypeOverride, UnsetType] = unset,
        **kwargs,
    ):
        """
        Monitor configuration options for data quality queries.

        :param crontab_override: Crontab expression to override the default schedule.
        :type crontab_override: str, optional

        :param custom_sql: Custom SQL query for the monitor.
        :type custom_sql: str, optional

        :param custom_where: Custom WHERE clause for the query.
        :type custom_where: str, optional

        :param group_by_columns: Columns to group results by.
        :type group_by_columns: [str], optional

        :param model_type_override: Override for the model type used in anomaly detection.
        :type model_type_override: MonitorFormulaAndFunctionDataQualityModelTypeOverride, optional
        """
        if crontab_override is not unset:
            kwargs["crontab_override"] = crontab_override
        if custom_sql is not unset:
            kwargs["custom_sql"] = custom_sql
        if custom_where is not unset:
            kwargs["custom_where"] = custom_where
        if group_by_columns is not unset:
            kwargs["group_by_columns"] = group_by_columns
        if model_type_override is not unset:
            kwargs["model_type_override"] = model_type_override
        super().__init__(kwargs)
