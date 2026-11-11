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


class ChatGPTEnterpriseIntegrationAccountSettingsUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "openai_org_id": (str,),
        }

    attribute_map = {
        "openai_org_id": "openai_org_id",
    }

    def __init__(self_, openai_org_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Settings for updating the ChatGPT Enterprise integration account. Only the fields provided are changed.

        :param openai_org_id: OpenAI API Platform organization ID ( ``org-...`` ) that the Costs API uses for your Enterprise usage. This is not the ChatGPT workspace UUID or your Datadog organization ID. A value that does not match ``^org-[A-Za-z0-9]+$`` is rejected with a ``422`` response.
        :type openai_org_id: str, optional
        """
        if openai_org_id is not unset:
            kwargs["openai_org_id"] = openai_org_id
        super().__init__(kwargs)
