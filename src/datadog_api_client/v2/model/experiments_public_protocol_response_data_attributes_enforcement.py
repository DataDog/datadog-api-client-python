# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ExperimentsPublicProtocolResponseDataAttributesEnforcement(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "confidence_interval_method": (str,),
            "confidence_level": (str,),
            "cuped_calculation": (str,),
            "default_duration": (str,),
            "environment": (str,),
            "flag_source": (str,),
            "multiple_testing_correction": (str,),
            "notifications": (str,),
            "primary_metric": (str,),
            "secondary_metrics": (str,),
            "split_by_exploration_dimensions": (str,),
            "subject_type": (str,),
            "targeting_rules": (str,),
            "traffic_exposure": (str,),
            "warehouse_exposure_source": (str,),
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
        confidence_interval_method: Union[str, UnsetType] = unset,
        confidence_level: Union[str, UnsetType] = unset,
        cuped_calculation: Union[str, UnsetType] = unset,
        default_duration: Union[str, UnsetType] = unset,
        environment: Union[str, UnsetType] = unset,
        flag_source: Union[str, UnsetType] = unset,
        multiple_testing_correction: Union[str, UnsetType] = unset,
        notifications: Union[str, UnsetType] = unset,
        primary_metric: Union[str, UnsetType] = unset,
        secondary_metrics: Union[str, UnsetType] = unset,
        split_by_exploration_dimensions: Union[str, UnsetType] = unset,
        subject_type: Union[str, UnsetType] = unset,
        targeting_rules: Union[str, UnsetType] = unset,
        traffic_exposure: Union[str, UnsetType] = unset,
        warehouse_exposure_source: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Controls that determine which protocol settings can be changed in an experiment.

        :param confidence_interval_method: LOCKED prevents changes to confidence interval method. EDITABLE permits changes.
        :type confidence_interval_method: str, optional

        :param confidence_level: LOCKED prevents changes to confidence level. EDITABLE permits changes.
        :type confidence_level: str, optional

        :param cuped_calculation: LOCKED prevents changes to CUPED variance reduction. EDITABLE permits changes.
        :type cuped_calculation: str, optional

        :param default_duration: LOCKED prevents changes to default duration. EDITABLE permits changes.
        :type default_duration: str, optional

        :param environment: LOCKED prevents changes to environment. EDITABLE permits changes.
        :type environment: str, optional

        :param flag_source: LOCKED prevents changes to feature flag source. EDITABLE permits changes.
        :type flag_source: str, optional

        :param multiple_testing_correction: LOCKED prevents changes to multiple testing correction. EDITABLE permits changes.
        :type multiple_testing_correction: str, optional

        :param notifications: LOCKED prevents changes to notifications. EDITABLE permits changes.
        :type notifications: str, optional

        :param primary_metric: LOCKED prevents changes to primary metric. EDITABLE permits changes.
        :type primary_metric: str, optional

        :param secondary_metrics: LOCKED prevents changes to secondary metrics. EDITABLE permits changes.
        :type secondary_metrics: str, optional

        :param split_by_exploration_dimensions: LOCKED prevents changes to result exploration dimensions. EDITABLE permits changes.
        :type split_by_exploration_dimensions: str, optional

        :param subject_type: LOCKED prevents changes to subject type. EDITABLE permits changes.
        :type subject_type: str, optional

        :param targeting_rules: LOCKED prevents changes to targeting rules. EDITABLE permits changes.
        :type targeting_rules: str, optional

        :param traffic_exposure: LOCKED prevents changes to traffic exposure. EDITABLE permits changes.
        :type traffic_exposure: str, optional

        :param warehouse_exposure_source: LOCKED prevents changes to warehouse exposure source. EDITABLE permits changes.
        :type warehouse_exposure_source: str, optional
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
