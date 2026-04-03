# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.exposure_schedule_request import ExposureScheduleRequest
    from datadog_api_client.v2.model.guardrail_metric_request import GuardrailMetricRequest
    from datadog_api_client.v2.model.targeting_rule_request import TargetingRuleRequest
    from datadog_api_client.v2.model.allocation_type import AllocationType
    from datadog_api_client.v2.model.variant_weight_request import VariantWeightRequest


class UpsertAllocationRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.exposure_schedule_request import ExposureScheduleRequest
        from datadog_api_client.v2.model.guardrail_metric_request import GuardrailMetricRequest
        from datadog_api_client.v2.model.targeting_rule_request import TargetingRuleRequest
        from datadog_api_client.v2.model.allocation_type import AllocationType
        from datadog_api_client.v2.model.variant_weight_request import VariantWeightRequest

        return {
            "experiment_id": (str, none_type),
            "exposure_schedule": (ExposureScheduleRequest,),
            "guardrail_metrics": ([GuardrailMetricRequest],),
            "id": (UUID,),
            "key": (str,),
            "name": (str,),
            "targeting_rules": ([TargetingRuleRequest],),
            "type": (AllocationType,),
            "variant_weights": ([VariantWeightRequest],),
        }

    attribute_map = {
        "experiment_id": "experiment_id",
        "exposure_schedule": "exposure_schedule",
        "guardrail_metrics": "guardrail_metrics",
        "id": "id",
        "key": "key",
        "name": "name",
        "targeting_rules": "targeting_rules",
        "type": "type",
        "variant_weights": "variant_weights",
    }

    def __init__(
        self_,
        key: str,
        name: str,
        type: AllocationType,
        experiment_id: Union[str, none_type, UnsetType] = unset,
        exposure_schedule: Union[ExposureScheduleRequest, UnsetType] = unset,
        guardrail_metrics: Union[List[GuardrailMetricRequest], UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        targeting_rules: Union[List[TargetingRuleRequest], UnsetType] = unset,
        variant_weights: Union[List[VariantWeightRequest], UnsetType] = unset,
        **kwargs,
    ):
        """
        Request to create or update a targeting rule (allocation) for a feature flag environment.

        :param experiment_id: The experiment ID for experiment-linked allocations.
        :type experiment_id: str, none_type, optional

        :param exposure_schedule: Progressive release request payload.
        :type exposure_schedule: ExposureScheduleRequest, optional

        :param guardrail_metrics: Guardrail metrics used to monitor and auto-pause or abort.
        :type guardrail_metrics: [GuardrailMetricRequest], optional

        :param id: The unique identifier of the targeting rule allocation.
        :type id: UUID, optional

        :param key: The unique key of the targeting rule allocation.
        :type key: str

        :param name: The display name of the targeting rule.
        :type name: str

        :param targeting_rules: Targeting rules that determine audience eligibility.
        :type targeting_rules: [TargetingRuleRequest], optional

        :param type: The type of targeting rule (called allocation in the API model).
        :type type: AllocationType

        :param variant_weights: Variant distribution weights.
        :type variant_weights: [VariantWeightRequest], optional
        """
        if experiment_id is not unset:
            kwargs["experiment_id"] = experiment_id
        if exposure_schedule is not unset:
            kwargs["exposure_schedule"] = exposure_schedule
        if guardrail_metrics is not unset:
            kwargs["guardrail_metrics"] = guardrail_metrics
        if id is not unset:
            kwargs["id"] = id
        if targeting_rules is not unset:
            kwargs["targeting_rules"] = targeting_rules
        if variant_weights is not unset:
            kwargs["variant_weights"] = variant_weights
        super().__init__(kwargs)

        self_.key = key
        self_.name = name
        self_.type = type
