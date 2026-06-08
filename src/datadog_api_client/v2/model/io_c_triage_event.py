# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class IoCTriageEvent(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "triage_state": (str,),
            "triaged_at": (datetime,),
            "triaged_by": (str,),
        }

    attribute_map = {
        "triage_state": "triage_state",
        "triaged_at": "triaged_at",
        "triaged_by": "triaged_by",
    }

    def __init__(
        self_,
        triage_state: Union[str, UnsetType] = unset,
        triaged_at: Union[datetime, UnsetType] = unset,
        triaged_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single entry in an indicator's triage history timeline.

        :param triage_state: Triage state set by this action: not_reviewed or reviewed.
        :type triage_state: str, optional

        :param triaged_at: Timestamp when this triage action occurred.
        :type triaged_at: datetime, optional

        :param triaged_by: UUID of the user who performed this triage action.
        :type triaged_by: str, optional
        """
        if triage_state is not unset:
            kwargs["triage_state"] = triage_state
        if triaged_at is not unset:
            kwargs["triaged_at"] = triaged_at
        if triaged_by is not unset:
            kwargs["triaged_by"] = triaged_by
        super().__init__(kwargs)
