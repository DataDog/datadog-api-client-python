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


class BulkMuteFindingsRequestProperties(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding_mute_reason import FindingMuteReason

        return {
            "description": (str,),
            "expiration_date": (int,),
            "muted": (bool,),
            "reason": (FindingMuteReason,),
        }

    attribute_map = {
        "description": "description",
        "expiration_date": "expiration_date",
        "muted": "muted",
        "reason": "reason",
    }

    def __init__(
        self_,
        muted: bool,
        reason: FindingMuteReason,
        description: Union[str, UnsetType] = unset,
        expiration_date: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the new mute properties of the findings.

        :param description: Additional information about the reason why those findings are muted or unmuted. This field has a maximum limit of 280 characters.
        :type description: str, optional

        :param expiration_date: The expiration date of the mute or unmute action (Unix ms). It must be set to a value greater than the current timestamp.
            If this field is not provided, the finding will be muted or unmuted indefinitely, which is equivalent to setting the expiration date to 9999999999999.
        :type expiration_date: int, optional

        :param muted: Whether those findings should be muted or unmuted.
        :type muted: bool

        :param reason: The reason why this finding is muted or unmuted.
        :type reason: FindingMuteReason
        """
        if description is not unset:
            kwargs["description"] = description
        if expiration_date is not unset:
            kwargs["expiration_date"] = expiration_date
        super().__init__(kwargs)

        self_.muted = muted
        self_.reason = reason
