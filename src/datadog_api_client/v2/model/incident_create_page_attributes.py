# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_page_target import IncidentPageTarget


class IncidentCreatePageAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_page_target import IncidentPageTarget

        return {
            "description": (str, none_type),
            "services": ([str], none_type),
            "tags": ([str], none_type),
            "target": (IncidentPageTarget,),
            "title": (str,),
        }

    attribute_map = {
        "description": "description",
        "services": "services",
        "tags": "tags",
        "target": "target",
        "title": "title",
    }

    def __init__(
        self_,
        target: IncidentPageTarget,
        title: str,
        description: Union[str, none_type, UnsetType] = unset,
        services: Union[List[str], none_type, UnsetType] = unset,
        tags: Union[List[str], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a page from an incident.

        :param description: Description of the page.
        :type description: str, none_type, optional

        :param services: List of services associated with the page.
        :type services: [str], none_type, optional

        :param tags: List of tags for the page.
        :type tags: [str], none_type, optional

        :param target: Target for creating a page from an incident.
        :type target: IncidentPageTarget

        :param title: Title of the page.
        :type title: str
        """
        if description is not unset:
            kwargs["description"] = description
        if services is not unset:
            kwargs["services"] = services
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.target = target
        self_.title = title
