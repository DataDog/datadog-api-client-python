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
    from datadog_api_client.v2.model.service_now_template_update_request_attributes import (
        ServiceNowTemplateUpdateRequestAttributes,
    )
    from datadog_api_client.v2.model.service_now_template_type import ServiceNowTemplateType


class ServiceNowTemplateUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_template_update_request_attributes import (
            ServiceNowTemplateUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.service_now_template_type import ServiceNowTemplateType

        return {
            "attributes": (ServiceNowTemplateUpdateRequestAttributes,),
            "type": (ServiceNowTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: ServiceNowTemplateUpdateRequestAttributes, type: ServiceNowTemplateType, **kwargs):
        """
        Data object for updating a ServiceNow template

        :param attributes: Attributes for updating a ServiceNow template
        :type attributes: ServiceNowTemplateUpdateRequestAttributes

        :param type: Type identifier for ServiceNow template resources
        :type type: ServiceNowTemplateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
