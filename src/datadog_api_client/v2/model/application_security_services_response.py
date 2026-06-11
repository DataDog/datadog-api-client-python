# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.application_security_service_resource import ApplicationSecurityServiceResource
    from datadog_api_client.v2.model.application_security_services_metadata import ApplicationSecurityServicesMetadata


class ApplicationSecurityServicesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_service_resource import ApplicationSecurityServiceResource
        from datadog_api_client.v2.model.application_security_services_metadata import (
            ApplicationSecurityServicesMetadata,
        )

        return {
            "data": ([ApplicationSecurityServiceResource],),
            "meta": (ApplicationSecurityServicesMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[ApplicationSecurityServiceResource], meta: ApplicationSecurityServicesMetadata, **kwargs
    ):
        """
        Response object containing the list of services matching the requested name.

        :param data: The list of services matching the requested name.
        :type data: [ApplicationSecurityServiceResource]

        :param meta: Metadata returned alongside the list of services.
        :type meta: ApplicationSecurityServicesMetadata
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
