# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class SeatUserDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assigned_at": (datetime, none_type),
            "email": (str, none_type),
            "name": (str, none_type),
        }

    attribute_map = {
        "assigned_at": "assigned_at",
        "email": "email",
        "name": "name",
    }

    def __init__(
        self_,
        assigned_at: Union[datetime, none_type, UnsetType] = unset,
        email: Union[str, none_type, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param assigned_at: The date and time the seat was assigned.
        :type assigned_at: datetime, none_type, optional

        :param email: The email of the user.
        :type email: str, none_type, optional

        :param name: The name of the user.
        :type name: str, none_type, optional
        """
        if assigned_at is not unset:
            kwargs["assigned_at"] = assigned_at
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
