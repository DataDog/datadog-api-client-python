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
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_model_configuration import (
        MonitorFormulaAndFunctionDataQualityModelConfiguration,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_model_type_override import (
        MonitorFormulaAndFunctionDataQualityModelTypeOverride,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_source_to_target_config import (
        MonitorFormulaAndFunctionDataQualitySourceToTargetConfig,
    )


class MonitorFormulaAndFunctionDataQualityMonitorOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_model_configuration import (
            MonitorFormulaAndFunctionDataQualityModelConfiguration,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_model_type_override import (
            MonitorFormulaAndFunctionDataQualityModelTypeOverride,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_source_to_target_config import (
            MonitorFormulaAndFunctionDataQualitySourceToTargetConfig,
        )

        return {
            "crontab_override": (str,),
            "custom_sql": (str,),
            "custom_where": (str,),
            "group_by_columns": ([str],),
            "model_configuration": (MonitorFormulaAndFunctionDataQualityModelConfiguration,),
            "model_type_override": (MonitorFormulaAndFunctionDataQualityModelTypeOverride,),
            "sensitivity": (float,),
            "source_to_target_config": (MonitorFormulaAndFunctionDataQualitySourceToTargetConfig,),
        }

    attribute_map = {
        "crontab_override": "crontab_override",
        "custom_sql": "custom_sql",
        "custom_where": "custom_where",
        "group_by_columns": "group_by_columns",
        "model_configuration": "model_configuration",
        "model_type_override": "model_type_override",
        "sensitivity": "sensitivity",
        "source_to_target_config": "source_to_target_config",
    }

    def __init__(
        self_,
        crontab_override: Union[str, UnsetType] = unset,
        custom_sql: Union[str, UnsetType] = unset,
        custom_where: Union[str, UnsetType] = unset,
        group_by_columns: Union[List[str], UnsetType] = unset,
        model_configuration: Union[MonitorFormulaAndFunctionDataQualityModelConfiguration, UnsetType] = unset,
        model_type_override: Union[MonitorFormulaAndFunctionDataQualityModelTypeOverride, UnsetType] = unset,
        sensitivity: Union[float, UnsetType] = unset,
        source_to_target_config: Union[MonitorFormulaAndFunctionDataQualitySourceToTargetConfig, UnsetType] = unset,
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

        :param model_configuration: Tuning options for the anomaly detection model used by the monitor.
        :type model_configuration: MonitorFormulaAndFunctionDataQualityModelConfiguration, optional

        :param model_type_override: Override for the model type used in anomaly detection.
        :type model_type_override: MonitorFormulaAndFunctionDataQualityModelTypeOverride, optional

        :param sensitivity: Sensitivity of the anomaly detection model, expressed as a multiplier on the width
            of the predicted bounds. Higher values widen the bounds and produce fewer alerts;
            lower values tighten them and produce more alerts. Defaults to ``3.0``.
        :type sensitivity: float, optional

        :param source_to_target_config: Configuration for a source to target monitor, which compares the same measure
            across two data entities and alerts on the difference between them.
        :type source_to_target_config: MonitorFormulaAndFunctionDataQualitySourceToTargetConfig, optional
        """
        if crontab_override is not unset:
            kwargs["crontab_override"] = crontab_override
        if custom_sql is not unset:
            kwargs["custom_sql"] = custom_sql
        if custom_where is not unset:
            kwargs["custom_where"] = custom_where
        if group_by_columns is not unset:
            kwargs["group_by_columns"] = group_by_columns
        if model_configuration is not unset:
            kwargs["model_configuration"] = model_configuration
        if model_type_override is not unset:
            kwargs["model_type_override"] = model_type_override
        if sensitivity is not unset:
            kwargs["sensitivity"] = sensitivity
        if source_to_target_config is not unset:
            kwargs["source_to_target_config"] = source_to_target_config
        super().__init__(kwargs)
