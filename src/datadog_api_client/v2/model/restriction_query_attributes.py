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


class RestrictionQueryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "last_modifier_email": (str,),
            "last_modifier_name": (str,),
            "modified_at": (datetime,),
            "restriction_query": (str,),
            "role_count": (int,),
            "user_count": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "last_modifier_email": "last_modifier_email",
        "last_modifier_name": "last_modifier_name",
        "modified_at": "modified_at",
        "restriction_query": "restriction_query",
        "role_count": "role_count",
        "user_count": "user_count",
    }
    read_only_vars = {
        "created_at",
        "last_modifier_email",
        "last_modifier_name",
        "modified_at",
        "role_count",
        "user_count",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        last_modifier_email: Union[str, UnsetType] = unset,
        last_modifier_name: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        restriction_query: Union[str, UnsetType] = unset,
        role_count: Union[int, UnsetType] = unset,
        user_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the restriction query.

        :param created_at: Creation time of the restriction query.
        :type created_at: datetime, optional

        :param last_modifier_email: Email of the user who last modified this restriction query.
        :type last_modifier_email: str, optional

        :param last_modifier_name: Name of the user who last modified this restriction query.
        :type last_modifier_name: str, optional

        :param modified_at: Time of last restriction query modification.
        :type modified_at: datetime, optional

        :param restriction_query: The query that defines the restriction. Only the content matching the query can be returned.
        :type restriction_query: str, optional

        :param role_count: Number of roles associated with this restriction query.
        :type role_count: int, optional

        :param user_count: Number of users associated with this restriction query.
        :type user_count: int, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if last_modifier_email is not unset:
            kwargs["last_modifier_email"] = last_modifier_email
        if last_modifier_name is not unset:
            kwargs["last_modifier_name"] = last_modifier_name
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if restriction_query is not unset:
            kwargs["restriction_query"] = restriction_query
        if role_count is not unset:
            kwargs["role_count"] = role_count
        if user_count is not unset:
            kwargs["user_count"] = user_count
        super().__init__(kwargs)
