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


class RelationEntity(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "kind": (str,),
            "name": (str,),
            "namespace": (str,),
        }

    attribute_map = {
        "kind": "kind",
        "name": "name",
        "namespace": "namespace",
    }

    def __init__(
        self_,
        kind: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        namespace: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relation entity reference.

        :param kind: Entity kind.
        :type kind: str, optional

        :param name: Entity name.
        :type name: str, optional

        :param namespace: Entity namespace.
        :type namespace: str, optional
        """
        if kind is not unset:
            kwargs["kind"] = kind
        if name is not unset:
            kwargs["name"] = name
        if namespace is not unset:
            kwargs["namespace"] = namespace
        super().__init__(kwargs)
