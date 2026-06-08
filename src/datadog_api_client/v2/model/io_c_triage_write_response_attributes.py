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


class IoCTriageWriteResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "indicator": (str,),
            "triage_state": (str,),
            "triaged_at": (datetime,),
            "triaged_by": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "indicator": "indicator",
        "triage_state": "triage_state",
        "triaged_at": "triaged_at",
        "triaged_by": "triaged_by",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        indicator: Union[str, UnsetType] = unset,
        triage_state: Union[str, UnsetType] = unset,
        triaged_at: Union[datetime, UnsetType] = unset,
        triaged_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a created or updated triage state.

        :param created_at: Timestamp when the triage record was created.
        :type created_at: datetime, optional

        :param indicator: The indicator value that was triaged.
        :type indicator: str, optional

        :param triage_state: The triage state that was set: not_reviewed or reviewed.
        :type triage_state: str, optional

        :param triaged_at: Timestamp when the triage state was set.
        :type triaged_at: datetime, optional

        :param triaged_by: UUID of the user who set the triage state.
        :type triaged_by: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if indicator is not unset:
            kwargs["indicator"] = indicator
        if triage_state is not unset:
            kwargs["triage_state"] = triage_state
        if triaged_at is not unset:
            kwargs["triaged_at"] = triaged_at
        if triaged_by is not unset:
            kwargs["triaged_by"] = triaged_by
        super().__init__(kwargs)
