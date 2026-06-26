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


class CycloneDXMetadataComponent(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "bom_ref": (str,),
            "name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "bom_ref": "bom-ref",
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_, name: str, bom_ref: Union[str, UnsetType] = unset, type: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        The asset that was scanned (for example, a host or container image).

        :param bom_ref: A unique reference identifier for this metadata component. If set, must match a ``bom-ref`` in ``components``.
        :type bom_ref: str, optional

        :param name: The name or identifier of the scanned asset (for example, an instance ID or hostname).
        :type name: str

        :param type: The type of the scanned asset.
        :type type: str, optional
        """
        if bom_ref is not unset:
            kwargs["bom_ref"] = bom_ref
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.name = name
