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


class ActionInbox(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "reason_description": (str,),
        }

    attribute_map = {
        "reason_description": "reason_description",
    }

    def __init__(self_, reason_description: Union[str, UnsetType] = unset, **kwargs):
        """
        Action of the inbox rule

        :param reason_description: Free text to add a reason description.
        :type reason_description: str, optional
        """
        if reason_description is not unset:
            kwargs["reason_description"] = reason_description
        super().__init__(kwargs)
