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


class AiGatewayBudgetInstanceResetAttributes(ModelNormal):
    validations = {
        "instance_key": {
            "min_length": 1,
        },
        "reason": {
            "max_length": 1024,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "instance_key": (str,),
            "reason": (str,),
        }

    attribute_map = {
        "instance_key": "instance_key",
        "reason": "reason",
    }

    def __init__(self_, instance_key: str, reason: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes used to reset one budget instance's active-period spend.

        :param instance_key: Counter key of the instance to reset, as returned by the list budget instances endpoint.
        :type instance_key: str

        :param reason: Optional reason recorded with the spend reset.
        :type reason: str, optional
        """
        if reason is not unset:
            kwargs["reason"] = reason
        super().__init__(kwargs)

        self_.instance_key = instance_key
