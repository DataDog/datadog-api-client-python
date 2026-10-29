# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.on_call_page_live_call_outcome import OnCallPageLiveCallOutcome


class OnCallPageLiveCallOver(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_page_live_call_outcome import OnCallPageLiveCallOutcome

        return {
            "outcome": (OnCallPageLiveCallOutcome,),
            "support_hours_start_at": (datetime,),
        }

    attribute_map = {
        "outcome": "outcome",
        "support_hours_start_at": "support_hours_start_at",
    }

    def __init__(
        self_,
        outcome: Union[OnCallPageLiveCallOutcome, UnsetType] = unset,
        support_hours_start_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about a live call that has ended.

        :param outcome: The outcome of a live call that has ended.
        :type outcome: OnCallPageLiveCallOutcome, optional

        :param support_hours_start_at: When support hours start, if the call was placed outside support hours.
        :type support_hours_start_at: datetime, optional
        """
        if outcome is not unset:
            kwargs["outcome"] = outcome
        if support_hours_start_at is not unset:
            kwargs["support_hours_start_at"] = support_hours_start_at
        super().__init__(kwargs)
