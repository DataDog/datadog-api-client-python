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


class GuidedTableColumnFunction(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "args": ([str, float, bool],),
            "name": (str,),
        }

    attribute_map = {
        "args": "args",
        "name": "name",
    }

    def __init__(self_, name: str, args: Union[List[Union[str, float, bool]], UnsetType] = unset, **kwargs):
        """
        A function to apply when computing a column's value.

        :param args: Arguments passed to the function in order.
        :type args: [str, float, bool], optional

        :param name: Function name (e.g. ``clamp_min`` , ``abs`` , ``round`` ). Not restricted to a fixed set.
        :type name: str
        """
        if args is not unset:
            kwargs["args"] = args
        super().__init__(kwargs)

        self_.name = name
