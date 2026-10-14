# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExperimentsReplaceProtocolEnforcementInput(ModelNormal):
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
        confidence_interval_method: str,
        confidence_level: str,
        cuped_calculation: str,
        default_duration: str,
        environment: str,
        flag_source: str,
        multiple_testing_correction: str,
        notifications: str,
        primary_metric: str,
        secondary_metrics: str,
        split_by_exploration_dimensions: str,
        subject_type: str,
        targeting_rules: str,
        traffic_exposure: str,
        warehouse_exposure_source: str,
        **kwargs,
    ):
        """
        Complete lock map. Omit this object to preserve current locks. Null is rejected; every field is required.

        :param confidence_interval_method: Always LOCKED. The server keeps this setting locked regardless of the supplied value.
        :type confidence_interval_method: str

        :param confidence_level: LOCKED prevents changes to confidence level. EDITABLE permits changes.
        :type confidence_level: str

        :param cuped_calculation: LOCKED prevents changes to CUPED variance reduction. EDITABLE permits changes.
        :type cuped_calculation: str

        :param default_duration: LOCKED prevents changes to default duration. EDITABLE permits changes.
        :type default_duration: str

        :param environment: LOCKED prevents changes to environment. EDITABLE permits changes.
        :type environment: str

        :param flag_source: Always LOCKED. The server keeps this setting locked regardless of the supplied value.
        :type flag_source: str

        :param multiple_testing_correction: LOCKED prevents changes to multiple testing correction. EDITABLE permits changes.
        :type multiple_testing_correction: str

        :param notifications: LOCKED prevents changes to notifications. EDITABLE permits changes.
        :type notifications: str

        :param primary_metric: LOCKED prevents changes to primary metric. EDITABLE permits changes.
        :type primary_metric: str

        :param secondary_metrics: LOCKED prevents changes to secondary metrics. EDITABLE permits changes.
        :type secondary_metrics: str

        :param split_by_exploration_dimensions: LOCKED prevents changes to result exploration dimensions. EDITABLE permits changes.
        :type split_by_exploration_dimensions: str

        :param subject_type: Always LOCKED. The server keeps this setting locked regardless of the supplied value.
        :type subject_type: str

        :param targeting_rules: LOCKED prevents changes to targeting rules. EDITABLE permits changes.
        :type targeting_rules: str

        :param traffic_exposure: LOCKED prevents changes to traffic exposure. EDITABLE permits changes.
        :type traffic_exposure: str

        :param warehouse_exposure_source: LOCKED prevents changes to warehouse exposure source. EDITABLE permits changes.
        :type warehouse_exposure_source: str
        """
        super().__init__(kwargs)

        self_.confidence_interval_method = confidence_interval_method
        self_.confidence_level = confidence_level
        self_.cuped_calculation = cuped_calculation
        self_.default_duration = default_duration
        self_.environment = environment
        self_.flag_source = flag_source
        self_.multiple_testing_correction = multiple_testing_correction
        self_.notifications = notifications
        self_.primary_metric = primary_metric
        self_.secondary_metrics = secondary_metrics
        self_.split_by_exploration_dimensions = split_by_exploration_dimensions
        self_.subject_type = subject_type
        self_.targeting_rules = targeting_rules
        self_.traffic_exposure = traffic_exposure
        self_.warehouse_exposure_source = warehouse_exposure_source
