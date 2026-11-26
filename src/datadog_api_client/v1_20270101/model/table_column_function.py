# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.dashboard_inline_schema47 import DashboardInlineSchema47


class TableColumnFunction(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dashboard_inline_schema47 import DashboardInlineSchema47

        return {
            "args": ([DashboardInlineSchema47],),
            "name": (str,),
        }

    attribute_map = {
        "args": "args",
        "name": "name",
    }

    def __init__(
        self_,
        name: str,
        args: Union[List[Union[DashboardInlineSchema47, str, float, bool]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param args: Test-only generated schema for the dashboard versioning proof of concept.
        :type args: [DashboardInlineSchema47], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        if args is not unset:
            kwargs["args"] = args
        super().__init__(kwargs)

        self_.name = name
