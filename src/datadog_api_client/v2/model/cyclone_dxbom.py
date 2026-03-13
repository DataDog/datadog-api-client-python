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
    from datadog_api_client.v2.model.cyclone_dx_component import CycloneDXComponent
    from datadog_api_client.v2.model.cyclone_dx_metadata import CycloneDXMetadata
    from datadog_api_client.v2.model.cyclone_dx_vulnerability import CycloneDXVulnerability


class CycloneDXBOM(ModelNormal):
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
        version: int,
        vulnerabilities: List[CycloneDXVulnerability],
        **kwargs,
    ):
        """
        CycloneDX 1.5 Bill of Materials (BOM) for importing vulnerabilities.

        :param bom_format: The format of the BOM. Must be "CycloneDX".
        :type bom_format: str

        :param components: List of components (libraries, applications, or operating systems) that are affected by vulnerabilities.
        :type components: [CycloneDXComponent]

        :param metadata: Metadata for the CycloneDX BOM.
        :type metadata: CycloneDXMetadata

        :param spec_version: The version of the CycloneDX specification. Must be "1.5".
        :type spec_version: str

        :param version: The version of the BOM.
        :type version: int

        :param vulnerabilities: List of vulnerabilities to be imported.
        :type vulnerabilities: [CycloneDXVulnerability]
        """
        super().__init__(kwargs)

        self_.bom_format = bom_format
        self_.components = components
        self_.metadata = metadata
        self_.spec_version = spec_version
        self_.version = version
        self_.vulnerabilities = vulnerabilities
