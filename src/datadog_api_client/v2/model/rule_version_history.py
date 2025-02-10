# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rule_versions import RuleVersions


class RuleVersionHistory(ModelNormal):
    validations = {
        "count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_versions import RuleVersions

        return {
            "count": (int,),
            "data": ({str: (RuleVersions,)},),
        }

    attribute_map = {
        "count": "count",
        "data": "data",
    }

    def __init__(
        self_, count: Union[int, UnsetType] = unset, data: Union[Dict[str, RuleVersions], UnsetType] = unset, **kwargs
    ):
        """
        Response object containing the version history of a rule.

        :param count: The number of rule versions.
        :type count: int, optional

        :param data: The ``RuleVersionHistory`` ``data``.
        :type data: {str: (RuleVersions,)}, optional
        """
        if count is not unset:
            kwargs["count"] = count
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
