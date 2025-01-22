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
    from datadog_api_client.v2.model.sbom_component_type import SBOMComponentType


class SBOMComponent(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sbom_component_type import SBOMComponentType

        return {
            "bom_ref": (str,),
            "name": (str,),
            "purl": (str,),
            "type": (SBOMComponentType,),
            "version": (str,),
        }

    attribute_map = {
        "bom_ref": "bom-ref",
        "name": "name",
        "purl": "purl",
        "type": "type",
        "version": "version",
    }

    def __init__(
        self_,
        name: str,
        type: SBOMComponentType,
        version: str,
        bom_ref: Union[str, UnsetType] = unset,
        purl: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Software or hardware component.

        :param bom_ref: An optional identifier that can be used to reference the component elsewhere in the BOM.
        :type bom_ref: str, optional

        :param name: The name of the component. This will often be a shortened, single name of the component.
        :type name: str

        :param purl: Specifies the package-url (purl). The purl, if specified, MUST be valid and conform to the `specification <https://github.com/package-url/purl-spec>`_.
        :type purl: str, optional

        :param type: The SBOM component type
        :type type: SBOMComponentType

        :param version: The component version.
        :type version: str
        """
        if bom_ref is not unset:
            kwargs["bom_ref"] = bom_ref
        if purl is not unset:
            kwargs["purl"] = purl
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
        self_.version = version
