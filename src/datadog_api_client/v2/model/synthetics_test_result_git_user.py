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


class SyntheticsTestResultGitUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "date": (str,),
            "email": (str,),
            "name": (str,),
        }

    attribute_map = {
        "date": "date",
        "email": "email",
        "name": "name",
    }

    def __init__(
        self_,
        date: Union[str, UnsetType] = unset,
        email: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A Git user (author or committer).

        :param date: Timestamp of the commit action for this user.
        :type date: str, optional

        :param email: Email address of the Git user.
        :type email: str, optional

        :param name: Name of the Git user.
        :type name: str, optional
        """
        if date is not unset:
            kwargs["date"] = date
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
