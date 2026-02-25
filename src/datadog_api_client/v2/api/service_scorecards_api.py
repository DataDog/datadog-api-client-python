# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

import collections
from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    set_attribute_from_path,
    get_attribute_from_path,
    UnsetType,
    unset,
)
from datadog_api_client.v2.model.list_campaigns_response import ListCampaignsResponse
from datadog_api_client.v2.model.campaign_response import CampaignResponse
from datadog_api_client.v2.model.create_campaign_request import CreateCampaignRequest
from datadog_api_client.v2.model.update_campaign_request import UpdateCampaignRequest
from datadog_api_client.v2.model.generate_campaign_team_reports_request import GenerateCampaignTeamReportsRequest
from datadog_api_client.v2.model.generate_campaign_report_request import GenerateCampaignReportRequest
from datadog_api_client.v2.model.list_default_rules_response import ListDefaultRulesResponse
from datadog_api_client.v2.model.list_facets_response import ListFacetsResponse
from datadog_api_client.v2.model.outcomes_response import OutcomesResponse
from datadog_api_client.v2.model.outcomes_response_data_item import OutcomesResponseDataItem
from datadog_api_client.v2.model.update_outcomes_async_request import UpdateOutcomesAsyncRequest
from datadog_api_client.v2.model.outcomes_batch_response import OutcomesBatchResponse
from datadog_api_client.v2.model.outcomes_batch_request import OutcomesBatchRequest
from datadog_api_client.v2.model.list_rules_response import ListRulesResponse
from datadog_api_client.v2.model.list_rules_response_data_item import ListRulesResponseDataItem
from datadog_api_client.v2.model.create_rule_response import CreateRuleResponse
from datadog_api_client.v2.model.create_rule_request import CreateRuleRequest
from datadog_api_client.v2.model.update_rule_response import UpdateRuleResponse
from datadog_api_client.v2.model.update_rule_request import UpdateRuleRequest
from datadog_api_client.v2.model.list_scorecards_response import ListScorecardsResponse
from datadog_api_client.v2.model.list_scores_response import ListScoresResponse
from datadog_api_client.v2.model.setup_rules_request import SetupRulesRequest


