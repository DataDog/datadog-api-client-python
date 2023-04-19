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


class FindingRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "name": (str,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
    }

    def __init__(self_, id: Union[str, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        The rule that triggered this finding.

        :param id: The ID of the rule that triggered this finding.
        :type id: str, optional

        :param name: The name of the rule that triggered this finding.
        :type name: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
