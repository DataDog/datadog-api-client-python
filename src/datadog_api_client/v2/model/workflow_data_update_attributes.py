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
    from datadog_api_client.v2.model.workflow_run_as import WorkflowRunAs
    from datadog_api_client.v2.model.workflow_run_as_user_mode import WorkflowRunAsUserMode
    from datadog_api_client.v2.model.spec import Spec
    from datadog_api_client.v2.model.workflow_run_as_owner import WorkflowRunAsOwner
    from datadog_api_client.v2.model.workflow_run_as_service_account import WorkflowRunAsServiceAccount
    from datadog_api_client.v2.model.workflow_run_as_initiator import WorkflowRunAsInitiator


class WorkflowDataUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_run_as import WorkflowRunAs
        from datadog_api_client.v2.model.workflow_run_as_user_mode import WorkflowRunAsUserMode
        from datadog_api_client.v2.model.spec import Spec

        return {
            "created_at": (datetime,),
            "description": (str,),
            "name": (str,),
            "published": (bool,),
            "run_as": (WorkflowRunAs,),
            "run_as_user_mode": (WorkflowRunAsUserMode,),
            "spec": (Spec,),
            "tags": ([str],),
            "updated_at": (datetime,),
            "webhook_secret": (str,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "description": "description",
        "name": "name",
        "published": "published",
        "run_as": "runAs",
        "run_as_user_mode": "runAsUserMode",
        "spec": "spec",
        "tags": "tags",
        "updated_at": "updatedAt",
        "webhook_secret": "webhookSecret",
    }
    read_only_vars = {
        "created_at",
        "updated_at",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        published: Union[bool, UnsetType] = unset,
        run_as: Union[
            WorkflowRunAs, WorkflowRunAsOwner, WorkflowRunAsServiceAccount, WorkflowRunAsInitiator, UnsetType
        ] = unset,
        run_as_user_mode: Union[WorkflowRunAsUserMode, UnsetType] = unset,
        spec: Union[Spec, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        webhook_secret: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``WorkflowDataUpdateAttributes`` object.

        :param created_at: When the workflow was created.
        :type created_at: datetime, optional

        :param description: Description of the workflow.
        :type description: str, optional

        :param name: Name of the workflow.
        :type name: str, optional

        :param published: Set the workflow to published or unpublished. Workflows in an unpublished state will only be executable via manual runs. Automatic triggers such as Schedule will not execute the workflow until it is published.
        :type published: bool, optional

        :param run_as: Identity used to run the workflow.
        :type run_as: WorkflowRunAs, optional

        :param run_as_user_mode: The effective type of identity used to run the workflow.
        :type run_as_user_mode: WorkflowRunAsUserMode, optional

        :param spec: A complete Workflow Automation definition, including its triggers, steps, and connections.
        :type spec: Spec, optional

        :param tags: Tags of the workflow.
        :type tags: [str], optional

        :param updated_at: When the workflow was last updated.
        :type updated_at: datetime, optional

        :param webhook_secret: If a Webhook trigger is defined on this workflow, a webhookSecret is required and should be provided here.
        :type webhook_secret: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if published is not unset:
            kwargs["published"] = published
        if run_as is not unset:
            kwargs["run_as"] = run_as
        if run_as_user_mode is not unset:
            kwargs["run_as_user_mode"] = run_as_user_mode
        if spec is not unset:
            kwargs["spec"] = spec
        if tags is not unset:
            kwargs["tags"] = tags
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if webhook_secret is not unset:
            kwargs["webhook_secret"] = webhook_secret
        super().__init__(kwargs)
