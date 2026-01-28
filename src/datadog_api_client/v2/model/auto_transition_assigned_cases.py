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


class AutoTransitionAssignedCases(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "auto_transition_assigned_cases_on_self_assigned": (bool,),
        }

    attribute_map = {
        "auto_transition_assigned_cases_on_self_assigned": "auto_transition_assigned_cases_on_self_assigned",
    }

    def __init__(self_, auto_transition_assigned_cases_on_self_assigned: Union[bool, UnsetType] = unset, **kwargs):
        """
        Auto-transition assigned cases settings

        :param auto_transition_assigned_cases_on_self_assigned: Whether to auto-transition cases when self-assigned
        :type auto_transition_assigned_cases_on_self_assigned: bool, optional
        """
        if auto_transition_assigned_cases_on_self_assigned is not unset:
            kwargs["auto_transition_assigned_cases_on_self_assigned"] = auto_transition_assigned_cases_on_self_assigned
        super().__init__(kwargs)
