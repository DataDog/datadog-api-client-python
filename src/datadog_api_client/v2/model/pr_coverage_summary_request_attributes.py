# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class PRCoverageSummaryRequestAttributes(ModelNormal):
    validations = {
        "pr_number": {
            "inclusive_minimum": 1,
        },
        "repository_url": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "pr_number": (int,),
            "repository_url": (str,),
        }

    attribute_map = {
        "pr_number": "pr_number",
        "repository_url": "repository_url",
    }

    def __init__(self_, pr_number: int, repository_url: str, **kwargs):
        """
        Attributes for requesting code coverage summary for a pull request.

        :param pr_number: The pull request number. Must be a positive integer.
        :type pr_number: int

        :param repository_url: The repository URL. Accepts a full URL with or without a scheme (for example, ``https://github.com/org/repo`` or ``github.com/org/repo`` ).
        :type repository_url: str
        """
        super().__init__(kwargs)

        self_.pr_number = pr_number
        self_.repository_url = repository_url
