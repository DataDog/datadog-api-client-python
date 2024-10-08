# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class IncidentIntegrationMetadataMetadata(ModelComposed):
    def __init__(self, **kwargs):
        """
        Incident integration metadata's metadata attribute.

        :param channels: Array of Slack channels in this integration metadata.
        :type channels: [SlackIntegrationMetadataChannelItem]

        :param issues: Array of Jira issues in this integration metadata.
        :type issues: [JiraIntegrationMetadataIssuesItem]

        :param teams: Array of Microsoft Teams in this integration metadata.
        :type teams: [MSTeamsIntegrationMetadataTeamsItem]
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.slack_integration_metadata import SlackIntegrationMetadata
        from datadog_api_client.v2.model.jira_integration_metadata import JiraIntegrationMetadata
        from datadog_api_client.v2.model.ms_teams_integration_metadata import MSTeamsIntegrationMetadata

        return {
            "oneOf": [
                SlackIntegrationMetadata,
                JiraIntegrationMetadata,
                MSTeamsIntegrationMetadata,
            ],
        }
