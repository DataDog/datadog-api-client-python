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


class UsageAttributionTypesAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "values": ([str],),
        }

    attribute_map = {
        "values": "values",
    }

    def __init__(self_, values: Union[List[str], UnsetType] = unset, **kwargs):
        """
        List of usage attribution types.

        :param values: List of usage attribution types.
        :type values: [str], optional
        """
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
