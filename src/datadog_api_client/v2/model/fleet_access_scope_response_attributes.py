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


class FleetAccessScopeResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_access_scope_features import FleetAccessScopeFeatures

        return {
            "created_at": (str,),
            "creator": (str,),
            "description": (str,),
            "features": (FleetAccessScopeFeatures,),
            "query": (str,),
            "updated_at": (str,),
            "updater": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "creator": "creator",
        "description": "description",
        "features": "features",
        "query": "query",
        "updated_at": "updated_at",
        "updater": "updater",
    }
    read_only_vars = {
        "created_at",
        "creator",
        "updated_at",
        "updater",
    }

    def __init__(
        self_,
        created_at: Union[str, UnsetType] = unset,
        creator: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        features: Union[FleetAccessScopeFeatures, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        updated_at: Union[str, UnsetType] = unset,
        updater: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Fleet access scope attributes and audit information.

        :param created_at: RFC3339 timestamp when the scope was created.
        :type created_at: str, optional

        :param creator: Handle of the user who created the scope.
        :type creator: str, optional

        :param description: Human-readable description of the access scope. Omission clears the description on update.
        :type description: str, optional

        :param features: Fleet actions authorized on agents matching the access scope query.
        :type features: FleetAccessScopeFeatures, optional

        :param query: Agent query selecting hosts covered by the scope. An empty query matches all hosts. Omission clears the query on update.
        :type query: str, optional

        :param updated_at: RFC3339 timestamp when the scope was last updated.
        :type updated_at: str, optional

        :param updater: Handle of the user who last updated the scope.
        :type updater: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if creator is not unset:
            kwargs["creator"] = creator
        if description is not unset:
            kwargs["description"] = description
        if features is not unset:
            kwargs["features"] = features
        if query is not unset:
            kwargs["query"] = query
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updater is not unset:
            kwargs["updater"] = updater
        super().__init__(kwargs)
