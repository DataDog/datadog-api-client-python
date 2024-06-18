# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
    unset,
    UnsetType,
    UUID,
)



class ListAPIsResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
        }
    attribute_map = {
        "name": "name",
    }

    def __init__(self_, name: Union[str, UnsetType]=unset, **kwargs):
        """
        Attributes for ``ListAPIsResponseData``.

        :param name: API name.
        :type name: str, optional
        """
        if name is not unset:
             kwargs["name"] = name
        super().__init__(kwargs)


