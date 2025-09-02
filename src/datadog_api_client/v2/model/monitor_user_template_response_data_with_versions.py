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
    from datadog_api_client.v2.model.monitor_user_template import MonitorUserTemplate
    from datadog_api_client.v2.model.monitor_user_template_resource_type import MonitorUserTemplateResourceType


class MonitorUserTemplateResponseDataWithVersions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_user_template import MonitorUserTemplate
        from datadog_api_client.v2.model.monitor_user_template_resource_type import MonitorUserTemplateResourceType

        return {
            "attributes": (MonitorUserTemplate,),
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
        attributes: Union[MonitorUserTemplate, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[MonitorUserTemplateResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Monitor user template data.

        :param attributes: A monitor user template object.
        :type attributes: MonitorUserTemplate, optional

        :param id: The unique identifier.
        :type id: str, optional

        :param type: Monitor user template resource type.
        :type type: MonitorUserTemplateResourceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
