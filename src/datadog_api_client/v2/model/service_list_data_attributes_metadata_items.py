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


class ServiceListDataAttributesMetadataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_traced": (bool,),
            "is_usm": (bool,),
        }

    attribute_map = {
        "is_traced": "isTraced",
        "is_usm": "isUsm",
    }

    def __init__(self_, is_traced: Union[bool, UnsetType] = unset, is_usm: Union[bool, UnsetType] = unset, **kwargs):
        """


        :param is_traced:
        :type is_traced: bool, optional

        :param is_usm:
        :type is_usm: bool, optional
        """
        if is_traced is not unset:
            kwargs["is_traced"] = is_traced
        if is_usm is not unset:
            kwargs["is_usm"] = is_usm
        super().__init__(kwargs)
