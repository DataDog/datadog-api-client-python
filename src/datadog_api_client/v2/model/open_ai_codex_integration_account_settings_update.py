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


class OpenAICodexIntegrationAccountSettingsUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "codex_workspace_id": (str,),
        }

    attribute_map = {
        "codex_workspace_id": "codex_workspace_id",
    }

    def __init__(self_, codex_workspace_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Settings for updating the OpenAI Codex integration account. Only the fields provided are changed.

        :param codex_workspace_id: ID of the Codex workspace to collect data from.
        :type codex_workspace_id: str, optional
        """
        if codex_workspace_id is not unset:
            kwargs["codex_workspace_id"] = codex_workspace_id
        super().__init__(kwargs)
