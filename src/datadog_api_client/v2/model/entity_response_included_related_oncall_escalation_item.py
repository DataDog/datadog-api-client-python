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


class EntityResponseIncludedRelatedOncallEscalationItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "escalation_level": (int,),
            "name": (str,),
        }

    attribute_map = {
        "email": "email",
        "escalation_level": "escalationLevel",
        "name": "name",
    }

    def __init__(
        self_,
        email: Union[str, UnsetType] = unset,
        escalation_level: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Oncall escalation

        :param email: Oncall email.
        :type email: str, optional

        :param escalation_level: Oncall level.
        :type escalation_level: int, optional

        :param name: Oncall name.
        :type name: str, optional
        """
        if email is not unset:
            kwargs["email"] = email
        if escalation_level is not unset:
            kwargs["escalation_level"] = escalation_level
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
