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


class InboxRuleAction(ModelNormal):
    validations = {
        "description": {
            "max_length": 20000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
        }

    attribute_map = {
        "description": "description",
    }

    def __init__(self_, description: Union[str, UnsetType] = unset, **kwargs):
        """
        The action to take when the inbox rule matches a finding.

        :param description: An optional description providing more context for the rule.
        :type description: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)
