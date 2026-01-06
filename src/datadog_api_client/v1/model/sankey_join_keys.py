# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SankeyJoinKeys(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "primary": (str,),
            "secondary": ([str],),
        }

    attribute_map = {
        "primary": "primary",
        "secondary": "secondary",
    }

    def __init__(self_, primary: str, secondary: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Join keys.

        :param primary: Primary join key.
        :type primary: str

        :param secondary: Secondary join keys.
        :type secondary: [str], optional
        """
        if secondary is not unset:
            kwargs["secondary"] = secondary
        super().__init__(kwargs)

        self_.primary = primary
