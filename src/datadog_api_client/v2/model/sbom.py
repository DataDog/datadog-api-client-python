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
    from datadog_api_client.v2.model.sbom_attributes import SBOMAttributes
    from datadog_api_client.v2.model.sbom_type import SBOMType


class SBOM(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sbom_attributes import SBOMAttributes
        from datadog_api_client.v2.model.sbom_type import SBOMType

        return {
            "attributes": (SBOMAttributes,),
            "id": (str,),
            "type": (SBOMType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SBOMAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SBOMType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single SBOM

        :param attributes: The JSON:API attributes of the SBOM.
        :type attributes: SBOMAttributes, optional

        :param id: The unique ID for this SBOM (it is equivalent to the ``asset_name`` or ``asset_name@repo_digest`` (Image)
        :type id: str, optional

        :param type: The JSON:API type.
        :type type: SBOMType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
