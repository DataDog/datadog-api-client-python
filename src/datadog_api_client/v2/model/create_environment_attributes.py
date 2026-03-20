# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CreateEnvironmentAttributes(ModelNormal):
    validations = {
        "queries": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "is_production": (bool,),
            "name": (str,),
            "queries": ([str],),
            "require_feature_flag_approval": (bool,),
        }

    attribute_map = {
        "is_production": "is_production",
        "name": "name",
        "queries": "queries",
        "require_feature_flag_approval": "require_feature_flag_approval",
    }

    def __init__(
        self_,
        name: str,
        queries: List[str],
        is_production: Union[bool, UnsetType] = unset,
        require_feature_flag_approval: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a new environment.

        :param is_production: Indicates whether this is a production environment.
        :type is_production: bool, optional

        :param name: The name of the environment.
        :type name: str

        :param queries: List of queries to define the environment scope.
        :type queries: [str]

        :param require_feature_flag_approval: Indicates whether feature flag changes require approval in this environment.
        :type require_feature_flag_approval: bool, optional
        """
        if is_production is not unset:
            kwargs["is_production"] = is_production
        if require_feature_flag_approval is not unset:
            kwargs["require_feature_flag_approval"] = require_feature_flag_approval
        super().__init__(kwargs)

        self_.name = name
        self_.queries = queries
