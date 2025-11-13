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


class TeamConnectionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "managed_by": (str,),
            "source": (str,),
        }

    attribute_map = {
        "managed_by": "managed_by",
        "source": "source",
    }

    def __init__(self_, managed_by: Union[str, UnsetType] = unset, source: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes of the team connection.

        :param managed_by: The entity that manages this team connection.
        :type managed_by: str, optional

        :param source: The name of the external source.
        :type source: str, optional
        """
        if managed_by is not unset:
            kwargs["managed_by"] = managed_by
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)
