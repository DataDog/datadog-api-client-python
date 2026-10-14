# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ExperimentsPatchProtocolEnforcementInput(ModelNormal):
    validations = {
        "confidence_interval_method": {},
        "confidence_level": {},
        "cuped_calculation": {},
        "default_duration": {},
        "environment": {},
        "flag_source": {},
        "multiple_testing_correction": {},
        "notifications": {},
        "primary_metric": {},
        "secondary_metrics": {},
        "split_by_exploration_dimensions": {},
        "subject_type": {},
        "targeting_rules": {},
        "traffic_exposure": {},
        "warehouse_exposure_source": {},
    }
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "confidence_interval_method": (str, none_type),
            "confidence_level": (str, none_type),
            "cuped_calculation": (str, none_type),
            "default_duration": (str, none_type),
            "environment": (str, none_type),
            "flag_source": (str, none_type),
            "multiple_testing_correction": (str, none_type),
            "notifications": (str, none_type),
            "primary_metric": (str, none_type),
            "secondary_metrics": (str, none_type),
            "split_by_exploration_dimensions": (str, none_type),
            "subject_type": (str, none_type),
            "targeting_rules": (str, none_type),
            "traffic_exposure": (str, none_type),
            "warehouse_exposure_source": (str, none_type),
        }

    attribute_map = {
        "confidence_interval_method": "confidence_interval_method",
        "confidence_level": "confidence_level",
        "cuped_calculation": "cuped_calculation",
        "default_duration": "default_duration",
        "environment": "environment",
        "flag_source": "flag_source",
        "multiple_testing_correction": "multiple_testing_correction",
        "notifications": "notifications",
        "primary_metric": "primary_metric",
        "secondary_metrics": "secondary_metrics",
        "split_by_exploration_dimensions": "split_by_exploration_dimensions",
        "subject_type": "subject_type",
        "targeting_rules": "targeting_rules",
        "traffic_exposure": "traffic_exposure",
        "warehouse_exposure_source": "warehouse_exposure_source",
    }

    def __init__(
        self_,
        confidence_interval_method: Union[str, none_type, UnsetType] = unset,
        confidence_level: Union[str, none_type, UnsetType] = unset,
        cuped_calculation: Union[str, none_type, UnsetType] = unset,
        default_duration: Union[str, none_type, UnsetType] = unset,
        environment: Union[str, none_type, UnsetType] = unset,
        flag_source: Union[str, none_type, UnsetType] = unset,
        multiple_testing_correction: Union[str, none_type, UnsetType] = unset,
        notifications: Union[str, none_type, UnsetType] = unset,
        primary_metric: Union[str, none_type, UnsetType] = unset,
        secondary_metrics: Union[str, none_type, UnsetType] = unset,
        split_by_exploration_dimensions: Union[str, none_type, UnsetType] = unset,
        subject_type: Union[str, none_type, UnsetType] = unset,
        targeting_rules: Union[str, none_type, UnsetType] = unset,
        traffic_exposure: Union[str, none_type, UnsetType] = unset,
        warehouse_exposure_source: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Partial lock map. Omitted fields remain unchanged. Null clears the whole map. Empty or null field values become ``EDITABLE`` , except ``subject_type`` , ``flag_source`` , and ``confidence_interval_method`` , which remain ``LOCKED``.

        :param confidence_interval_method: Always ``LOCKED``. The server keeps this setting locked regardless of the supplied value.
        :type confidence_interval_method: str, none_type, optional

        :param confidence_level: LOCKED prevents changes to confidence level. EDITABLE permits changes.
        :type confidence_level: str, none_type, optional

        :param cuped_calculation: LOCKED prevents changes to CUPED variance reduction. EDITABLE permits changes.
        :type cuped_calculation: str, none_type, optional

        :param default_duration: LOCKED prevents changes to default duration. EDITABLE permits changes.
        :type default_duration: str, none_type, optional

        :param environment: LOCKED prevents changes to environment. EDITABLE permits changes.
        :type environment: str, none_type, optional

        :param flag_source: Always LOCKED. The server keeps this setting locked regardless of the supplied value.
        :type flag_source: str, none_type, optional

        :param multiple_testing_correction: LOCKED prevents changes to multiple testing correction. EDITABLE permits changes.
        :type multiple_testing_correction: str, none_type, optional

        :param notifications: LOCKED prevents changes to notifications. EDITABLE permits changes.
        :type notifications: str, none_type, optional

        :param primary_metric: LOCKED prevents changes to primary metric. EDITABLE permits changes.
        :type primary_metric: str, none_type, optional

        :param secondary_metrics: LOCKED prevents changes to secondary metrics. EDITABLE permits changes.
        :type secondary_metrics: str, none_type, optional

        :param split_by_exploration_dimensions: LOCKED prevents changes to result exploration dimensions. EDITABLE permits changes.
        :type split_by_exploration_dimensions: str, none_type, optional

        :param subject_type: Always LOCKED. The server keeps this setting locked regardless of the supplied value.
        :type subject_type: str, none_type, optional

        :param targeting_rules: LOCKED prevents changes to targeting rules. EDITABLE permits changes.
        :type targeting_rules: str, none_type, optional

        :param traffic_exposure: LOCKED prevents changes to traffic exposure. EDITABLE permits changes.
        :type traffic_exposure: str, none_type, optional

        :param warehouse_exposure_source: LOCKED prevents changes to warehouse exposure source. EDITABLE permits changes.
        :type warehouse_exposure_source: str, none_type, optional
        """
        if confidence_interval_method is not unset:
            kwargs["confidence_interval_method"] = confidence_interval_method
        if confidence_level is not unset:
            kwargs["confidence_level"] = confidence_level
        if cuped_calculation is not unset:
            kwargs["cuped_calculation"] = cuped_calculation
        if default_duration is not unset:
            kwargs["default_duration"] = default_duration
        if environment is not unset:
            kwargs["environment"] = environment
        if flag_source is not unset:
            kwargs["flag_source"] = flag_source
        if multiple_testing_correction is not unset:
            kwargs["multiple_testing_correction"] = multiple_testing_correction
        if notifications is not unset:
            kwargs["notifications"] = notifications
        if primary_metric is not unset:
            kwargs["primary_metric"] = primary_metric
        if secondary_metrics is not unset:
            kwargs["secondary_metrics"] = secondary_metrics
        if split_by_exploration_dimensions is not unset:
            kwargs["split_by_exploration_dimensions"] = split_by_exploration_dimensions
        if subject_type is not unset:
            kwargs["subject_type"] = subject_type
        if targeting_rules is not unset:
            kwargs["targeting_rules"] = targeting_rules
        if traffic_exposure is not unset:
            kwargs["traffic_exposure"] = traffic_exposure
        if warehouse_exposure_source is not unset:
            kwargs["warehouse_exposure_source"] = warehouse_exposure_source
        super().__init__(kwargs)
