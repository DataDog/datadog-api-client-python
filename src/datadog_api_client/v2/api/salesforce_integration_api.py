# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.model.salesforce_incidents_templates_response import SalesforceIncidentsTemplatesResponse
from datadog_api_client.v2.model.salesforce_incidents_template_response import SalesforceIncidentsTemplateResponse
from datadog_api_client.v2.model.salesforce_incidents_template_create_request import (
    SalesforceIncidentsTemplateCreateRequest,
)
from datadog_api_client.v2.model.salesforce_incidents_template_update_request import (
    SalesforceIncidentsTemplateUpdateRequest,
)
from datadog_api_client.v2.model.salesforce_incidents_organizations_response import (
    SalesforceIncidentsOrganizationsResponse,
)


class SalesforceIntegrationApi:
    """
    Configure your `Datadog Salesforce integration <https://docs.datadoghq.com/integrations/salesforce/>`_
    directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_incident_template_endpoint = _Endpoint(
            settings={
                "response_type": (SalesforceIncidentsTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/salesforce-incidents/incident-templates",
                "operation_id": "create_incident_template",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (SalesforceIncidentsTemplateCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_incident_template_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/salesforce-incidents/incident-templates/{incident_template_id}",
                "operation_id": "delete_incident_template",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "incident_template_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_template_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_salesforce_organization_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/salesforce-incidents/organizations/{salesforce_org_id}",
                "operation_id": "delete_salesforce_organization",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "salesforce_org_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "salesforce_org_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_incident_templates_endpoint = _Endpoint(
            settings={
                "response_type": (SalesforceIncidentsTemplatesResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/salesforce-incidents/incident-templates",
                "operation_id": "get_incident_templates",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_salesforce_organizations_endpoint = _Endpoint(
            settings={
                "response_type": (SalesforceIncidentsOrganizationsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/salesforce-incidents/organizations",
                "operation_id": "get_salesforce_organizations",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_incident_template_endpoint = _Endpoint(
            settings={
                "response_type": (SalesforceIncidentsTemplateResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/integration/salesforce-incidents/incident-templates/{incident_template_id}",
                "operation_id": "update_incident_template",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "incident_template_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "incident_template_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (SalesforceIncidentsTemplateUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_incident_template(
        self,
        body: SalesforceIncidentsTemplateCreateRequest,
    ) -> SalesforceIncidentsTemplateResponse:
        """Create a Salesforce incident template.

        Create a new Salesforce incident template for your organization. Template
        names must be unique within an organization.

        :param body: Salesforce incident template payload.
        :type body: SalesforceIncidentsTemplateCreateRequest
        :rtype: SalesforceIncidentsTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_incident_template_endpoint.call_with_http_info(**kwargs)

    def delete_incident_template(
        self,
        incident_template_id: str,
    ) -> None:
        """Delete a Salesforce incident template.

        Delete a single Salesforce incident template from your organization.

        :param incident_template_id: The ID of the Salesforce incident template.
        :type incident_template_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_template_id"] = incident_template_id

        return self._delete_incident_template_endpoint.call_with_http_info(**kwargs)

    def delete_salesforce_organization(
        self,
        salesforce_org_id: str,
    ) -> None:
        """Delete a connected Salesforce organization.

        Disconnect a Salesforce organization from your Datadog organization.
        This also deletes any incident templates referencing the organization.

        :param salesforce_org_id: The Datadog-assigned ID of the connected Salesforce organization.
        :type salesforce_org_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["salesforce_org_id"] = salesforce_org_id

        return self._delete_salesforce_organization_endpoint.call_with_http_info(**kwargs)

    def get_incident_templates(
        self,
    ) -> SalesforceIncidentsTemplatesResponse:
        """Get all Salesforce incident templates.

        Get all Salesforce incident templates configured for your organization.

        :rtype: SalesforceIncidentsTemplatesResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_incident_templates_endpoint.call_with_http_info(**kwargs)

    def get_salesforce_organizations(
        self,
    ) -> SalesforceIncidentsOrganizationsResponse:
        """Get all connected Salesforce organizations.

        Get all Salesforce organizations connected to your Datadog organization
        through the Salesforce integration. Salesforce organizations are connected
        through the OAuth setup flow in the Datadog Salesforce integration page.

        :rtype: SalesforceIncidentsOrganizationsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._get_salesforce_organizations_endpoint.call_with_http_info(**kwargs)

    def update_incident_template(
        self,
        incident_template_id: str,
        body: SalesforceIncidentsTemplateUpdateRequest,
    ) -> SalesforceIncidentsTemplateResponse:
        """Update a Salesforce incident template.

        Update a single Salesforce incident template in your organization.

        :param incident_template_id: The ID of the Salesforce incident template.
        :type incident_template_id: str
        :param body: Salesforce incident template payload.
        :type body: SalesforceIncidentsTemplateUpdateRequest
        :rtype: SalesforceIncidentsTemplateResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["incident_template_id"] = incident_template_id

        kwargs["body"] = body

        return self._update_incident_template_endpoint.call_with_http_info(**kwargs)
