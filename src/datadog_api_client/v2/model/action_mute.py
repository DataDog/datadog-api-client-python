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
    from datadog_api_client.v2.model.mute_reason import MuteReason


class ActionMute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mute_reason import MuteReason

        return {
            "expire_at": (int,),
            "reason": (MuteReason,),
            "reason_description": (str,),
        }

    attribute_map = {
        "expire_at": "expire_at",
        "reason": "reason",
        "reason_description": "reason_description",
    }

    def __init__(
        self_,
        reason: MuteReason,
        expire_at: Union[int, UnsetType] = unset,
        reason_description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Action of the mute rule

        :param expire_at: End date of the mute rule (null means mute forever)
        :type expire_at: int, optional

        :param reason: Reason for muting a vulnerability
        :type reason: MuteReason

        :param reason_description: Free text to add a reason description.
        :type reason_description: str, optional
        """
        if expire_at is not unset:
            kwargs["expire_at"] = expire_at
        if reason_description is not unset:
            kwargs["reason_description"] = reason_description
        super().__init__(kwargs)

        self_.reason = reason
