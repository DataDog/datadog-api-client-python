# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_memory_violation_type import AiMemoryViolationType


class AiMemoryViolationResultResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_memory_violation_type import AiMemoryViolationType

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "line": (int,),
            "message": (str,),
            "name": (str,),
            "repository_id": (str,),
            "rule": (str,),
            "sha": (str,),
            "type": (AiMemoryViolationType,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "line": "line",
        "message": "message",
        "name": "name",
        "repository_id": "repository_id",
        "rule": "rule",
        "sha": "sha",
        "type": "type",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        line: int,
        message: str,
        name: str,
        repository_id: str,
        rule: str,
        sha: str,
        type: AiMemoryViolationType,
        **kwargs,
    ):
        """
        Response attributes of an AI memory violation result.

        :param created_at: The creation timestamp.
        :type created_at: datetime

        :param created_by: The identifier of the user who created the result.
        :type created_by: str

        :param line: The line number where the violation was found.
        :type line: int

        :param message: A message explaining the violation result.
        :type message: str

        :param name: The file path where the violation was found.
        :type name: str

        :param repository_id: The repository identifier.
        :type repository_id: str

        :param rule: The rule identifier in the format ruleset/rule.
        :type rule: str

        :param sha: The git commit SHA where the violation was found.
        :type sha: str

        :param type: The type of AI memory violation result indicating whether it is a true positive or false positive.
        :type type: AiMemoryViolationType
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.line = line
        self_.message = message
        self_.name = name
        self_.repository_id = repository_id
        self_.rule = rule
        self_.sha = sha
        self_.type = type
