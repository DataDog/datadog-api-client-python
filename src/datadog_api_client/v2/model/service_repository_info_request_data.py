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
    from datadog_api_client.v2.model.service_repository_info_request_attributes import (
        ServiceRepositoryInfoRequestAttributes,
    )
    from datadog_api_client.v2.model.service_repository_info_data_type import ServiceRepositoryInfoDataType


class ServiceRepositoryInfoRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_repository_info_request_attributes import (
            ServiceRepositoryInfoRequestAttributes,
        )
        from datadog_api_client.v2.model.service_repository_info_data_type import ServiceRepositoryInfoDataType

        return {
            "attributes": (ServiceRepositoryInfoRequestAttributes,),
            "type": (ServiceRepositoryInfoDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: ServiceRepositoryInfoRequestAttributes, type: ServiceRepositoryInfoDataType, **kwargs
    ):
        """
        Data object for the service repository info request.

        :param attributes: Attributes for the service repository info request.
        :type attributes: ServiceRepositoryInfoRequestAttributes

        :param type: The resource type for service repository info objects.
        :type type: ServiceRepositoryInfoDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
