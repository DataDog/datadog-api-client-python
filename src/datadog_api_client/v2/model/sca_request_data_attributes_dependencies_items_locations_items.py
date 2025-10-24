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
    from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_file_position import (
        ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,
    )


class ScaRequestDataAttributesDependenciesItemsLocationsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_file_position import (
            ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,
        )

        return {
            "block": (ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,),
            "name": (ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,),
            "namespace": (ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,),
            "version": (ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition,),
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
        name: Union[ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition, UnsetType] = unset,
        namespace: Union[ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition, UnsetType] = unset,
        version: Union[ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param block:
        :type block: ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition, optional

        :param name:
        :type name: ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition, optional

        :param namespace:
        :type namespace: ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition, optional

        :param version:
        :type version: ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition, optional
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
