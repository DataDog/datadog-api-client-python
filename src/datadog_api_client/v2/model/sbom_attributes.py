# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sbom_component import SBOMComponent
    from datadog_api_client.v2.model.sbom_component_dependency import SBOMComponentDependency
    from datadog_api_client.v2.model.sbom_metadata import SBOMMetadata
    from datadog_api_client.v2.model.spec_version import SpecVersion


class SBOMAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sbom_component import SBOMComponent
        from datadog_api_client.v2.model.sbom_component_dependency import SBOMComponentDependency
        from datadog_api_client.v2.model.sbom_metadata import SBOMMetadata
        from datadog_api_client.v2.model.spec_version import SpecVersion

        return {
            "bom_format": (str,),
            "components": ([SBOMComponent],),
            "dependencies": ([SBOMComponentDependency],),
            "metadata": (SBOMMetadata,),
            "serial_number": (str,),
            "spec_version": (SpecVersion,),
            "version": (int,),
        }

    attribute_map = {
        "bom_format": "bomFormat",
        "components": "components",
        "dependencies": "dependencies",
        "metadata": "metadata",
        "serial_number": "serialNumber",
        "spec_version": "specVersion",
        "version": "version",
    }

    def __init__(
        self_,
        bom_format: str,
        components: List[SBOMComponent],
        dependencies: List[SBOMComponentDependency],
        metadata: SBOMMetadata,
        serial_number: str,
        spec_version: SpecVersion,
        version: int,
        **kwargs,
    ):
        """
        The JSON:API attributes of the SBOM.

        :param bom_format: Specifies the format of the BOM. This helps to identify the file as CycloneDX since BOM do not have a filename convention nor does JSON schema support namespaces. This value MUST be ``CycloneDX``.
        :type bom_format: str

        :param components: A list of software and hardware components.
        :type components: [SBOMComponent]

        :param dependencies: List of dependencies between components of the SBOM.
        :type dependencies: [SBOMComponentDependency]

        :param metadata: Provides additional information about a BOM.
        :type metadata: SBOMMetadata

        :param serial_number: Every BOM generated has a unique serial number, even if the contents of the BOM have not changed overt time. The serial number follows `RFC-4122 <https://datatracker.ietf.org/doc/html/rfc4122>`_
        :type serial_number: str

        :param spec_version: The version of the CycloneDX specification a BOM conforms to.
        :type spec_version: SpecVersion

        :param version: It increments when a BOM is modified. The default value is 1.
        :type version: int
        """
        super().__init__(kwargs)

        self_.bom_format = bom_format
        self_.components = components
        self_.dependencies = dependencies
        self_.metadata = metadata
        self_.serial_number = serial_number
        self_.spec_version = spec_version
        self_.version = version
