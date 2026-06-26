# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cyclone_dx_component import CycloneDXComponent
    from datadog_api_client.v2.model.cyclone_dx_metadata import CycloneDXMetadata
    from datadog_api_client.v2.model.cyclone_dx_vulnerability import CycloneDXVulnerability


class CycloneDXBom(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cyclone_dx_component import CycloneDXComponent
        from datadog_api_client.v2.model.cyclone_dx_metadata import CycloneDXMetadata
        from datadog_api_client.v2.model.cyclone_dx_vulnerability import CycloneDXVulnerability

        return {
            "bom_format": (str,),
            "components": ([CycloneDXComponent],),
            "metadata": (CycloneDXMetadata,),
            "spec_version": (str,),
            "version": (int,),
            "vulnerabilities": ([CycloneDXVulnerability],),
        }

    attribute_map = {
        "bom_format": "bomFormat",
        "components": "components",
        "metadata": "metadata",
        "spec_version": "specVersion",
        "version": "version",
        "vulnerabilities": "vulnerabilities",
    }

    def __init__(
        self_,
        bom_format: str,
        components: List[CycloneDXComponent],
        metadata: CycloneDXMetadata,
        spec_version: str,
        vulnerabilities: List[CycloneDXVulnerability],
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A CycloneDX 1.5 Bill of Materials (BOM) document containing vulnerability data.

        :param bom_format: The BOM format identifier. Must be ``CycloneDX``.
        :type bom_format: str

        :param components: The list of scanned software components. Cannot be empty.
        :type components: [CycloneDXComponent]

        :param metadata: Metadata about the BOM, including the scanned asset and the scanner tool.
        :type metadata: CycloneDXMetadata

        :param spec_version: The CycloneDX specification version. Must be ``1.5``.
        :type spec_version: str

        :param version: The version number of the BOM document.
        :type version: int, optional

        :param vulnerabilities: The list of detected vulnerabilities. Cannot be empty.
        :type vulnerabilities: [CycloneDXVulnerability]
        """
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.bom_format = bom_format
        self_.components = components
        self_.metadata = metadata
        self_.spec_version = spec_version
        self_.vulnerabilities = vulnerabilities
