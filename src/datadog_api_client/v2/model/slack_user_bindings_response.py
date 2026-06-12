# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.slack_user_binding_data import SlackUserBindingData


class SlackUserBindingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.slack_user_binding_data import SlackUserBindingData

        return {
            "data": ([SlackUserBindingData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[SlackUserBindingData], **kwargs):
        """
        Response with a list of Slack user bindings.

        :param data: An array of Slack user bindings.
        :type data: [SlackUserBindingData]
        """
        super().__init__(kwargs)

        self_.data = data
