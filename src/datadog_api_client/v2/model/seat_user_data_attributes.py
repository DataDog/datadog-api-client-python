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


class SeatUserDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assigned_at": (str,),
            "email": (str,),
            "name": (str,),
        }

    attribute_map = {
        "assigned_at": "assigned_at",
        "email": "email",
        "name": "name",
    }

    def __init__(
        self_,
        assigned_at: Union[str, UnsetType] = unset,
        email: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param assigned_at:
        :type assigned_at: str, optional

        :param email:
        :type email: str, optional

        :param name:
        :type name: str, optional
        """
        if assigned_at is not unset:
            kwargs["assigned_at"] = assigned_at
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
