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
    from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items import (
        ScaRequestDataAttributesDependenciesItemsLocationsItems,
    )
    from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_reachable_symbol_properties_items import (
        ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems,
    )


class ScaRequestDataAttributesDependenciesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items import (
            ScaRequestDataAttributesDependenciesItemsLocationsItems,
        )
        from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_reachable_symbol_properties_items import (
            ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems,
        )

        return {
            "exclusions": ([str],),
            "group": (str,),
            "is_dev": (bool,),
            "is_direct": (bool,),
            "language": (str,),
            "locations": ([ScaRequestDataAttributesDependenciesItemsLocationsItems],),
            "name": (str,),
            "package_manager": (str,),
            "purl": (str,),
            "reachable_symbol_properties": ([ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems],),
            "version": (str,),
        }

    attribute_map = {
        "exclusions": "exclusions",
        "group": "group",
        "is_dev": "is_dev",
        "is_direct": "is_direct",
        "language": "language",
        "locations": "locations",
        "name": "name",
        "package_manager": "package_manager",
        "purl": "purl",
        "reachable_symbol_properties": "reachable_symbol_properties",
        "version": "version",
    }

    def __init__(
        self_,
        exclusions: Union[List[str], UnsetType] = unset,
        group: Union[str, UnsetType] = unset,
        is_dev: Union[bool, UnsetType] = unset,
        is_direct: Union[bool, UnsetType] = unset,
        language: Union[str, UnsetType] = unset,
        locations: Union[List[ScaRequestDataAttributesDependenciesItemsLocationsItems], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        package_manager: Union[str, UnsetType] = unset,
        purl: Union[str, UnsetType] = unset,
        reachable_symbol_properties: Union[
            List[ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems], UnsetType
        ] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A dependency found in the repository, including its identity, location, and reachability metadata.

        :param exclusions: A list of patterns or identifiers that should be excluded from analysis for this dependency.
        :type exclusions: [str], optional

        :param group: The group or organization namespace of the dependency (e.g., Maven group ID).
        :type group: str, optional

        :param is_dev: Indicates whether this is a development-only dependency not used in production.
        :type is_dev: bool, optional

        :param is_direct: Indicates whether this is a direct dependency (as opposed to a transitive one).
        :type is_direct: bool, optional

        :param language: The programming language ecosystem of this dependency (e.g., java, python, javascript).
        :type language: str, optional

        :param locations: The list of source file locations where this dependency is declared.
        :type locations: [ScaRequestDataAttributesDependenciesItemsLocationsItems], optional

        :param name: The name of the dependency package.
        :type name: str, optional

        :param package_manager: The package manager responsible for this dependency (e.g., maven, pip, npm).
        :type package_manager: str, optional

        :param purl: The Package URL (PURL) uniquely identifying this dependency.
        :type purl: str, optional

        :param reachable_symbol_properties: Properties describing symbols from this dependency that are reachable in the application code.
        :type reachable_symbol_properties: [ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems], optional

        :param version: The version of the dependency.
        :type version: str, optional
        """
        if exclusions is not unset:
            kwargs["exclusions"] = exclusions
        if group is not unset:
            kwargs["group"] = group
        if is_dev is not unset:
            kwargs["is_dev"] = is_dev
        if is_direct is not unset:
            kwargs["is_direct"] = is_direct
        if language is not unset:
            kwargs["language"] = language
        if locations is not unset:
            kwargs["locations"] = locations
        if name is not unset:
            kwargs["name"] = name
        if package_manager is not unset:
            kwargs["package_manager"] = package_manager
        if purl is not unset:
            kwargs["purl"] = purl
        if reachable_symbol_properties is not unset:
            kwargs["reachable_symbol_properties"] = reachable_symbol_properties
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
