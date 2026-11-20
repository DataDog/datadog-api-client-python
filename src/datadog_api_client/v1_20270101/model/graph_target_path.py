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
    from datadog_api_client.v1_20270101.model.graph_target_path_type import GraphTargetPathType


class GraphTargetPath(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.graph_target_path_type import GraphTargetPathType

        return {
            "end": (str,),
            "start": (str,),
            "type": (GraphTargetPathType,),
        }

    attribute_map = {
        "end": "end",
        "start": "start",
        "type": "type",
    }

    def __init__(self_, start: str, type: GraphTargetPathType, end: Union[str, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param end: Test-only generated schema for the dashboard versioning proof of concept.
        :type end: str, optional

        :param start: Test-only generated schema for the dashboard versioning proof of concept.
        :type start: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: GraphTargetPathType
        """
        if end is not unset:
            kwargs["end"] = end
        super().__init__(kwargs)

        self_.start = start
        self_.type = type
