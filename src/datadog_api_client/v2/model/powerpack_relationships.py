# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.creator import Creator


class PowerpackRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.creator import Creator

        return {
            "author": (Creator,),
        }

    attribute_map = {
        "author": "author",
    }

    def __init__(self_, author: Union[Creator, UnsetType] = unset, **kwargs):
        """
        Powerpack relationship object.

        :param author: Creator of the object.
        :type author: Creator, optional
        """
        if author is not unset:
            kwargs["author"] = author
        super().__init__(kwargs)
