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


class SeatUserDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assigned_at": (datetime,),
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
        assigned_at: Union[datetime, UnsetType] = unset,
        email: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param assigned_at: The date and time the seat was assigned.
        :type assigned_at: datetime, optional

        :param email: The email of the user.
        :type email: str, optional

        :param name: The name of the user.
        :type name: str, optional
        """
        if assigned_at is not unset:
            kwargs["assigned_at"] = assigned_at
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
