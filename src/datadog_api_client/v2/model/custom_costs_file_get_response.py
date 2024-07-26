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
    from datadog_api_client.v2.model.custom_costs_file_metadata_with_content_high_level import (
        CustomCostsFileMetadataWithContentHighLevel,
    )
    from datadog_api_client.v2.model.custom_cost_get_response_meta import CustomCostGetResponseMeta


class CustomCostsFileGetResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_costs_file_metadata_with_content_high_level import (
            CustomCostsFileMetadataWithContentHighLevel,
        )
        from datadog_api_client.v2.model.custom_cost_get_response_meta import CustomCostGetResponseMeta

        return {
            "data": (CustomCostsFileMetadataWithContentHighLevel,),
            "meta": (CustomCostGetResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[CustomCostsFileMetadataWithContentHighLevel, UnsetType] = unset,
        meta: Union[CustomCostGetResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for Get Custom Costs files.

        :param data: JSON API format of for a Custom Costs file with content.
        :type data: CustomCostsFileMetadataWithContentHighLevel, optional

        :param meta: Meta for the response from the Get Custom Costs endpoints.
        :type meta: CustomCostGetResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
