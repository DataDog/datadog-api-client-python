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
    from datadog_api_client.v2.model.cyclone_dx_component_type import CycloneDXComponentType


class CycloneDXComponent(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cyclone_dx_component_type import CycloneDXComponentType

        return {
            "bom_ref": (str,),
            "name": (str,),
            "purl": (str,),
            "type": (CycloneDXComponentType,),
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
        bom_ref: str,
        name: str,
        type: CycloneDXComponentType,
        version: str,
        purl: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A component (library, application, or operating system) in the BOM.

        :param bom_ref: Unique reference identifier for this component.
        :type bom_ref: str

        :param name: The name of the component.
        :type name: str

        :param purl: Package URL for the component. Required for library components.
        :type purl: str, optional

        :param type: The type of the component. Supported types are library, application, and operating-system.
        :type type: CycloneDXComponentType

        :param version: The version of the component.
        :type version: str
        """
        if purl is not unset:
            kwargs["purl"] = purl
        super().__init__(kwargs)

        self_.bom_ref = bom_ref
        self_.name = name
        self_.type = type
        self_.version = version
