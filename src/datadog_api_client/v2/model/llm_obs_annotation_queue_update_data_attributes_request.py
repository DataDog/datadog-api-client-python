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
    from datadog_api_client.v2.model.llm_obs_annotation_schema import LLMObsAnnotationSchema


class LLMObsAnnotationQueueUpdateDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_schema import LLMObsAnnotationSchema

        return {
            "annotation_schema": (LLMObsAnnotationSchema,),
            "description": (str,),
            "name": (str,),
            "restrict_to_assignees": (bool,),
            "restrict_to_reviewers": (bool,),
            "reviewer_emails": ([str],),
        }

    attribute_map = {
        "annotation_schema": "annotation_schema",
        "description": "description",
        "name": "name",
        "restrict_to_assignees": "restrict_to_assignees",
        "restrict_to_reviewers": "restrict_to_reviewers",
        "reviewer_emails": "reviewer_emails",
    }

    def __init__(
        self_,
        annotation_schema: Union[LLMObsAnnotationSchema, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        restrict_to_assignees: Union[bool, UnsetType] = unset,
        restrict_to_reviewers: Union[bool, UnsetType] = unset,
        reviewer_emails: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating an Agent Observability annotation queue. All fields are optional.

        :param annotation_schema: Schema defining the labels for an annotation queue.
        :type annotation_schema: LLMObsAnnotationSchema, optional

        :param description: Updated description of the annotation queue.
        :type description: str, optional

        :param name: Updated name of the annotation queue.
        :type name: str, optional

        :param restrict_to_assignees: Whether annotation access is restricted to assigned users.
        :type restrict_to_assignees: bool, optional

        :param restrict_to_reviewers: Whether annotation access is restricted to queue reviewers.
        :type restrict_to_reviewers: bool, optional

        :param reviewer_emails: Updated email addresses of reviewers who can access the annotation queue.
        :type reviewer_emails: [str], optional
        """
        if annotation_schema is not unset:
            kwargs["annotation_schema"] = annotation_schema
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if restrict_to_assignees is not unset:
            kwargs["restrict_to_assignees"] = restrict_to_assignees
        if restrict_to_reviewers is not unset:
            kwargs["restrict_to_reviewers"] = restrict_to_reviewers
        if reviewer_emails is not unset:
            kwargs["reviewer_emails"] = reviewer_emails
        super().__init__(kwargs)
