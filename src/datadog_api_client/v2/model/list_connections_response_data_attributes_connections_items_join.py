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


class ListConnectionsResponseDataAttributesConnectionsItemsJoin(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attribute": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attribute": "attribute",
        "type": "type",
    }

    def __init__(self_, attribute: Union[str, UnsetType] = unset, type: Union[str, UnsetType] = unset, **kwargs):
        """


        :param attribute:
        :type attribute: str, optional

        :param type:
        :type type: str, optional
        """
        if attribute is not unset:
            kwargs["attribute"] = attribute
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