class ServiceScorecardsApi:
    """
    API to create and update scorecard rules and outcomes. See `Service Scorecards <https://docs.datadoghq.com/service_catalog/scorecards>`_ for more information.

    This feature is currently in BETA. If you have any feedback, contact `Datadog support <https://docs.datadoghq.com/help/>`_.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_scorecard_campaign_endpoint = _Endpoint(
            settings={
                "response_type": (CampaignResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/campaigns",
                "operation_id": "create_scorecard_campaign",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateCampaignRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_scorecard_outcomes_batch_endpoint = _Endpoint(
            settings={
                "response_type": (OutcomesBatchResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/outcomes/batch",
                "operation_id": "create_scorecard_outcomes_batch",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (OutcomesBatchRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_scorecard_rule_endpoint = _Endpoint(
            settings={
                "response_type": (CreateRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/rules",
                "operation_id": "create_scorecard_rule",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (CreateRuleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_scorecard_campaign_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/campaigns/{campaign_id}",
                "operation_id": "delete_scorecard_campaign",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "campaign_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "campaign_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_scorecard_rule_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/rules/{rule_id}",
                "operation_id": "delete_scorecard_rule",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_scorecard_rule_workflow_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/rules/{rule_id}/workflow",
                "operation_id": "delete_scorecard_rule_workflow",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._generate_scorecard_campaign_report_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/campaigns/{campaign_id}/report",
                "operation_id": "generate_scorecard_campaign_report",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "campaign_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "campaign_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GenerateCampaignReportRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._generate_scorecard_campaign_team_reports_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/campaigns/{campaign_id}/entity-owner-report",
                "operation_id": "generate_scorecard_campaign_team_reports",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "campaign_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "campaign_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (GenerateCampaignTeamReportsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._get_scorecard_campaign_endpoint = _Endpoint(
            settings={
                "response_type": (CampaignResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/campaigns/{campaign_id}",
                "operation_id": "get_scorecard_campaign",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "campaign_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "campaign_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "include_meta": {
                    "openapi_types": (bool,),
                    "attribute": "include_meta",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_scorecard_campaigns_endpoint = _Endpoint(
            settings={
                "response_type": (ListCampaignsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/campaigns",
                "operation_id": "list_scorecard_campaigns",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "filter_campaign_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[campaign][name]",
                    "location": "query",
                },
                "filter_campaign_status": {
                    "openapi_types": (str,),
                    "attribute": "filter[campaign][status]",
                    "location": "query",
                },
                "filter_campaign_owner": {
                    "openapi_types": (str,),
                    "attribute": "filter[campaign][owner]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_scorecard_default_rules_endpoint = _Endpoint(
            settings={
                "response_type": (ListDefaultRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/default-rules",
                "operation_id": "list_scorecard_default_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_scorecard_facets_endpoint = _Endpoint(
            settings={
                "response_type": (ListFacetsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/facets",
                "operation_id": "list_scorecard_facets",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_entity_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[entity][query]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_scorecard_outcomes_endpoint = _Endpoint(
            settings={
                "response_type": (OutcomesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/outcomes",
                "operation_id": "list_scorecard_outcomes",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "fields_outcome": {
                    "openapi_types": (str,),
                    "attribute": "fields[outcome]",
                    "location": "query",
                },
                "fields_rule": {
                    "openapi_types": (str,),
                    "attribute": "fields[rule]",
                    "location": "query",
                },
                "filter_outcome_service_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[outcome][service_name]",
                    "location": "query",
                },
                "filter_outcome_state": {
                    "openapi_types": (str,),
                    "attribute": "filter[outcome][state]",
                    "location": "query",
                },
                "filter_rule_enabled": {
                    "openapi_types": (bool,),
                    "attribute": "filter[rule][enabled]",
                    "location": "query",
                },
                "filter_rule_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][id]",
                    "location": "query",
                },
                "filter_rule_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][name]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_scorecard_rules_endpoint = _Endpoint(
            settings={
                "response_type": (ListRulesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/rules",
                "operation_id": "list_scorecard_rules",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "filter_rule_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][id]",
                    "location": "query",
                },
                "filter_rule_enabled": {
                    "openapi_types": (bool,),
                    "attribute": "filter[rule][enabled]",
                    "location": "query",
                },
                "filter_rule_custom": {
                    "openapi_types": (bool,),
                    "attribute": "filter[rule][custom]",
                    "location": "query",
                },
                "filter_rule_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][name]",
                    "location": "query",
                },
                "filter_rule_description": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][description]",
                    "location": "query",
                },
                "fields_rule": {
                    "openapi_types": (str,),
                    "attribute": "fields[rule]",
                    "location": "query",
                },
                "fields_scorecard": {
                    "openapi_types": (str,),
                    "attribute": "fields[scorecard]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_scorecards_endpoint = _Endpoint(
            settings={
                "response_type": (ListScorecardsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/scorecards",
                "operation_id": "list_scorecards",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_size": {
                    "openapi_types": (int,),
                    "attribute": "page[size]",
                    "location": "query",
                },
                "filter_scorecard_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[scorecard][id]",
                    "location": "query",
                },
                "filter_scorecard_name": {
                    "openapi_types": (str,),
                    "attribute": "filter[scorecard][name]",
                    "location": "query",
                },
                "filter_scorecard_description": {
                    "openapi_types": (str,),
                    "attribute": "filter[scorecard][description]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_scorecard_scores_endpoint = _Endpoint(
            settings={
                "response_type": (ListScoresResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/scores/{aggregation}",
                "operation_id": "list_scorecard_scores",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "aggregation": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "aggregation",
                    "location": "path",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "filter_entity_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[entity][query]",
                    "location": "query",
                },
                "filter_rule_id": {
                    "openapi_types": (str,),
                    "attribute": "filter[rule][id]",
                    "location": "query",
                },
                "filter_rule_enabled": {
                    "openapi_types": (bool,),
                    "attribute": "filter[rule][enabled]",
                    "location": "query",
                },
                "filter_rule_custom": {
                    "openapi_types": (bool,),
                    "attribute": "filter[rule][custom]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._setup_scorecard_rules_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/setup",
                "operation_id": "setup_scorecard_rules",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SetupRulesRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_scorecard_campaign_endpoint = _Endpoint(
            settings={
                "response_type": (CampaignResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/campaigns/{campaign_id}",
                "operation_id": "update_scorecard_campaign",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "campaign_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "campaign_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateCampaignRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_scorecard_outcomes_async_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/outcomes",
                "operation_id": "update_scorecard_outcomes_async",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (UpdateOutcomesAsyncRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_scorecard_rule_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateRuleResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/rules/{rule_id}",
                "operation_id": "update_scorecard_rule",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (UpdateRuleRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_scorecard_rule_workflow_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/scorecard/rules/{rule_id}/workflow/{workflow_id}",
                "operation_id": "update_scorecard_rule_workflow",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "rule_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "rule_id",
                    "location": "path",
                },
                "workflow_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "workflow_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

    def create_scorecard_campaign(
        self,
        body: CreateCampaignRequest,
    ) -> CampaignResponse:
        """Create a new campaign.

        Creates a new scorecard campaign.

        :param body: Campaign data.
        :type body: CreateCampaignRequest
        :rtype: CampaignResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_scorecard_campaign_endpoint.call_with_http_info(**kwargs)

    def create_scorecard_outcomes_batch(
        self,
        body: OutcomesBatchRequest,
    ) -> OutcomesBatchResponse:
        """Create outcomes batch.

        Sets multiple service-rule outcomes in a single batched request.

        :param body: Set of scorecard outcomes.
        :type body: OutcomesBatchRequest
        :rtype: OutcomesBatchResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_scorecard_outcomes_batch_endpoint.call_with_http_info(**kwargs)

    def create_scorecard_rule(
        self,
        body: CreateRuleRequest,
    ) -> CreateRuleResponse:
        """Create a new rule.

        Creates a new rule.

        :param body: Rule attributes.
        :type body: CreateRuleRequest
        :rtype: CreateRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_scorecard_rule_endpoint.call_with_http_info(**kwargs)

    def delete_scorecard_campaign(
        self,
        campaign_id: str,
    ) -> None:
        """Delete a campaign.

        Deletes a single campaign by ID or key.

        :param campaign_id: Campaign ID or key.
        :type campaign_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["campaign_id"] = campaign_id

        return self._delete_scorecard_campaign_endpoint.call_with_http_info(**kwargs)

    def delete_scorecard_rule(
        self,
        rule_id: str,
    ) -> None:
        """Delete a rule.

        Deletes a single rule.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._delete_scorecard_rule_endpoint.call_with_http_info(**kwargs)

    def delete_scorecard_rule_workflow(
        self,
        rule_id: str,
    ) -> None:
        """Delete rule workflow.

        Removes workflow association from a scorecard rule.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        return self._delete_scorecard_rule_workflow_endpoint.call_with_http_info(**kwargs)

    def generate_scorecard_campaign_report(
        self,
        campaign_id: str,
        body: GenerateCampaignReportRequest,
    ) -> None:
        """Generate campaign report.

        Generates and sends a campaign report to Slack.

        :param campaign_id: Campaign ID.
        :type campaign_id: str
        :param body: Report generation request.
        :type body: GenerateCampaignReportRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["campaign_id"] = campaign_id

        kwargs["body"] = body

        return self._generate_scorecard_campaign_report_endpoint.call_with_http_info(**kwargs)

    def generate_scorecard_campaign_team_reports(
        self,
        campaign_id: str,
        body: GenerateCampaignTeamReportsRequest,
    ) -> None:
        """Generate team-specific campaign reports.

        Generates and sends team-specific campaign reports to Slack.

        :param campaign_id: Campaign ID.
        :type campaign_id: str
        :param body: Team report generation request.
        :type body: GenerateCampaignTeamReportsRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["campaign_id"] = campaign_id

        kwargs["body"] = body

        return self._generate_scorecard_campaign_team_reports_endpoint.call_with_http_info(**kwargs)

    def get_scorecard_campaign(
        self,
        campaign_id: str,
        *,
        include: Union[str, UnsetType] = unset,
        include_meta: Union[bool, UnsetType] = unset,
    ) -> CampaignResponse:
        """Get a campaign.

        Fetches a single campaign by ID or key.

        :param campaign_id: Campaign ID or key.
        :type campaign_id: str
        :param include: Include related data (for example, scores).
        :type include: str, optional
        :param include_meta: Include metadata (entity and rule counts).
        :type include_meta: bool, optional
        :rtype: CampaignResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["campaign_id"] = campaign_id

        if include is not unset:
            kwargs["include"] = include

        if include_meta is not unset:
            kwargs["include_meta"] = include_meta

        return self._get_scorecard_campaign_endpoint.call_with_http_info(**kwargs)

    def list_scorecard_campaigns(
        self,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        filter_campaign_name: Union[str, UnsetType] = unset,
        filter_campaign_status: Union[str, UnsetType] = unset,
        filter_campaign_owner: Union[str, UnsetType] = unset,
    ) -> ListCampaignsResponse:
        """List all campaigns.

        Fetches all scorecard campaigns.

        :param page_limit: Maximum number of campaigns to return.
        :type page_limit: int, optional
        :param page_offset: Offset for pagination.
        :type page_offset: int, optional
        :param filter_campaign_name: Filter campaigns by name (full-text search).
        :type filter_campaign_name: str, optional
        :param filter_campaign_status: Filter campaigns by status.
        :type filter_campaign_status: str, optional
        :param filter_campaign_owner: Filter campaigns by owner UUID.
        :type filter_campaign_owner: str, optional
        :rtype: ListCampaignsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if filter_campaign_name is not unset:
            kwargs["filter_campaign_name"] = filter_campaign_name

        if filter_campaign_status is not unset:
            kwargs["filter_campaign_status"] = filter_campaign_status

        if filter_campaign_owner is not unset:
            kwargs["filter_campaign_owner"] = filter_campaign_owner

        return self._list_scorecard_campaigns_endpoint.call_with_http_info(**kwargs)

    def list_scorecard_default_rules(
        self,
    ) -> ListDefaultRulesResponse:
        """List default rules.

        Fetches all default scorecard rules available for the organization.

        :rtype: ListDefaultRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_scorecard_default_rules_endpoint.call_with_http_info(**kwargs)

    def list_scorecard_facets(
        self,
        *,
        filter_entity_query: Union[str, UnsetType] = unset,
    ) -> ListFacetsResponse:
        """List entity facets.

        Fetches facets for scorecard entities with counts.

        :param filter_entity_query: Entity query filter.
        :type filter_entity_query: str, optional
        :rtype: ListFacetsResponse
        """
        kwargs: Dict[str, Any] = {}
        if filter_entity_query is not unset:
            kwargs["filter_entity_query"] = filter_entity_query

        return self._list_scorecard_facets_endpoint.call_with_http_info(**kwargs)

    def list_scorecard_outcomes(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        fields_outcome: Union[str, UnsetType] = unset,
        fields_rule: Union[str, UnsetType] = unset,
        filter_outcome_service_name: Union[str, UnsetType] = unset,
        filter_outcome_state: Union[str, UnsetType] = unset,
        filter_rule_enabled: Union[bool, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_name: Union[str, UnsetType] = unset,
    ) -> OutcomesResponse:
        """List all rule outcomes.

        Fetches all rule outcomes.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param include: Include related rule details in the response.
        :type include: str, optional
        :param fields_outcome: Return only specified values in the outcome attributes.
        :type fields_outcome: str, optional
        :param fields_rule: Return only specified values in the included rule details.
        :type fields_rule: str, optional
        :param filter_outcome_service_name: Filter outcomes on a specific service name.
        :type filter_outcome_service_name: str, optional
        :param filter_outcome_state: Filter outcomes by a specific state.
        :type filter_outcome_state: str, optional
        :param filter_rule_enabled: Filter outcomes based on whether a rule is enabled or disabled.
        :type filter_rule_enabled: bool, optional
        :param filter_rule_id: Filter outcomes based on rule ID.
        :type filter_rule_id: str, optional
        :param filter_rule_name: Filter outcomes based on rule name.
        :type filter_rule_name: str, optional
        :rtype: OutcomesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if include is not unset:
            kwargs["include"] = include

        if fields_outcome is not unset:
            kwargs["fields_outcome"] = fields_outcome

        if fields_rule is not unset:
            kwargs["fields_rule"] = fields_rule

        if filter_outcome_service_name is not unset:
            kwargs["filter_outcome_service_name"] = filter_outcome_service_name

        if filter_outcome_state is not unset:
            kwargs["filter_outcome_state"] = filter_outcome_state

        if filter_rule_enabled is not unset:
            kwargs["filter_rule_enabled"] = filter_rule_enabled

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_name is not unset:
            kwargs["filter_rule_name"] = filter_rule_name

        return self._list_scorecard_outcomes_endpoint.call_with_http_info(**kwargs)

    def list_scorecard_outcomes_with_pagination(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        fields_outcome: Union[str, UnsetType] = unset,
        fields_rule: Union[str, UnsetType] = unset,
        filter_outcome_service_name: Union[str, UnsetType] = unset,
        filter_outcome_state: Union[str, UnsetType] = unset,
        filter_rule_enabled: Union[bool, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_name: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[OutcomesResponseDataItem]:
        """List all rule outcomes.

        Provide a paginated version of :meth:`list_scorecard_outcomes`, returning all items.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param include: Include related rule details in the response.
        :type include: str, optional
        :param fields_outcome: Return only specified values in the outcome attributes.
        :type fields_outcome: str, optional
        :param fields_rule: Return only specified values in the included rule details.
        :type fields_rule: str, optional
        :param filter_outcome_service_name: Filter outcomes on a specific service name.
        :type filter_outcome_service_name: str, optional
        :param filter_outcome_state: Filter outcomes by a specific state.
        :type filter_outcome_state: str, optional
        :param filter_rule_enabled: Filter outcomes based on whether a rule is enabled or disabled.
        :type filter_rule_enabled: bool, optional
        :param filter_rule_id: Filter outcomes based on rule ID.
        :type filter_rule_id: str, optional
        :param filter_rule_name: Filter outcomes based on rule name.
        :type filter_rule_name: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[OutcomesResponseDataItem]
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if include is not unset:
            kwargs["include"] = include

        if fields_outcome is not unset:
            kwargs["fields_outcome"] = fields_outcome

        if fields_rule is not unset:
            kwargs["fields_rule"] = fields_rule

        if filter_outcome_service_name is not unset:
            kwargs["filter_outcome_service_name"] = filter_outcome_service_name

        if filter_outcome_state is not unset:
            kwargs["filter_outcome_state"] = filter_outcome_state

        if filter_rule_enabled is not unset:
            kwargs["filter_rule_enabled"] = filter_rule_enabled

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_name is not unset:
            kwargs["filter_rule_name"] = filter_rule_name

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_scorecard_outcomes_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_scorecard_rules(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_enabled: Union[bool, UnsetType] = unset,
        filter_rule_custom: Union[bool, UnsetType] = unset,
        filter_rule_name: Union[str, UnsetType] = unset,
        filter_rule_description: Union[str, UnsetType] = unset,
        fields_rule: Union[str, UnsetType] = unset,
        fields_scorecard: Union[str, UnsetType] = unset,
    ) -> ListRulesResponse:
        """List all rules.

        Fetch all rules.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param include: Include related scorecard details in the response.
        :type include: str, optional
        :param filter_rule_id: Filter the rules on a rule ID.
        :type filter_rule_id: str, optional
        :param filter_rule_enabled: Filter for enabled rules only.
        :type filter_rule_enabled: bool, optional
        :param filter_rule_custom: Filter for custom rules only.
        :type filter_rule_custom: bool, optional
        :param filter_rule_name: Filter rules on the rule name.
        :type filter_rule_name: str, optional
        :param filter_rule_description: Filter rules on the rule description.
        :type filter_rule_description: str, optional
        :param fields_rule: Return only specific fields in the response for rule attributes.
        :type fields_rule: str, optional
        :param fields_scorecard: Return only specific fields in the included response for scorecard attributes.
        :type fields_scorecard: str, optional
        :rtype: ListRulesResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if include is not unset:
            kwargs["include"] = include

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_enabled is not unset:
            kwargs["filter_rule_enabled"] = filter_rule_enabled

        if filter_rule_custom is not unset:
            kwargs["filter_rule_custom"] = filter_rule_custom

        if filter_rule_name is not unset:
            kwargs["filter_rule_name"] = filter_rule_name

        if filter_rule_description is not unset:
            kwargs["filter_rule_description"] = filter_rule_description

        if fields_rule is not unset:
            kwargs["fields_rule"] = fields_rule

        if fields_scorecard is not unset:
            kwargs["fields_scorecard"] = fields_scorecard

        return self._list_scorecard_rules_endpoint.call_with_http_info(**kwargs)

    def list_scorecard_rules_with_pagination(
        self,
        *,
        page_size: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        include: Union[str, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_enabled: Union[bool, UnsetType] = unset,
        filter_rule_custom: Union[bool, UnsetType] = unset,
        filter_rule_name: Union[str, UnsetType] = unset,
        filter_rule_description: Union[str, UnsetType] = unset,
        fields_rule: Union[str, UnsetType] = unset,
        fields_scorecard: Union[str, UnsetType] = unset,
    ) -> collections.abc.Iterable[ListRulesResponseDataItem]:
        """List all rules.

        Provide a paginated version of :meth:`list_scorecard_rules`, returning all items.

        :param page_size: Size for a given page. The maximum allowed value is 100.
        :type page_size: int, optional
        :param page_offset: Specific offset to use as the beginning of the returned page.
        :type page_offset: int, optional
        :param include: Include related scorecard details in the response.
        :type include: str, optional
        :param filter_rule_id: Filter the rules on a rule ID.
        :type filter_rule_id: str, optional
        :param filter_rule_enabled: Filter for enabled rules only.
        :type filter_rule_enabled: bool, optional
        :param filter_rule_custom: Filter for custom rules only.
        :type filter_rule_custom: bool, optional
        :param filter_rule_name: Filter rules on the rule name.
        :type filter_rule_name: str, optional
        :param filter_rule_description: Filter rules on the rule description.
        :type filter_rule_description: str, optional
        :param fields_rule: Return only specific fields in the response for rule attributes.
        :type fields_rule: str, optional
        :param fields_scorecard: Return only specific fields in the included response for scorecard attributes.
        :type fields_scorecard: str, optional

        :return: A generator of paginated results.
        :rtype: collections.abc.Iterable[ListRulesResponseDataItem]
        """
        kwargs: Dict[str, Any] = {}
        if page_size is not unset:
            kwargs["page_size"] = page_size

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if include is not unset:
            kwargs["include"] = include

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_enabled is not unset:
            kwargs["filter_rule_enabled"] = filter_rule_enabled

        if filter_rule_custom is not unset:
            kwargs["filter_rule_custom"] = filter_rule_custom

        if filter_rule_name is not unset:
            kwargs["filter_rule_name"] = filter_rule_name

        if filter_rule_description is not unset:
            kwargs["filter_rule_description"] = filter_rule_description

        if fields_rule is not unset:
            kwargs["fields_rule"] = fields_rule

        if fields_scorecard is not unset:
            kwargs["fields_scorecard"] = fields_scorecard

        local_page_size = get_attribute_from_path(kwargs, "page_size", 10)
        endpoint = self._list_scorecard_rules_endpoint
        set_attribute_from_path(kwargs, "page_size", local_page_size, endpoint.params_map)
        pagination = {
            "limit_value": local_page_size,
            "results_path": "data",
            "page_offset_param": "page_offset",
            "endpoint": endpoint,
            "kwargs": kwargs,
        }
        return endpoint.call_with_http_info_paginated(pagination)

    def list_scorecards(
        self,
        *,
        page_offset: Union[int, UnsetType] = unset,
        page_size: Union[int, UnsetType] = unset,
        filter_scorecard_id: Union[str, UnsetType] = unset,
        filter_scorecard_name: Union[str, UnsetType] = unset,
        filter_scorecard_description: Union[str, UnsetType] = unset,
    ) -> ListScorecardsResponse:
        """List all scorecards.

        Fetches all scorecards.

        :param page_offset: Offset for pagination.
        :type page_offset: int, optional
        :param page_size: Maximum number of scorecards to return.
        :type page_size: int, optional
        :param filter_scorecard_id: Filter by scorecard ID.
        :type filter_scorecard_id: str, optional
        :param filter_scorecard_name: Filter by scorecard name (partial match).
        :type filter_scorecard_name: str, optional
        :param filter_scorecard_description: Filter by scorecard description (partial match).
        :type filter_scorecard_description: str, optional
        :rtype: ListScorecardsResponse
        """
        kwargs: Dict[str, Any] = {}
        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_size is not unset:
            kwargs["page_size"] = page_size

        if filter_scorecard_id is not unset:
            kwargs["filter_scorecard_id"] = filter_scorecard_id

        if filter_scorecard_name is not unset:
            kwargs["filter_scorecard_name"] = filter_scorecard_name

        if filter_scorecard_description is not unset:
            kwargs["filter_scorecard_description"] = filter_scorecard_description

        return self._list_scorecards_endpoint.call_with_http_info(**kwargs)

    def list_scorecard_scores(
        self,
        aggregation: str,
        *,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        filter_entity_query: Union[str, UnsetType] = unset,
        filter_rule_id: Union[str, UnsetType] = unset,
        filter_rule_enabled: Union[bool, UnsetType] = unset,
        filter_rule_custom: Union[bool, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
    ) -> ListScoresResponse:
        """List scores by aggregation.

        Fetches scorecard scores aggregated by entity, rule, scorecard, service, or team.

        :param aggregation: Aggregation type (by-entity, by-rule, by-scorecard, by-service, by-team).
        :type aggregation: str
        :param page_limit: Maximum number of scores to return.
        :type page_limit: int, optional
        :param page_offset: Offset for pagination.
        :type page_offset: int, optional
        :param filter_entity_query: Entity query filter.
        :type filter_entity_query: str, optional
        :param filter_rule_id: Filter by rule IDs (comma-separated).
        :type filter_rule_id: str, optional
        :param filter_rule_enabled: Filter by rule enabled status.
        :type filter_rule_enabled: bool, optional
        :param filter_rule_custom: Filter by custom rules.
        :type filter_rule_custom: bool, optional
        :param sort: Sort order (comma-separated list of fields; prefix a field with - for descending order).
        :type sort: str, optional
        :rtype: ListScoresResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["aggregation"] = aggregation

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if filter_entity_query is not unset:
            kwargs["filter_entity_query"] = filter_entity_query

        if filter_rule_id is not unset:
            kwargs["filter_rule_id"] = filter_rule_id

        if filter_rule_enabled is not unset:
            kwargs["filter_rule_enabled"] = filter_rule_enabled

        if filter_rule_custom is not unset:
            kwargs["filter_rule_custom"] = filter_rule_custom

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_scorecard_scores_endpoint.call_with_http_info(**kwargs)

    def setup_scorecard_rules(
        self,
        body: SetupRulesRequest,
    ) -> None:
        """Set up rules for organization.

        Sets up default scorecard rules for the organization.

        :param body: Setup rules request.
        :type body: SetupRulesRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._setup_scorecard_rules_endpoint.call_with_http_info(**kwargs)

    def update_scorecard_campaign(
        self,
        campaign_id: str,
        body: UpdateCampaignRequest,
    ) -> CampaignResponse:
        """Update a campaign.

        Updates an existing campaign.

        :param campaign_id: Campaign ID or key.
        :type campaign_id: str
        :param body: Campaign data.
        :type body: UpdateCampaignRequest
        :rtype: CampaignResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["campaign_id"] = campaign_id

        kwargs["body"] = body

        return self._update_scorecard_campaign_endpoint.call_with_http_info(**kwargs)

    def update_scorecard_outcomes_async(
        self,
        body: UpdateOutcomesAsyncRequest,
    ) -> None:
        """Update Scorecard outcomes asynchronously.

        Updates multiple scorecard rule outcomes in a single batched request.

        :param body: Set of scorecard outcomes.
        :type body: UpdateOutcomesAsyncRequest
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._update_scorecard_outcomes_async_endpoint.call_with_http_info(**kwargs)

    def update_scorecard_rule(
        self,
        rule_id: str,
        body: UpdateRuleRequest,
    ) -> UpdateRuleResponse:
        """Update an existing rule.

        Updates an existing rule.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :param body: Rule attributes.
        :type body: UpdateRuleRequest
        :rtype: UpdateRuleResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["body"] = body

        return self._update_scorecard_rule_endpoint.call_with_http_info(**kwargs)

    def update_scorecard_rule_workflow(
        self,
        rule_id: str,
        workflow_id: str,
    ) -> None:
        """Associate workflow with rule.

        Associates a workflow with a scorecard rule.

        :param rule_id: The ID of the rule.
        :type rule_id: str
        :param workflow_id: Workflow ID.
        :type workflow_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["rule_id"] = rule_id

        kwargs["workflow_id"] = workflow_id

        return self._update_scorecard_rule_workflow_endpoint.call_with_http_info(**kwargs)
