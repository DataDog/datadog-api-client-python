# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GCPServiceAccountMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "accessible_projects": ([str],),
        }

    attribute_map = {
        "accessible_projects": "accessible_projects",
    }

    def __init__(self_, accessible_projects: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Additional information related to your service account.

        :param accessible_projects: The current list of projects accessible from your service account.
        :type accessible_projects: [str], optional
        """
        if accessible_projects is not unset:
            kwargs["accessible_projects"] = accessible_projects
        super().__init__(kwargs)
