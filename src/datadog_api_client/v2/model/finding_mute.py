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
    from datadog_api_client.v2.model.finding_mute_reason import FindingMuteReason


class FindingMute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding_mute_reason import FindingMuteReason

        return {
            "description": (str,),
            "expiration_date": (int,),
            "muted": (bool,),
            "reason": (FindingMuteReason,),
            "start_date": (int,),
            "uuid": (str,),
        }

    attribute_map = {
        "description": "description",
        "expiration_date": "expiration_date",
        "muted": "muted",
        "reason": "reason",
        "start_date": "start_date",
        "uuid": "uuid",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        expiration_date: Union[int, UnsetType] = unset,
        muted: Union[bool, UnsetType] = unset,
        reason: Union[FindingMuteReason, UnsetType] = unset,
        start_date: Union[int, UnsetType] = unset,
        uuid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about the mute status of this finding.

        :param description: Additional information about the reason why this finding is muted or unmuted.
        :type description: str, optional

        :param expiration_date: The expiration date of the mute or unmute action (Unix ms).
        :type expiration_date: int, optional

        :param muted: Whether this finding is muted or unmuted.
        :type muted: bool, optional

        :param reason: The reason why this finding is muted or unmuted.
        :type reason: FindingMuteReason, optional

        :param start_date: The start of the mute period.
        :type start_date: int, optional

        :param uuid: The ID of the user who muted or unmuted this finding.
        :type uuid: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if expiration_date is not unset:
            kwargs["expiration_date"] = expiration_date
        if muted is not unset:
            kwargs["muted"] = muted
        if reason is not unset:
            kwargs["reason"] = reason
        if start_date is not unset:
            kwargs["start_date"] = start_date
        if uuid is not unset:
            kwargs["uuid"] = uuid
        super().__init__(kwargs)
