# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_now_template_attributes import ServiceNowTemplateAttributes
    from datadog_api_client.v2.model.service_now_template_type import ServiceNowTemplateType


class ServiceNowTemplateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_template_attributes import ServiceNowTemplateAttributes
        from datadog_api_client.v2.model.service_now_template_type import ServiceNowTemplateType

        return {
            "attributes": (ServiceNowTemplateAttributes,),
            "id": (UUID,),
            "type": (ServiceNowTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ServiceNowTemplateAttributes, id: UUID, type: ServiceNowTemplateType, **kwargs):
        """
        Data object for a ServiceNow template

        :param attributes: Attributes of a ServiceNow template
        :type attributes: ServiceNowTemplateAttributes

        :param id: Unique identifier for the ServiceNow template
        :type id: UUID

        :param type: Type identifier for ServiceNow template resources
        :type type: ServiceNowTemplateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
