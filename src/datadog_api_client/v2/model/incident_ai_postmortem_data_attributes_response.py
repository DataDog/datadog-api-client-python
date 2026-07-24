# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IncidentAIPostmortemDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "action_items": (str,),
            "customer_impact": (str,),
            "executive_summary": (str,),
            "key_timeline": (str,),
            "lessons_learned": (str,),
            "system_overview": (str,),
        }

    attribute_map = {
        "action_items": "action_items",
        "customer_impact": "customer_impact",
        "executive_summary": "executive_summary",
        "key_timeline": "key_timeline",
        "lessons_learned": "lessons_learned",
        "system_overview": "system_overview",
    }

    def __init__(
        self_,
        action_items: Union[str, UnsetType] = unset,
        customer_impact: Union[str, UnsetType] = unset,
        executive_summary: Union[str, UnsetType] = unset,
        key_timeline: Union[str, UnsetType] = unset,
        lessons_learned: Union[str, UnsetType] = unset,
        system_overview: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an AI-generated incident postmortem.

        :param action_items: Action items to prevent recurrence.
        :type action_items: str, optional

        :param customer_impact: The impact of the incident on customers.
        :type customer_impact: str, optional

        :param executive_summary: An executive summary of the incident.
        :type executive_summary: str, optional

        :param key_timeline: Key timeline events during the incident.
        :type key_timeline: str, optional

        :param lessons_learned: Lessons learned from the incident.
        :type lessons_learned: str, optional

        :param system_overview: An overview of the affected systems.
        :type system_overview: str, optional
        """
        if action_items is not unset:
            kwargs["action_items"] = action_items
        if customer_impact is not unset:
            kwargs["customer_impact"] = customer_impact
        if executive_summary is not unset:
            kwargs["executive_summary"] = executive_summary
        if key_timeline is not unset:
            kwargs["key_timeline"] = key_timeline
        if lessons_learned is not unset:
            kwargs["lessons_learned"] = lessons_learned
        if system_overview is not unset:
            kwargs["system_overview"] = system_overview
        super().__init__(kwargs)
