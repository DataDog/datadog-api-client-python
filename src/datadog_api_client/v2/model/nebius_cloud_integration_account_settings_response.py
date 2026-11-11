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


class NebiusCloudIntegrationAccountSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_tags": ([str],),
            "tenant_id": (str,),
        }

    attribute_map = {
        "account_tags": "account_tags",
        "tenant_id": "tenant_id",
    }

    def __init__(self_, tenant_id: str, account_tags: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Settings configured on the Nebius Cloud integration account.

        :param account_tags: Tags applied to all data collected from this Nebius Cloud account.
        :type account_tags: [str], optional

        :param tenant_id: ID of the Nebius tenant being monitored.
        :type tenant_id: str
        """
        if account_tags is not unset:
            kwargs["account_tags"] = account_tags
        super().__init__(kwargs)

        self_.tenant_id = tenant_id
