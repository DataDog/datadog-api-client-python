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
    from datadog_api_client.v2.model.fleet_access_scope_features import FleetAccessScopeFeatures


class FleetAccessScopeAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_access_scope_features import FleetAccessScopeFeatures

        return {
            "description": (str,),
            "features": (FleetAccessScopeFeatures,),
            "query": (str,),
        }

    attribute_map = {
        "description": "description",
        "features": "features",
        "query": "query",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        features: Union[FleetAccessScopeFeatures, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Mutable fleet access scope attributes. PUT replaces all mutable attributes; omitted strings become empty and omitted feature flags become false.

        :param description: Human-readable description of the access scope. Omission clears the description on update.
        :type description: str, optional

        :param features: Fleet actions authorized on agents matching the access scope query.
        :type features: FleetAccessScopeFeatures, optional

        :param query: Agent query selecting hosts covered by the scope. An empty query matches all hosts. Omission clears the query on update.
        :type query: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if features is not unset:
            kwargs["features"] = features
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)
