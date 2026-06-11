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
    from datadog_api_client.v2.model.application_security_service_attributes import ApplicationSecurityServiceAttributes
    from datadog_api_client.v2.model.application_security_service_type import ApplicationSecurityServiceType


class ApplicationSecurityServiceResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_service_attributes import (
            ApplicationSecurityServiceAttributes,
        )
        from datadog_api_client.v2.model.application_security_service_type import ApplicationSecurityServiceType

        return {
            "attributes": (ApplicationSecurityServiceAttributes,),
            "id": (str,),
            "type": (ApplicationSecurityServiceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ApplicationSecurityServiceAttributes, id: str, type: ApplicationSecurityServiceType, **kwargs
    ):
        """
        A JSON:API resource describing a service and its Application Security details.

        :param attributes: Application Security details describing a service in a given environment.
        :type attributes: ApplicationSecurityServiceAttributes

        :param id: The unique identifier of the service, formatted as ``<service>_<environment>``.
        :type id: str

        :param type: The type of the resource. The value should always be ``service_env``.
        :type type: ApplicationSecurityServiceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
