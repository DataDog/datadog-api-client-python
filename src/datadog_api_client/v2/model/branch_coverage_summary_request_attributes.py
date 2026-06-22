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


class BranchCoverageSummaryRequestAttributes(ModelNormal):
    validations = {
        "branch": {
            "min_length": 1,
        },
        "repository_id": {
            "min_length": 1,
        },
        "repository_url": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "branch": (str,),
            "repository_id": (str,),
            "repository_url": (str,),
        }

    attribute_map = {
        "branch": "branch",
        "repository_id": "repository_id",
        "repository_url": "repository_url",
    }

    def __init__(
        self_,
        branch: str,
        repository_id: Union[str, UnsetType] = unset,
        repository_url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for requesting code coverage summary for a branch.

        :param branch: The branch name.
        :type branch: str

        :param repository_id: Deprecated: use ``repository_url`` instead. The repository URL. **Deprecated**.
        :type repository_id: str, optional

        :param repository_url: The repository URL. Accepts a full URL with or without a scheme (for example, ``https://github.com/org/repo`` or ``github.com/org/repo`` ).
        :type repository_url: str, optional
        """
        if repository_id is not unset:
            kwargs["repository_id"] = repository_id
        if repository_url is not unset:
            kwargs["repository_url"] = repository_url
        super().__init__(kwargs)

        self_.branch = branch
