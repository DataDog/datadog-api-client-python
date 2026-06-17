# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class GovernanceBestPracticeDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "deep_link": (str,),
            "description": (str,),
            "detection_type": (str, none_type),
            "id": (str,),
            "impact": (str,),
            "impact_hint": (int,),
            "permissions": ([str],),
            "status": (str,),
            "summary": (str,),
            "title": (str,),
            "trigger_condition": (str,),
            "trigger_type": (str,),
        }

    attribute_map = {
        "category": "category",
        "deep_link": "deep_link",
        "description": "description",
        "detection_type": "detection_type",
        "id": "id",
        "impact": "impact",
        "impact_hint": "impact_hint",
        "permissions": "permissions",
        "status": "status",
        "summary": "summary",
        "title": "title",
        "trigger_condition": "trigger_condition",
        "trigger_type": "trigger_type",
    }

    def __init__(
        self_,
        category: str,
        deep_link: str,
        description: str,
        id: str,
        impact: str,
        impact_hint: int,
        permissions: List[str],
        status: str,
        summary: str,
        title: str,
        trigger_condition: str,
        trigger_type: str,
        detection_type: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The best practice associated with an insight. Populated with the first active best practice
        matched to the insight; ``null`` when no best practice is attached.

        :param category: The value driver the best practice is grouped under, such as ``access_governance`` ,
            ``security`` , ``compliance`` , or ``operational_hygiene``.
        :type category: str

        :param deep_link: A relative link to the configuration page where the best practice can be acted upon.
        :type deep_link: str

        :param description: The full rationale and guidance for the best practice.
        :type description: str

        :param detection_type: An optional association to a control's detection type. ``null`` when not associated with a control.
        :type detection_type: str, none_type, optional

        :param id: The unique identifier of the best practice.
        :type id: str

        :param impact: The expected impact of following the best practice.
        :type impact: str

        :param impact_hint: A priority hint for ordering best practices by expected impact. Lower values indicate
            higher priority.
        :type impact_hint: int

        :param permissions: The permissions required for the user to act on the best practice.
        :type permissions: [str]

        :param status: Whether the best practice is currently ``active`` or ``deprecated``.
        :type status: str

        :param summary: A one-line explanation of why this best practice matters.
        :type summary: str

        :param title: A short, human-readable name for the best practice.
        :type title: str

        :param trigger_condition: The condition that surfaces the best practice. For an ``insight`` trigger, the insight
            slug; for a ``static`` trigger, a descriptive condition key.
        :type trigger_condition: str

        :param trigger_type: How the best practice is surfaced. ``insight`` ties it to an insight; ``static`` surfaces it
            unless its condition is met.
        :type trigger_type: str
        """
        if detection_type is not unset:
            kwargs["detection_type"] = detection_type
        super().__init__(kwargs)

        self_.category = category
        self_.deep_link = deep_link
        self_.description = description
        self_.id = id
        self_.impact = impact
        self_.impact_hint = impact_hint
        self_.permissions = permissions
        self_.status = status
        self_.summary = summary
        self_.title = title
        self_.trigger_condition = trigger_condition
        self_.trigger_type = trigger_type
