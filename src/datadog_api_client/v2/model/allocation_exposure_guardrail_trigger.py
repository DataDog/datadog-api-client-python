# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    UUID,
)


class AllocationExposureGuardrailTrigger(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "allocation_exposure_schedule_id": (UUID,),
            "created_at": (datetime,),
            "flagging_variant_id": (UUID,),
            "id": (UUID,),
            "metric_id": (str,),
            "triggered_action": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "allocation_exposure_schedule_id": "allocation_exposure_schedule_id",
        "created_at": "created_at",
        "flagging_variant_id": "flagging_variant_id",
        "id": "id",
        "metric_id": "metric_id",
        "triggered_action": "triggered_action",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        allocation_exposure_schedule_id: UUID,
        created_at: datetime,
        flagging_variant_id: UUID,
        id: UUID,
        metric_id: str,
        triggered_action: str,
        updated_at: datetime,
        **kwargs,
    ):
        """
        Guardrail trigger details for a progressive rollout.

        :param allocation_exposure_schedule_id: The progressive rollout ID this trigger belongs to.
        :type allocation_exposure_schedule_id: UUID

        :param created_at: The timestamp when this trigger was created.
        :type created_at: datetime

        :param flagging_variant_id: The variant ID that triggered this event.
        :type flagging_variant_id: UUID

        :param id: The unique identifier of the guardrail trigger.
        :type id: UUID

        :param metric_id: The metric ID associated with the trigger.
        :type metric_id: str

        :param triggered_action: The action that was triggered.
        :type triggered_action: str

        :param updated_at: The timestamp when this trigger was last updated.
        :type updated_at: datetime
        """
        super().__init__(kwargs)

        self_.allocation_exposure_schedule_id = allocation_exposure_schedule_id
        self_.created_at = created_at
        self_.flagging_variant_id = flagging_variant_id
        self_.id = id
        self_.metric_id = metric_id
        self_.triggered_action = triggered_action
        self_.updated_at = updated_at
