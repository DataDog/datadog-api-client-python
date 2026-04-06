# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.allocation_exposure_schedule import AllocationExposureSchedule
    from datadog_api_client.v2.model.guardrail_metric import GuardrailMetric
    from datadog_api_client.v2.model.targeting_rule import TargetingRule
    from datadog_api_client.v2.model.allocation_type import AllocationType
    from datadog_api_client.v2.model.variant_weight import VariantWeight


class Allocation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.allocation_exposure_schedule import AllocationExposureSchedule
        from datadog_api_client.v2.model.guardrail_metric import GuardrailMetric
        from datadog_api_client.v2.model.targeting_rule import TargetingRule
        from datadog_api_client.v2.model.allocation_type import AllocationType
        from datadog_api_client.v2.model.variant_weight import VariantWeight

        return {
            "created_at": (datetime,),
            "environment_ids": ([UUID],),
            "experiment_id": (str, none_type),
            "exposure_schedule": (AllocationExposureSchedule,),
            "guardrail_metrics": ([GuardrailMetric],),
            "id": (UUID,),
            "key": (str,),
            "name": (str,),
            "order_position": (int,),
            "targeting_rules": ([TargetingRule],),
            "type": (AllocationType,),
            "updated_at": (datetime,),
            "variant_weights": ([VariantWeight],),
        }

    attribute_map = {
        "created_at": "created_at",
        "environment_ids": "environment_ids",
        "experiment_id": "experiment_id",
        "exposure_schedule": "exposure_schedule",
        "guardrail_metrics": "guardrail_metrics",
        "id": "id",
        "key": "key",
        "name": "name",
        "order_position": "order_position",
        "targeting_rules": "targeting_rules",
        "type": "type",
        "updated_at": "updated_at",
        "variant_weights": "variant_weights",
    }

    def __init__(
        self_,
        created_at: datetime,
        environment_ids: List[UUID],
        guardrail_metrics: List[GuardrailMetric],
        key: str,
        name: str,
        order_position: int,
        targeting_rules: List[TargetingRule],
        type: AllocationType,
        updated_at: datetime,
        variant_weights: List[VariantWeight],
        experiment_id: Union[str, none_type, UnsetType] = unset,
        exposure_schedule: Union[AllocationExposureSchedule, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Targeting rule (allocation) details for a feature flag environment.

        :param created_at: The timestamp when the targeting rule allocation was created.
        :type created_at: datetime

        :param environment_ids: Environment IDs associated with this targeting rule allocation.
        :type environment_ids: [UUID]

        :param experiment_id: The experiment ID linked to this targeting rule allocation.
        :type experiment_id: str, none_type, optional

        :param exposure_schedule: Progressive release details for a targeting rule allocation.
        :type exposure_schedule: AllocationExposureSchedule, optional

        :param guardrail_metrics: Guardrail metrics associated with this targeting rule allocation.
        :type guardrail_metrics: [GuardrailMetric]

        :param id: The unique identifier of the targeting rule allocation.
        :type id: UUID, optional

        :param key: The unique key of the targeting rule allocation.
        :type key: str

        :param name: The display name of the targeting rule.
        :type name: str

        :param order_position: Sort order position within the environment.
        :type order_position: int

        :param targeting_rules: Conditions associated with this targeting rule allocation.
        :type targeting_rules: [TargetingRule]

        :param type: The type of targeting rule (called allocation in the API model).
        :type type: AllocationType

        :param updated_at: The timestamp when the targeting rule allocation was last updated.
        :type updated_at: datetime

        :param variant_weights: Weighted variant assignments for this targeting rule allocation.
        :type variant_weights: [VariantWeight]
        """
        if experiment_id is not unset:
            kwargs["experiment_id"] = experiment_id
        if exposure_schedule is not unset:
            kwargs["exposure_schedule"] = exposure_schedule
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.environment_ids = environment_ids
        self_.guardrail_metrics = guardrail_metrics
        self_.key = key
        self_.name = name
        self_.order_position = order_position
        self_.targeting_rules = targeting_rules
        self_.type = type
        self_.updated_at = updated_at
        self_.variant_weights = variant_weights
