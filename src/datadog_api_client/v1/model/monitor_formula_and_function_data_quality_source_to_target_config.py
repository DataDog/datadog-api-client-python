# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_diff_type import (
        MonitorFormulaAndFunctionDataQualityDiffType,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_entity_metric_config import (
        MonitorFormulaAndFunctionDataQualityEntityMetricConfig,
    )


class MonitorFormulaAndFunctionDataQualitySourceToTargetConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_diff_type import (
            MonitorFormulaAndFunctionDataQualityDiffType,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_entity_metric_config import (
            MonitorFormulaAndFunctionDataQualityEntityMetricConfig,
        )

        return {
            "diff_type": (MonitorFormulaAndFunctionDataQualityDiffType,),
            "entity_type": (str,),
            "source": (MonitorFormulaAndFunctionDataQualityEntityMetricConfig,),
            "target": (MonitorFormulaAndFunctionDataQualityEntityMetricConfig,),
        }

    attribute_map = {
        "diff_type": "diff_type",
        "entity_type": "entity_type",
        "source": "source",
        "target": "target",
    }

    def __init__(
        self_,
        diff_type: MonitorFormulaAndFunctionDataQualityDiffType,
        entity_type: str,
        source: MonitorFormulaAndFunctionDataQualityEntityMetricConfig,
        target: MonitorFormulaAndFunctionDataQualityEntityMetricConfig,
        **kwargs,
    ):
        """
        Configuration for a source to target monitor, which compares the same measure
        across two data entities and alerts on the difference between them.

        :param diff_type: How the difference between the source and target measures is computed.
            ``absolute`` subtracts the two values, ``diff_percent`` expresses the difference
            as a percentage of the source value.
        :type diff_type: MonitorFormulaAndFunctionDataQualityDiffType

        :param entity_type: Type of the data entities being compared.
        :type entity_type: str

        :param source: Measure configuration for one side of a source to target comparison.
        :type source: MonitorFormulaAndFunctionDataQualityEntityMetricConfig

        :param target: Measure configuration for one side of a source to target comparison.
        :type target: MonitorFormulaAndFunctionDataQualityEntityMetricConfig
        """
        super().__init__(kwargs)

        self_.diff_type = diff_type
        self_.entity_type = entity_type
        self_.source = source
        self_.target = target
