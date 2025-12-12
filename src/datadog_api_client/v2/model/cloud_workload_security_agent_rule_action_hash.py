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


class CloudWorkloadSecurityAgentRuleActionHash(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "field": (str,),
        }

    attribute_map = {
        "field": "field",
    }

    def __init__(self_, field: Union[str, UnsetType] = unset, **kwargs):
        """
        Hash file specified by the field attribute

        :param field: The field of the hash action
        :type field: str, optional
        """
        if field is not unset:
            kwargs["field"] = field
        super().__init__(kwargs)
