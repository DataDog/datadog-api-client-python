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


class ContainerGroupRelationshipsLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "related": (str,),
        }

    attribute_map = {
        "related": "related",
    }

    def __init__(self_, related: Union[str, UnsetType] = unset, **kwargs):
        """
        Links attributes.

        :param related: Link to related containers.
        :type related: str, optional
        """
        if related is not unset:
            kwargs["related"] = related
        super().__init__(kwargs)
