# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class EnvironmentAttributes(ModelNormal):
    validations = {
        "queries": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "description": (str, none_type),
            "is_production": (bool,),
            "key": (str,),
            "name": (str,),
            "queries": ([str],),
            "require_feature_flag_approval": (bool,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "is_production": "is_production",
        "key": "key",
        "name": "name",
        "queries": "queries",
        "require_feature_flag_approval": "require_feature_flag_approval",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        name: str,
        created_at: Union[datetime, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        is_production: Union[bool, UnsetType] = unset,
        key: Union[str, UnsetType] = unset,
        queries: Union[List[str], UnsetType] = unset,
        require_feature_flag_approval: Union[bool, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an environment.

        :param created_at: The timestamp when the environment was created.
        :type created_at: datetime, optional

        :param description: The description of the environment.
        :type description: str, none_type, optional

        :param is_production: Indicates whether this is a production environment.
        :type is_production: bool, optional

        :param key: The unique key of the environment.
        :type key: str, optional

        :param name: The name of the environment.
        :type name: str

        :param queries: List of queries to define the environment scope.
        :type queries: [str], optional

        :param require_feature_flag_approval: Indicates whether feature flag changes require approval in this environment.
        :type require_feature_flag_approval: bool, optional

        :param updated_at: The timestamp when the environment was last updated.
        :type updated_at: datetime, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if description is not unset:
            kwargs["description"] = description
        if is_production is not unset:
            kwargs["is_production"] = is_production
        if key is not unset:
            kwargs["key"] = key
        if queries is not unset:
            kwargs["queries"] = queries
        if require_feature_flag_approval is not unset:
            kwargs["require_feature_flag_approval"] = require_feature_flag_approval
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.name = name
