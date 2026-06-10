# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ownership_feedback_action import OwnershipFeedbackAction
    from datadog_api_client.v2.model.ownership_inference_status import OwnershipInferenceStatus
    from datadog_api_client.v2.model.ownership_owner_type import OwnershipOwnerType


class OwnershipFeedbackResultAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_feedback_action import OwnershipFeedbackAction
        from datadog_api_client.v2.model.ownership_inference_status import OwnershipInferenceStatus
        from datadog_api_client.v2.model.ownership_owner_type import OwnershipOwnerType

        return {
            "action": (OwnershipFeedbackAction,),
            "checksum": (str,),
            "new_status": (OwnershipInferenceStatus,),
            "owner_type": (OwnershipOwnerType,),
            "previous_status": (OwnershipInferenceStatus,),
            "primary_contact_ref": (str, none_type),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "action": "action",
        "checksum": "checksum",
        "new_status": "new_status",
        "owner_type": "owner_type",
        "previous_status": "previous_status",
        "primary_contact_ref": "primary_contact_ref",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        action: OwnershipFeedbackAction,
        checksum: str,
        new_status: OwnershipInferenceStatus,
        owner_type: OwnershipOwnerType,
        previous_status: OwnershipInferenceStatus,
        updated_at: datetime,
        primary_contact_ref: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of an ownership feedback result.

        :param action: The feedback action to apply to an inference.
        :type action: OwnershipFeedbackAction

        :param checksum: The checksum of the inference after the feedback was applied.
        :type checksum: str

        :param new_status: The lifecycle status of an ownership inference.
        :type new_status: OwnershipInferenceStatus

        :param owner_type: The owner type for an ownership inference.
        :type owner_type: OwnershipOwnerType

        :param previous_status: The lifecycle status of an ownership inference.
        :type previous_status: OwnershipInferenceStatus

        :param primary_contact_ref: The primary contact reference for the inferred owner after the feedback was applied, formatted as ``ref:handle/<owner_handle>``.
        :type primary_contact_ref: str, none_type, optional

        :param updated_at: The time when the inference was updated by the feedback.
        :type updated_at: datetime
        """
        if primary_contact_ref is not unset:
            kwargs["primary_contact_ref"] = primary_contact_ref
        super().__init__(kwargs)

        self_.action = action
        self_.checksum = checksum
        self_.new_status = new_status
        self_.owner_type = owner_type
        self_.previous_status = previous_status
        self_.updated_at = updated_at
