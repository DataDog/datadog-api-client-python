# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.spec import Spec


class WorkflowListItemAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spec import Spec

        return {
            "created_at": (datetime,),
            "description": (str,),
            "name": (str,),
            "published": (bool,),
            "spec": (Spec,),
            "tags": ([str],),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "description": "description",
        "name": "name",
        "published": "published",
        "spec": "spec",
        "tags": "tags",
        "updated_at": "updatedAt",
    }
    read_only_vars = {
        "created_at",
        "updated_at",
    }

    def __init__(
        self_,
        name: str,
        created_at: Union[datetime, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        published: Union[bool, UnsetType] = unset,
        spec: Union[Spec, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a workflow returned in a list response.

        :param created_at: When the workflow was created.
        :type created_at: datetime, optional

        :param description: Description of the workflow.
        :type description: str, optional

        :param name: Name of the workflow.
        :type name: str

        :param published: Whether the workflow is published. Unpublished workflows can only be run manually. Automatic triggers such as Schedule do not fire until the workflow is published.
        :type published: bool, optional

        :param spec: The spec defines what the workflow does.
        :type spec: Spec, optional

        :param tags: Tags of the workflow.
        :type tags: [str], optional

        :param updated_at: When the workflow was last updated.
        :type updated_at: datetime, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if description is not unset:
            kwargs["description"] = description
        if published is not unset:
            kwargs["published"] = published
        if spec is not unset:
            kwargs["spec"] = spec
        if tags is not unset:
            kwargs["tags"] = tags
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.name = name
