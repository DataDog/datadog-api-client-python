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
    from datadog_api_client.v2.model.custom_costs_file_metadata_high_level import CustomCostsFileMetadataHighLevel
    from datadog_api_client.v2.model.custom_cost_upload_response_meta import CustomCostUploadResponseMeta


class CustomCostsFileUploadResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_costs_file_metadata_high_level import CustomCostsFileMetadataHighLevel
        from datadog_api_client.v2.model.custom_cost_upload_response_meta import CustomCostUploadResponseMeta

        return {
            "data": (CustomCostsFileMetadataHighLevel,),
            "meta": (CustomCostUploadResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[CustomCostsFileMetadataHighLevel, UnsetType] = unset,
        meta: Union[CustomCostUploadResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for Uploaded Custom Costs files.

        :param data: JSON API format for a Custom Costs file.
        :type data: CustomCostsFileMetadataHighLevel, optional

        :param meta: Meta for the response from the Upload Custom Costs endpoints.
        :type meta: CustomCostUploadResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
