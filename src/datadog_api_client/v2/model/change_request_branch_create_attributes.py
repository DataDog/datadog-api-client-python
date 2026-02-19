# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ChangeRequestBranchCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "branch_name": (str,),
            "repo_id": (str,),
        }

    attribute_map = {
        "branch_name": "branch_name",
        "repo_id": "repo_id",
    }

    def __init__(self_, branch_name: str, repo_id: str, **kwargs):
        """
        Attributes for creating a change request branch.

        :param branch_name: The name of the branch to create.
        :type branch_name: str

        :param repo_id: The repository identifier in the format owner/repository.
        :type repo_id: str
        """
        super().__init__(kwargs)

        self_.branch_name = branch_name
        self_.repo_id = repo_id
