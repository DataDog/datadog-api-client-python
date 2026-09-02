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
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_diff_function import (
        MonitorFormulaAndFunctionDataQualityDiffFunction,
    )
    from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_model_bounds_override import (
        MonitorFormulaAndFunctionDataQualityModelBoundsOverride,
    )


class MonitorFormulaAndFunctionDataQualityModelConfiguration(ModelNormal):
    validations = {
        "auto_resolve_days": {
            "inclusive_maximum": 365,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_diff_function import (
            MonitorFormulaAndFunctionDataQualityDiffFunction,
        )
        from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_model_bounds_override import (
            MonitorFormulaAndFunctionDataQualityModelBoundsOverride,
        )

        return {
            "auto_resolve_days": (int,),
            "enable_flatline_detection": (bool,),
            "function": (MonitorFormulaAndFunctionDataQualityDiffFunction,),
            "min_lower_bound_size": (float,),
            "min_upper_bound_size": (float,),
            "model_bounds_override": (MonitorFormulaAndFunctionDataQualityModelBoundsOverride,),
        }

    attribute_map = {
        "auto_resolve_days": "auto_resolve_days",
        "enable_flatline_detection": "enable_flatline_detection",
        "function": "function",
        "min_lower_bound_size": "min_lower_bound_size",
        "min_upper_bound_size": "min_upper_bound_size",
        "model_bounds_override": "model_bounds_override",
    }

    def __init__(
        self_,
        auto_resolve_days: Union[int, UnsetType] = unset,
        enable_flatline_detection: Union[bool, UnsetType] = unset,
        function: Union[MonitorFormulaAndFunctionDataQualityDiffFunction, UnsetType] = unset,
        min_lower_bound_size: Union[float, UnsetType] = unset,
        min_upper_bound_size: Union[float, UnsetType] = unset,
        model_bounds_override: Union[MonitorFormulaAndFunctionDataQualityModelBoundsOverride, UnsetType] = unset,
        **kwargs,
    ):
        """
        Tuning options for the anomaly detection model used by the monitor.

        :param auto_resolve_days: Number of days after which an open alert is automatically resolved.
            When unset, alerts stay open until the measure returns within bounds.
        :type auto_resolve_days: int, optional

        :param enable_flatline_detection: Whether to alert when the measure stops changing entirely.
            Defaults to ``true``.
        :type enable_flatline_detection: bool, optional

        :param function: Function applied to the measure before it is compared against the predicted bounds.
        :type function: MonitorFormulaAndFunctionDataQualityDiffFunction, optional

        :param min_lower_bound_size: Minimum distance between the predicted value and the lower bound. Widening the
            lower bound to at least this size suppresses alerts on small downward deviations.
            When unset, no minimum is enforced.
        :type min_lower_bound_size: float, optional

        :param min_upper_bound_size: Minimum distance between the predicted value and the upper bound. Widening the
            upper bound to at least this size suppresses alerts on small upward deviations.
            When unset, no minimum is enforced.
        :type min_upper_bound_size: float, optional

        :param model_bounds_override: Restricts which predicted bound the monitor alerts on. ``UPPER_ONLY`` alerts only when
            the measure rises above the upper bound, ``LOWER_ONLY`` only when it falls below the
            lower bound. When unset, the monitor alerts on both.
        :type model_bounds_override: MonitorFormulaAndFunctionDataQualityModelBoundsOverride, optional
        """
        if auto_resolve_days is not unset:
            kwargs["auto_resolve_days"] = auto_resolve_days
        if enable_flatline_detection is not unset:
            kwargs["enable_flatline_detection"] = enable_flatline_detection
        if function is not unset:
            kwargs["function"] = function
        if min_lower_bound_size is not unset:
            kwargs["min_lower_bound_size"] = min_lower_bound_size
        if min_upper_bound_size is not unset:
            kwargs["min_upper_bound_size"] = min_upper_bound_size
        if model_bounds_override is not unset:
            kwargs["model_bounds_override"] = model_bounds_override
        super().__init__(kwargs)
