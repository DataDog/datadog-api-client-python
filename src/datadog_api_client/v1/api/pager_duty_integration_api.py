# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v1.model.pager_duty_service_name import PagerDutyServiceName
from datadog_api_client.v1.model.pager_duty_service import PagerDutyService
from datadog_api_client.v1.model.pager_duty_service_key import PagerDutyServiceKey


class PagerDutyIntegrationApi:
    """
    Configure your `Datadog-PagerDuty integration <https://docs.datadoghq.com/api/?lang=bash#integration-pagerduty>`_
    directly through the Datadog API.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_pager_duty_integration_service_endpoint = _Endpoint(
            settings={
                "response_type": (PagerDutyServiceName,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/pagerduty/configuration/services",
                "operation_id": "create_pager_duty_integration_service",
                "http_method": "POST",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (PagerDutyService,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_pager_duty_integration_service_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/pagerduty/configuration/services/{service_name}",
                "operation_id": "delete_pager_duty_integration_service",
                "http_method": "DELETE",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "service_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_pager_duty_integration_service_endpoint = _Endpoint(
            settings={
                "response_type": (PagerDutyServiceName,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/pagerduty/configuration/services/{service_name}",
                "operation_id": "get_pager_duty_integration_service",
                "http_method": "GET",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "service_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service_name",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._update_pager_duty_integration_service_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v1/integration/pagerduty/configuration/services/{service_name}",
                "operation_id": "update_pager_duty_integration_service",
                "http_method": "PUT",
                "version": "v1",
                "servers": None,
            },
            params_map={
                "service_name": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "service_name",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (PagerDutyServiceKey,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_pager_duty_integration_service(self, body, **kwargs):
        """Create a new service object.

        Create a new service object in the PagerDuty integration.

        :param body: Create a new service object request body.
        :type body: PagerDutyService

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: PagerDutyServiceName
        """
        kwargs["body"] = body

        return self._create_pager_duty_integration_service_endpoint.call_with_http_info(**kwargs)

    def delete_pager_duty_integration_service(self, service_name, **kwargs):
        """Delete a single service object.

        Delete a single service object in the Datadog-PagerDuty integration.

        :param service_name: The service name
        :type service_name: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: None
        """
        kwargs["service_name"] = service_name

        return self._delete_pager_duty_integration_service_endpoint.call_with_http_info(**kwargs)

    def get_pager_duty_integration_service(self, service_name, **kwargs):
        """Get a single service object.

        Get service name in the Datadog-PagerDuty integration.

        :param service_name: The service name.
        :type service_name: str

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: PagerDutyServiceName
        """
        kwargs["service_name"] = service_name

        return self._get_pager_duty_integration_service_endpoint.call_with_http_info(**kwargs)

    def update_pager_duty_integration_service(self, service_name, body, **kwargs):
        """Update a single service object.

        Update a single service object in the Datadog-PagerDuty integration.

        :param service_name: The service name
        :type service_name: str
        :param body: Update an existing service object request body.
        :type body: PagerDutyServiceKey

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: None
        """
        kwargs["service_name"] = service_name

        kwargs["body"] = body

        return self._update_pager_duty_integration_service_endpoint.call_with_http_info(**kwargs)
