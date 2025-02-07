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
    from datadog_api_client.v2.model.workflow_user_relationship import WorkflowUserRelationship


class WorkflowDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_user_relationship import WorkflowUserRelationship

        return {
            "creator": (WorkflowUserRelationship,),
            "owner": (WorkflowUserRelationship,),
        }

    attribute_map = {
        "creator": "creator",
        "owner": "owner",
    }

    def __init__(
        self_,
        creator: Union[WorkflowUserRelationship, UnsetType] = unset,
        owner: Union[WorkflowUserRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``WorkflowDataRelationships`` object.

        :param creator: The definition of ``WorkflowUserRelationship`` object.
        :type creator: WorkflowUserRelationship, optional

        :param owner: The definition of ``WorkflowUserRelationship`` object.
        :type owner: WorkflowUserRelationship, optional
        """
        if creator is not unset:
            kwargs["creator"] = creator
        if owner is not unset:
            kwargs["owner"] = owner
        super().__init__(kwargs)
