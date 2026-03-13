# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.slack_routing_options import SlackRoutingOptions


class GenerateCampaignReportRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.slack_routing_options import SlackRoutingOptions

        return {
            "slack": (SlackRoutingOptions,),
        }

    attribute_map = {
        "slack": "slack",
    }

    def __init__(self_, slack: SlackRoutingOptions, **kwargs):
        """
        Attributes for generating a campaign report.

        :param slack: Slack routing options for report delivery.
        :type slack: SlackRoutingOptions
        """
        super().__init__(kwargs)

        self_.slack = slack
