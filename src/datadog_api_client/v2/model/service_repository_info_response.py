# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_repository_info_response_data import ServiceRepositoryInfoResponseData


class ServiceRepositoryInfoResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_repository_info_response_data import ServiceRepositoryInfoResponseData

        return {
            "data": (ServiceRepositoryInfoResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ServiceRepositoryInfoResponseData, **kwargs):
        """
        Response containing service repository information.

        :param data: Data object for the service repository info response.
        :type data: ServiceRepositoryInfoResponseData
        """
        super().__init__(kwargs)

        self_.data = data
