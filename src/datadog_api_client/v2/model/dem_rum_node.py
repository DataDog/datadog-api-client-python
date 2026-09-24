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


class DemRumNode(ModelNormal):
    validations = {
        "app_id": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "app_id": (str,),
            "id": (str,),
            "query": (str,),
        }

    attribute_map = {
        "app_id": "app_id",
        "id": "id",
        "query": "query",
    }

    def __init__(self_, app_id: str, query: str, id: Union[str, UnsetType] = unset, **kwargs):
        """
        A RUM node within a journey step.

        :param app_id: The RUM application ID whose events this node query matches. This value is required for every node when creating or updating a DEM feature or journey, including variants, and is used to discover the resource in application-scoped searches. Use ``GET /api/v2/rum/applications`` to find RUM application IDs.
        :type app_id: str

        :param id: The ID of the RUM node element.
        :type id: str, optional

        :param query: The RUM query for matching this node.
        :type query: str
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.app_id = app_id
        self_.query = query
