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
    from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_position import (
        ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition,
    )


class ScaRequestDataAttributesDependenciesItemsLocationsItemsFilePosition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items_locations_items_position import (
            ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition,
        )

        return {
            "end": (ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition,),
            "file_name": (str,),
            "start": (ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition,),
        }

    attribute_map = {
        "end": "end",
        "file_name": "file_name",
        "start": "start",
    }

    def __init__(
        self_,
        end: Union[ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition, UnsetType] = unset,
        file_name: Union[str, UnsetType] = unset,
        start: Union[ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param end:
        :type end: ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition, optional

        :param file_name:
        :type file_name: str, optional

        :param start:
        :type start: ScaRequestDataAttributesDependenciesItemsLocationsItemsPosition, optional
        """
        if end is not unset:
            kwargs["end"] = end
        if file_name is not unset:
            kwargs["file_name"] = file_name
        if start is not unset:
            kwargs["start"] = start
        super().__init__(kwargs)
