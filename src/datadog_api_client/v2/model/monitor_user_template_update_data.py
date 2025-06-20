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
    from datadog_api_client.v2.model.monitor_user_template_request_attributes import (
        MonitorUserTemplateRequestAttributes,
    )
    from datadog_api_client.v2.model.monitor_user_template_resource_type import MonitorUserTemplateResourceType


class MonitorUserTemplateUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_user_template_request_attributes import (
            MonitorUserTemplateRequestAttributes,
        )
        from datadog_api_client.v2.model.monitor_user_template_resource_type import MonitorUserTemplateResourceType

        return {
            "attributes": (MonitorUserTemplateRequestAttributes,),
            "id": (str,),
            "type": (MonitorUserTemplateResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: MonitorUserTemplateRequestAttributes,
        id: str,
        type: MonitorUserTemplateResourceType,
        **kwargs,
    ):
        """
        Monitor user template data.

        :param attributes: Attributes for a monitor user template.
        :type attributes: MonitorUserTemplateRequestAttributes

        :param id: The unique identifier.
        :type id: str

        :param type: Monitor user template resource type.
        :type type: MonitorUserTemplateResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
