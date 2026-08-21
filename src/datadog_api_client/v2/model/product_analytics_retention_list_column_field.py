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


class ProductAnalyticsRetentionListColumnField(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "path": (str,),
        }

    attribute_map = {
        "path": "path",
    }

    def __init__(self_, path: Union[str, UnsetType] = unset, **kwargs):
        """
        The attribute selected for a column.

        :param path: Attribute path of the column.
        :type path: str, optional
        """
        if path is not unset:
            kwargs["path"] = path
        super().__init__(kwargs)
