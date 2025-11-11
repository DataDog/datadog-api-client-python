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
            "modified_at": (datetime,),
            "restriction_query": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "modified_at": "modified_at",
        "restriction_query": "restriction_query",
    }
    read_only_vars = {
        "created_at",
        "modified_at",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        restriction_query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the restriction query.

        :param created_at: Creation time of the restriction query.
        :type created_at: datetime, optional

        :param modified_at: Time of last restriction query modification.
        :type modified_at: datetime, optional

        :param restriction_query: The query that defines the restriction. Only the content matching the query can be returned.
        :type restriction_query: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if restriction_query is not unset:
            kwargs["restriction_query"] = restriction_query
        super().__init__(kwargs)
