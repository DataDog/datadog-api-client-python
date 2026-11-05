# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class SecurityAgentInvestigationMitigationAction(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "applied": (bool,),
            "applied_at": (datetime,),
            "applied_by": (str,),
            "fqn": (str,),
            "id": (str,),
            "name": (str,),
            "resource": (str,),
            "source": (str,),
            "source_connected": (bool,),
            "target": (str,),
        }

    attribute_map = {
        "applied": "applied",
        "applied_at": "applied_at",
        "applied_by": "applied_by",
        "fqn": "fqn",
        "id": "id",
        "name": "name",
        "resource": "resource",
        "source": "source",
        "source_connected": "source_connected",
        "target": "target",
    }

    def __init__(
        self_,
        applied: bool,
        id: str,
        source: str,
        source_connected: bool,
        applied_at: Union[datetime, UnsetType] = unset,
        applied_by: Union[str, UnsetType] = unset,
        fqn: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        resource: Union[str, UnsetType] = unset,
        target: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An action that applies a mitigation.

        :param applied: Whether the action has run.
        :type applied: bool

        :param applied_at: When the action ran.
        :type applied_at: datetime, optional

        :param applied_by: Who ran the action.
        :type applied_by: str, optional

        :param fqn: ID of the action in the Action Catalog.
        :type fqn: str, optional

        :param id: ID of the action.
        :type id: str

        :param name: Name of the action in the Action Catalog.
        :type name: str, optional

        :param resource: The resource the action changes.
        :type resource: str, optional

        :param source: Integration that runs the action, such as ``dd`` , ``aws`` , or ``okta``.
        :type source: str

        :param source_connected: Whether the organization has a connection that can run the action.
        :type source_connected: bool

        :param target: What the action targets.
        :type target: str, optional
        """
        if applied_at is not unset:
            kwargs["applied_at"] = applied_at
        if applied_by is not unset:
            kwargs["applied_by"] = applied_by
        if fqn is not unset:
            kwargs["fqn"] = fqn
        if name is not unset:
            kwargs["name"] = name
        if resource is not unset:
            kwargs["resource"] = resource
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.applied = applied
        self_.id = id
        self_.source = source
        self_.source_connected = source_connected
