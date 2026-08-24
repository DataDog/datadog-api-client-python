# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_file_position import (
        ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,
    )
    from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_nullable_file_position import (
        ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition,
    )


class ScaRequestDataAttributesDependenciesItemsLocationsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_file_position import (
            ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,
        )
        from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_nullable_file_position import (
            ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition,
        )

        return {
            "block": (ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,),
            "name": (ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition,),
            "namespace": (ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition,),
            "version": (ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition,),
        }

    attribute_map = {
        "block": "block",
        "name": "name",
        "namespace": "namespace",
        "version": "version",
    }

    def __init__(
        self_,
        block: Union[ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition, UnsetType] = unset,
        name: Union[
            ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition, none_type, UnsetType
        ] = unset,
        namespace: Union[
            ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition, none_type, UnsetType
        ] = unset,
        version: Union[
            ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition, none_type, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        The source code location where a dependency is declared, including block, name, namespace, and version positions within the file.

        :param block: A range within a file defined by a start and end position, along with the file name.
        :type block: ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition, optional

        :param name: A nullable range within a file defined by a start and end position, along with the file name.
        :type name: ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition, none_type, optional

        :param namespace: A nullable range within a file defined by a start and end position, along with the file name.
        :type namespace: ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition, none_type, optional

        :param version: A nullable range within a file defined by a start and end position, along with the file name.
        :type version: ScaRequestDataAttributesDependenciesItemsLocationsItemsNullableFilePosition, none_type, optional
        """
        if block is not unset:
            kwargs["block"] = block
        if name is not unset:
            kwargs["name"] = name
        if namespace is not unset:
            kwargs["namespace"] = namespace
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
