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
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_snowflake_settings import (
        MonitorFormulaAndFunctionDataQualitySnowflakeSettings,
    )


class MonitorFormulaAndFunctionDataQualityPlatformSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_snowflake_settings import (
            MonitorFormulaAndFunctionDataQualitySnowflakeSettings,
        )

        return {
            "snowflake": (MonitorFormulaAndFunctionDataQualitySnowflakeSettings,),
        }

    attribute_map = {
        "snowflake": "snowflake",
    }

    def __init__(
        self_, snowflake: Union[MonitorFormulaAndFunctionDataQualitySnowflakeSettings, UnsetType] = unset, **kwargs
    ):
        """
        Platform-specific settings for a data quality monitor.

        :param snowflake: Snowflake-specific settings for a data quality monitor.
        :type snowflake: MonitorFormulaAndFunctionDataQualitySnowflakeSettings, optional
        """
        if snowflake is not unset:
            kwargs["snowflake"] = snowflake
        super().__init__(kwargs)
