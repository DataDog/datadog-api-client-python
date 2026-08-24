# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
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
            "group": (str, none_type),
            "is_dev": (bool,),
            "is_direct": (bool, none_type),
            "language": (str,),
            "locations": ([ScaRequestDataAttributesDependenciesItemsLocationsItems],),
            "name": (str,),
            "opaque": (bool,),
            "package_manager": (str,),
            "purl": (str,),
            "reachable_symbol_properties": ([ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems],),
            "requires_transitive_enrichment": (bool,),
            "target_frameworks": ([str],),
            "version": (str, none_type),
            "version_constraint": (bool,),
            "version_range": (str,),
        }

    attribute_map = {
        "exclusions": "exclusions",
        "group": "group",
        "is_dev": "is_dev",
        "is_direct": "is_direct",
        "language": "language",
        "locations": "locations",
        "name": "name",
        "opaque": "opaque",
        "package_manager": "package_manager",
        "purl": "purl",
        "reachable_symbol_properties": "reachable_symbol_properties",
        "requires_transitive_enrichment": "requires_transitive_enrichment",
        "target_frameworks": "target_frameworks",
        "version": "version",
        "version_constraint": "version_constraint",
        "version_range": "version_range",
    }

    def __init__(
        self_,
        exclusions: Union[List[str], UnsetType] = unset,
        group: Union[str, none_type, UnsetType] = unset,
        is_dev: Union[bool, UnsetType] = unset,
        is_direct: Union[bool, none_type, UnsetType] = unset,
        language: Union[str, UnsetType] = unset,
        locations: Union[List[ScaRequestDataAttributesDependenciesItemsLocationsItems], none_type, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        opaque: Union[bool, UnsetType] = unset,
        package_manager: Union[str, UnsetType] = unset,
        purl: Union[str, UnsetType] = unset,
        reachable_symbol_properties: Union[
            List[ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems], UnsetType
        ] = unset,
        requires_transitive_enrichment: Union[bool, UnsetType] = unset,
        target_frameworks: Union[List[str], UnsetType] = unset,
        version: Union[str, none_type, UnsetType] = unset,
        version_constraint: Union[bool, UnsetType] = unset,
        version_range: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A dependency found in the repository, including its identity, location, and reachability metadata.

        :param exclusions: A list of patterns or identifiers that should be excluded from analysis for this dependency.
        :type exclusions: [str], optional

        :param group: The group or organization namespace of the dependency (e.g., Maven group ID).
        :type group: str, none_type, optional

        :param is_dev: Indicates whether this is a development-only dependency not used in production.
        :type is_dev: bool, optional

        :param is_direct: Indicates whether this is a direct dependency (as opposed to a transitive one).
        :type is_direct: bool, none_type, optional

        :param language: The programming language ecosystem of this dependency (e.g., java, python, javascript).
        :type language: str, optional

        :param locations: The list of source file locations where this dependency is declared.
        :type locations: [ScaRequestDataAttributesDependenciesItemsLocationsItems], none_type, optional

        :param name: The name of the dependency package.
        :type name: str, optional

        :param opaque: Indicates whether dependency details are intentionally opaque.
        :type opaque: bool, optional

        :param package_manager: The package manager responsible for this dependency (e.g., maven, pip, npm).
        :type package_manager: str, optional

        :param purl: The Package URL (PURL) uniquely identifying this dependency.
        :type purl: str, optional

        :param reachable_symbol_properties: Properties describing symbols from this dependency that are reachable in the application code.
        :type reachable_symbol_properties: [ScaRequestDataAttributesDependenciesItemsReachableSymbolPropertiesItems], optional

        :param requires_transitive_enrichment: Indicates whether this dependency requires transitive dependency enrichment.
        :type requires_transitive_enrichment: bool, optional

        :param target_frameworks: The target framework identifiers associated with this dependency.
        :type target_frameworks: [str], optional

        :param version: The version of the dependency.
        :type version: str, none_type, optional

        :param version_constraint: Indicates whether the version value represents a version constraint.
        :type version_constraint: bool, optional

        :param version_range: The version range associated with this dependency when a manifest declares a range.
        :type version_range: str, optional
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
        if opaque is not unset:
            kwargs["opaque"] = opaque
        if package_manager is not unset:
            kwargs["package_manager"] = package_manager
        if purl is not unset:
            kwargs["purl"] = purl
        if reachable_symbol_properties is not unset:
            kwargs["reachable_symbol_properties"] = reachable_symbol_properties
        if requires_transitive_enrichment is not unset:
            kwargs["requires_transitive_enrichment"] = requires_transitive_enrichment
        if target_frameworks is not unset:
            kwargs["target_frameworks"] = target_frameworks
        if version is not unset:
            kwargs["version"] = version
        if version_constraint is not unset:
            kwargs["version_constraint"] = version_constraint
        if version_range is not unset:
            kwargs["version_range"] = version_range
        super().__init__(kwargs)
