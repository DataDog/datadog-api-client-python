# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GitHubOIDCClaimPatterns(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "actor": (str,),
            "actor_id": (str,),
            "enterprise": (str,),
            "enterprise_id": (str,),
            "environment": (str,),
            "event_name": (str,),
            "job_workflow_ref": (str,),
            "ref": (str,),
            "ref_type": (str,),
            "repository": (str,),
            "repository_id": (str,),
            "repository_owner": (str,),
            "repository_owner_id": (str,),
            "repository_visibility": (str,),
            "runner_environment": (str,),
            "sub": (str,),
            "workflow": (str,),
            "workflow_ref": (str,),
        }

    attribute_map = {
        "actor": "actor",
        "actor_id": "actor_id",
        "enterprise": "enterprise",
        "enterprise_id": "enterprise_id",
        "environment": "environment",
        "event_name": "event_name",
        "job_workflow_ref": "job_workflow_ref",
        "ref": "ref",
        "ref_type": "ref_type",
        "repository": "repository",
        "repository_id": "repository_id",
        "repository_owner": "repository_owner",
        "repository_owner_id": "repository_owner_id",
        "repository_visibility": "repository_visibility",
        "runner_environment": "runner_environment",
        "sub": "sub",
        "workflow": "workflow",
        "workflow_ref": "workflow_ref",
    }

    def __init__(
        self_,
        sub: str,
        actor: Union[str, UnsetType] = unset,
        actor_id: Union[str, UnsetType] = unset,
        enterprise: Union[str, UnsetType] = unset,
        enterprise_id: Union[str, UnsetType] = unset,
        environment: Union[str, UnsetType] = unset,
        event_name: Union[str, UnsetType] = unset,
        job_workflow_ref: Union[str, UnsetType] = unset,
        ref: Union[str, UnsetType] = unset,
        ref_type: Union[str, UnsetType] = unset,
        repository: Union[str, UnsetType] = unset,
        repository_id: Union[str, UnsetType] = unset,
        repository_owner: Union[str, UnsetType] = unset,
        repository_owner_id: Union[str, UnsetType] = unset,
        repository_visibility: Union[str, UnsetType] = unset,
        runner_environment: Union[str, UnsetType] = unset,
        workflow: Union[str, UnsetType] = unset,
        workflow_ref: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        GitHub Actions OIDC claims to match against. Each field is a regular expression.
        The ``sub`` claim is required; all other claims are optional. A token matches only when
        all provided patterns match simultaneously (AND semantics).

        :param actor: Regular expression matched against the ``actor`` claim.
        :type actor: str, optional

        :param actor_id: Regular expression matched against the ``actor_id`` claim.
        :type actor_id: str, optional

        :param enterprise: Regular expression matched against the ``enterprise`` claim.
        :type enterprise: str, optional

        :param enterprise_id: Regular expression matched against the ``enterprise_id`` claim.
        :type enterprise_id: str, optional

        :param environment: Regular expression matched against the ``environment`` claim.
        :type environment: str, optional

        :param event_name: Regular expression matched against the ``event_name`` claim.
        :type event_name: str, optional

        :param job_workflow_ref: Regular expression matched against the ``job_workflow_ref`` claim.
        :type job_workflow_ref: str, optional

        :param ref: Regular expression matched against the ``ref`` claim.
        :type ref: str, optional

        :param ref_type: Regular expression matched against the ``ref_type`` claim.
        :type ref_type: str, optional

        :param repository: Regular expression matched against the ``repository`` claim.
        :type repository: str, optional

        :param repository_id: Regular expression matched against the ``repository_id`` claim.
        :type repository_id: str, optional

        :param repository_owner: Regular expression matched against the ``repository_owner`` claim.
        :type repository_owner: str, optional

        :param repository_owner_id: Regular expression matched against the ``repository_owner_id`` claim.
        :type repository_owner_id: str, optional

        :param repository_visibility: Regular expression matched against the ``repository_visibility`` claim.
        :type repository_visibility: str, optional

        :param runner_environment: Regular expression matched against the ``runner_environment`` claim.
        :type runner_environment: str, optional

        :param sub: Regular expression matched against the entire ``sub`` (subject) claim, the primary GitHub Actions OIDC
            identifier (for example, ``repo:<OWNER>/<REPO>:ref:refs/heads/main`` ). The pattern must begin with
            ``repo:<OWNER>/`` , where ``<OWNER>`` is a literal repository-owner name rather than a regular expression.
        :type sub: str

        :param workflow: Regular expression matched against the ``workflow`` claim.
        :type workflow: str, optional

        :param workflow_ref: Regular expression matched against the ``workflow_ref`` claim.
        :type workflow_ref: str, optional
        """
        if actor is not unset:
            kwargs["actor"] = actor
        if actor_id is not unset:
            kwargs["actor_id"] = actor_id
        if enterprise is not unset:
            kwargs["enterprise"] = enterprise
        if enterprise_id is not unset:
            kwargs["enterprise_id"] = enterprise_id
        if environment is not unset:
            kwargs["environment"] = environment
        if event_name is not unset:
            kwargs["event_name"] = event_name
        if job_workflow_ref is not unset:
            kwargs["job_workflow_ref"] = job_workflow_ref
        if ref is not unset:
            kwargs["ref"] = ref
        if ref_type is not unset:
            kwargs["ref_type"] = ref_type
        if repository is not unset:
            kwargs["repository"] = repository
        if repository_id is not unset:
            kwargs["repository_id"] = repository_id
        if repository_owner is not unset:
            kwargs["repository_owner"] = repository_owner
        if repository_owner_id is not unset:
            kwargs["repository_owner_id"] = repository_owner_id
        if repository_visibility is not unset:
            kwargs["repository_visibility"] = repository_visibility
        if runner_environment is not unset:
            kwargs["runner_environment"] = runner_environment
        if workflow is not unset:
            kwargs["workflow"] = workflow
        if workflow_ref is not unset:
            kwargs["workflow_ref"] = workflow_ref
        super().__init__(kwargs)

        self_.sub = sub
