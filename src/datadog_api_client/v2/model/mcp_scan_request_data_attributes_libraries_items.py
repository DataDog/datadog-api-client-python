# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class McpScanRequestDataAttributesLibrariesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "exclusions": ([str],),
            "is_dev": (bool,),
            "is_direct": (bool,),
            "package_manager": (str,),
            "purl": (str,),
            "target_frameworks": ([str],),
        }

    attribute_map = {
        "exclusions": "exclusions",
        "is_dev": "is_dev",
        "is_direct": "is_direct",
        "package_manager": "package_manager",
        "purl": "purl",
        "target_frameworks": "target_frameworks",
    }

    def __init__(
        self_,
        is_dev: bool,
        is_direct: bool,
        package_manager: str,
        purl: str,
        exclusions: Union[List[str], UnsetType] = unset,
        target_frameworks: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A library declaration to include in the dependency scan.

        :param exclusions: The list of dependency PURLs to exclude when resolving transitive dependencies for this library.
        :type exclusions: [str], optional

        :param is_dev: Whether this library is a development-only dependency.
        :type is_dev: bool

        :param is_direct: Whether this library is a direct (rather than transitive) dependency.
        :type is_direct: bool

        :param package_manager: The package manager that produced this library entry (for example, ``npm`` , ``pip`` , ``nuget`` ).
        :type package_manager: str

        :param purl: The Package URL (PURL) uniquely identifying the library and its version.
        :type purl: str

        :param target_frameworks: The list of target framework identifiers associated with the library.
        :type target_frameworks: [str], optional
        """
        if exclusions is not unset:
            kwargs["exclusions"] = exclusions
        if target_frameworks is not unset:
            kwargs["target_frameworks"] = target_frameworks
        super().__init__(kwargs)

        self_.is_dev = is_dev
        self_.is_direct = is_direct
        self_.package_manager = package_manager
        self_.purl = purl
