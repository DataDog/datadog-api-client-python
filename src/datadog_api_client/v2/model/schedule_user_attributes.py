# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_attributes_status import UserAttributesStatus


class ScheduleUserAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_attributes_status import UserAttributesStatus

        return {
            "email": (str,),
            "name": (str,),
            "status": (UserAttributesStatus,),
        }

    attribute_map = {
        "email": "email",
        "name": "name",
        "status": "status",
    }

    def __init__(
        self_,
        email: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        status: Union[UserAttributesStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Provides basic user information for a schedule, including a name and email address.

        :param email: The user's email address.
        :type email: str, optional

        :param name: The user's name.
        :type name: str, optional

        :param status: The user's status.
        :type status: UserAttributesStatus, optional
        """
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
