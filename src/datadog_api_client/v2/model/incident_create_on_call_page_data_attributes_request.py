# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_page_role_reference import IncidentPageRoleReference
    from datadog_api_client.v2.model.incident_page_target import IncidentPageTarget


class IncidentCreateOnCallPageDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_page_role_reference import IncidentPageRoleReference
        from datadog_api_client.v2.model.incident_page_target import IncidentPageTarget

        return {
            "description": (str,),
            "role": (IncidentPageRoleReference,),
            "services": ([str],),
            "tags": ([str],),
            "target": (IncidentPageTarget,),
            "title": (str,),
        }

    attribute_map = {
        "description": "description",
        "role": "role",
        "services": "services",
        "tags": "tags",
        "target": "target",
        "title": "title",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        role: Union[IncidentPageRoleReference, UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        target: Union[IncidentPageTarget, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an on-call page from an incident.

        :param description: The description of the page.
        :type description: str, optional

        :param role: A reference to an incident role for a page.
        :type role: IncidentPageRoleReference, optional

        :param services: List of affected services.
        :type services: [str], optional

        :param tags: List of tags for the page.
        :type tags: [str], optional

        :param target: The target recipient for a page.
        :type target: IncidentPageTarget, optional

        :param title: The title of the page.
        :type title: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if role is not unset:
            kwargs["role"] = role
        if services is not unset:
            kwargs["services"] = services
        if tags is not unset:
            kwargs["tags"] = tags
        if target is not unset:
            kwargs["target"] = target
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
