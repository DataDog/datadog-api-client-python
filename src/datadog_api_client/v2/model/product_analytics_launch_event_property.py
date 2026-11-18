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


class ProductAnalyticsLaunchEventProperty(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "required": (bool,),
        }

    attribute_map = {
        "id": "id",
        "required": "required",
    }

    def __init__(self_, id: str, required: Union[bool, UnsetType] = unset, **kwargs):
        """
        A reference from an event to a property of the tracking plan.

        :param id: ID of a property in the tracking plan ``properties``.
        :type id: str

        :param required: Whether the event must always include the property.
        :type required: bool, optional
        """
        if required is not unset:
            kwargs["required"] = required
        super().__init__(kwargs)

        self_.id = id
