# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ownership_feedback_action import OwnershipFeedbackAction


class OwnershipFeedbackRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_feedback_action import OwnershipFeedbackAction

        return {
            "action": (OwnershipFeedbackAction,),
            "actor_handle": (str,),
            "actor_type": (str,),
            "corrected_owner_handle": (str, none_type),
            "corrected_owner_type": (str, none_type),
            "inference_checksum": (str,),
            "reason": (str, none_type),
        }

    attribute_map = {
        "action": "action",
        "actor_handle": "actor_handle",
        "actor_type": "actor_type",
        "corrected_owner_handle": "corrected_owner_handle",
        "corrected_owner_type": "corrected_owner_type",
        "inference_checksum": "inference_checksum",
        "reason": "reason",
    }

    def __init__(
        self_,
        action: OwnershipFeedbackAction,
        actor_handle: str,
        actor_type: str,
        inference_checksum: str,
        corrected_owner_handle: Union[str, none_type, UnsetType] = unset,
        corrected_owner_type: Union[str, none_type, UnsetType] = unset,
        reason: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of an ownership feedback request.

        :param action: The feedback action to apply to an inference.
        :type action: OwnershipFeedbackAction

        :param actor_handle: The handle of the actor submitting the feedback.
        :type actor_handle: str

        :param actor_type: The type of actor submitting the feedback, for example ``user`` or ``service``.
        :type actor_type: str

        :param corrected_owner_handle: The corrected owner handle. Required when ``action`` is ``correct``.
        :type corrected_owner_handle: str, none_type, optional

        :param corrected_owner_type: The corrected owner type. Required when ``action`` is ``correct``.
        :type corrected_owner_type: str, none_type, optional

        :param inference_checksum: The checksum of the inference being acted upon. Must match the current inference checksum or the request returns a conflict.
        :type inference_checksum: str

        :param reason: An optional free-form reason explaining the feedback.
        :type reason: str, none_type, optional
        """
        if corrected_owner_handle is not unset:
            kwargs["corrected_owner_handle"] = corrected_owner_handle
        if corrected_owner_type is not unset:
            kwargs["corrected_owner_type"] = corrected_owner_type
        if reason is not unset:
            kwargs["reason"] = reason
        super().__init__(kwargs)

        self_.action = action
        self_.actor_handle = actor_handle
        self_.actor_type = actor_type
        self_.inference_checksum = inference_checksum
