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


class ScaRequestDataAttributesFilesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "purl": (str,),
        }

    attribute_map = {
        "name": "name",
        "purl": "purl",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, purl: Union[str, UnsetType] = unset, **kwargs):
        """


        :param name:
        :type name: str, optional

        :param purl:
        :type purl: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if purl is not unset:
            kwargs["purl"] = purl
        super().__init__(kwargs)
