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


class ProductAnalyticsJoinKeys(ModelNormal):
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

    def __init__(
        self_, primary: Union[str, UnsetType] = unset, secondary: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Identity join keys used to stitch events belonging to the same user or session.

        :param primary: Primary identity join key. Defaults to ``@session.id``.
        :type primary: str, optional

        :param secondary: Additional identity join keys.
        :type secondary: [str], optional
        """
        if primary is not unset:
            kwargs["primary"] = primary
        if secondary is not unset:
            kwargs["secondary"] = secondary
        super().__init__(kwargs)
