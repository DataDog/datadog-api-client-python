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


class Entity(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "entity_kind": (str,),
            "entity_name": (str,),
            "entity_namespace": (str,),
            "entity_team": (str,),
        }

    attribute_map = {
        "entity_kind": "entity_kind",
        "entity_name": "entity_name",
        "entity_namespace": "entity_namespace",
        "entity_team": "entity_team",
    }

    def __init__(
        self_,
        entity_name: str,
        entity_kind: Union[str, UnsetType] = unset,
        entity_namespace: Union[str, UnsetType] = unset,
        entity_team: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An entity participating in the dependency upgrade workflow.

        :param entity_kind: The kind of the entity (for example, service or package).
        :type entity_kind: str, optional

        :param entity_name: The name of the entity.
        :type entity_name: str

        :param entity_namespace: The namespace of the entity.
        :type entity_namespace: str, optional

        :param entity_team: The team that owns the entity.
        :type entity_team: str, optional
        """
        if entity_kind is not unset:
            kwargs["entity_kind"] = entity_kind
        if entity_namespace is not unset:
            kwargs["entity_namespace"] = entity_namespace
        if entity_team is not unset:
            kwargs["entity_team"] = entity_team
        super().__init__(kwargs)

        self_.entity_name = entity_name
