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
    from datadog_api_client.v2.model.get_mapping_response_data_attributes_attributes_items import (
        GetMappingResponseDataAttributesAttributesItems,
    )


class GetMappingResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_mapping_response_data_attributes_attributes_items import (
            GetMappingResponseDataAttributesAttributesItems,
        )

        return {
            "attributes": ([GetMappingResponseDataAttributesAttributesItems],),
        }

    attribute_map = {
        "attributes": "attributes",
    }

    def __init__(
        self_, attributes: Union[List[GetMappingResponseDataAttributesAttributesItems], UnsetType] = unset, **kwargs
    ):
        """


        :param attributes:
        :type attributes: [GetMappingResponseDataAttributesAttributesItems], optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)
