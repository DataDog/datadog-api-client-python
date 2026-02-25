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
    from datadog_api_client.v2.model.cyclone_dx_reference_source import CycloneDXReferenceSource


class CycloneDXReference(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cyclone_dx_reference_source import CycloneDXReferenceSource

        return {
            "id": (str,),
            "source": (CycloneDXReferenceSource,),
        }

    attribute_map = {
        "id": "id",
        "source": "source",
    }

    def __init__(
        self_, id: Union[str, UnsetType] = unset, source: Union[CycloneDXReferenceSource, UnsetType] = unset, **kwargs
    ):
        """
        External reference for a vulnerability.

        :param id: Identifier of the reference.
        :type id: str, optional

        :param source: Source information for a reference.
        :type source: CycloneDXReferenceSource, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)
