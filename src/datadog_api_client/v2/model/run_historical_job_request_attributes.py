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
    from datadog_api_client.v2.model.job_definition_from_rule import JobDefinitionFromRule
    from datadog_api_client.v2.model.job_definition import JobDefinition


class RunHistoricalJobRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.job_definition_from_rule import JobDefinitionFromRule
        from datadog_api_client.v2.model.job_definition import JobDefinition

        return {
            "from_rule": (JobDefinitionFromRule,),
            "id": (str,),
            "job_definition": (JobDefinition,),
        }

    attribute_map = {
        "from_rule": "fromRule",
        "id": "id",
        "job_definition": "jobDefinition",
    }

    def __init__(
        self_,
        from_rule: Union[JobDefinitionFromRule, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        job_definition: Union[JobDefinition, UnsetType] = unset,
        **kwargs,
    ):
        """
        Run a historical job request.

        :param from_rule: Definition of a historical job based on a security monitoring rule.
        :type from_rule: JobDefinitionFromRule, optional

        :param id: Request ID.
        :type id: str, optional

        :param job_definition: Definition of a historical job.
        :type job_definition: JobDefinition, optional
        """
        if from_rule is not unset:
            kwargs["from_rule"] = from_rule
        if id is not unset:
            kwargs["id"] = id
        if job_definition is not unset:
            kwargs["job_definition"] = job_definition
        super().__init__(kwargs)
