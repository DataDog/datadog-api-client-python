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
    from datadog_api_client.v2.model.mcp_scan_request_data_attributes_libraries_items import (
        McpScanRequestDataAttributesLibrariesItems,
    )


class McpScanRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.mcp_scan_request_data_attributes_libraries_items import (
            McpScanRequestDataAttributesLibrariesItems,
        )

        return {
            "commit_hash": (str,),
            "libraries": ([McpScanRequestDataAttributesLibrariesItems],),
            "resource_name": (str,),
        }

    attribute_map = {
        "commit_hash": "commit_hash",
        "libraries": "libraries",
        "resource_name": "resource_name",
    }

    def __init__(
        self_,
        commit_hash: str,
        libraries: List[McpScanRequestDataAttributesLibrariesItems],
        resource_name: str,
        **kwargs,
    ):
        """
        The attributes of an MCP SCA scan request, describing the libraries to scan and their context.

        :param commit_hash: The commit hash of the source code being scanned.
        :type commit_hash: str

        :param libraries: The list of libraries to scan for vulnerabilities.
        :type libraries: [McpScanRequestDataAttributesLibrariesItems]

        :param resource_name: The name of the resource (typically the repository or project name) being scanned.
        :type resource_name: str
        """
        super().__init__(kwargs)

        self_.commit_hash = commit_hash
        self_.libraries = libraries
        self_.resource_name = resource_name
