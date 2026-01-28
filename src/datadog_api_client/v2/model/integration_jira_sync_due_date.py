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


class IntegrationJiraSyncDueDate(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "jira_field_id": (str,),
            "sync_type": (str,),
        }

    attribute_map = {
        "jira_field_id": "jira_field_id",
        "sync_type": "sync_type",
    }

    def __init__(
        self_, jira_field_id: Union[str, UnsetType] = unset, sync_type: Union[str, UnsetType] = unset, **kwargs
    ):
        """


        :param jira_field_id:
        :type jira_field_id: str, optional

        :param sync_type:
        :type sync_type: str, optional
        """
        if jira_field_id is not unset:
            kwargs["jira_field_id"] = jira_field_id
        if sync_type is not unset:
            kwargs["sync_type"] = sync_type
        super().__init__(kwargs)
