# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.forms_list_response import FormsListResponse
from datadog_api_client.v2.model.form_response import FormResponse
from datadog_api_client.v2.model.form_create_request import FormCreateRequest
from datadog_api_client.v2.model.form_update_request import FormUpdateRequest
from datadog_api_client.v2.model.form_publication_response import FormPublicationResponse
from datadog_api_client.v2.model.form_publication_request import FormPublicationRequest
from datadog_api_client.v2.model.form_submission_response import FormSubmissionResponse
from datadog_api_client.v2.model.form_submission_request import FormSubmissionRequest
from datadog_api_client.v2.model.form_version_response import FormVersionResponse
from datadog_api_client.v2.model.form_version_request import FormVersionRequest


class FormsApi:
    """
    Create and manage forms for collecting data from users.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._create_and_publish_form_endpoint = _Endpoint(
            settings={
                "response_type": (FormResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms/create_and_publish",
                "operation_id": "create_and_publish_form",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FormCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_form_endpoint = _Endpoint(
            settings={
                "response_type": (FormResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms",
                "operation_id": "create_form",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (FormCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_form_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms/{form_id}",
                "operation_id": "delete_form",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "form_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "form_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_form_endpoint = _Endpoint(
            settings={
                "response_type": (FormResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms/{form_id}",
                "operation_id": "get_form",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "form_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "form_id",
                    "location": "path",
                },
                "version": {
                    "openapi_types": (int,),
                    "attribute": "version",
                    "location": "query",
                },
                "published_version": {
                    "openapi_types": (bool,),
                    "attribute": "published_version",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_forms_endpoint = _Endpoint(
            settings={
                "response_type": (FormsListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms",
                "operation_id": "list_forms",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "name": {
                    "openapi_types": (str,),
                    "attribute": "name",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._publish_form_endpoint = _Endpoint(
            settings={
                "response_type": (FormPublicationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms/{form_id}/publish",
                "operation_id": "publish_form",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "form_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "form_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (FormPublicationRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._submit_form_endpoint = _Endpoint(
            settings={
                "response_type": (FormSubmissionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms/{form_id}/submit",
                "operation_id": "submit_form",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "form_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "form_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (FormSubmissionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_form_endpoint = _Endpoint(
            settings={
                "response_type": (FormResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms/{form_id}",
                "operation_id": "update_form",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "form_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "form_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (FormUpdateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upsert_and_publish_form_version_endpoint = _Endpoint(
            settings={
                "response_type": (FormResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms/{form_id}/versions/upsert_and_publish",
                "operation_id": "upsert_and_publish_form_version",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "form_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "form_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (FormVersionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._upsert_form_version_endpoint = _Endpoint(
            settings={
                "response_type": (FormVersionResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms/{form_id}/versions",
                "operation_id": "upsert_form_version",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "form_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "form_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (FormVersionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_and_publish_form(
        self,
        body: FormCreateRequest,
    ) -> FormResponse:
        """Create and publish a form.

        Create a new form and publish it immediately.

        :type body: FormCreateRequest
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_and_publish_form_endpoint.call_with_http_info(**kwargs)

    def create_form(
        self,
        body: FormCreateRequest,
    ) -> FormResponse:
        """Create a new form.

        Create a new form with the specified configuration.

        :type body: FormCreateRequest
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_form_endpoint.call_with_http_info(**kwargs)

    def delete_form(
        self,
        form_id: UUID,
    ) -> None:
        """Delete a form.

        Delete a form by ID.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        return self._delete_form_endpoint.call_with_http_info(**kwargs)

    def get_form(
        self,
        form_id: UUID,
        *,
        version: Union[int, UnsetType] = unset,
        published_version: Union[bool, UnsetType] = unset,
    ) -> FormResponse:
        """Get a form.

        Get a form by ID.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :param version: The version number of the form.
        :type version: int, optional
        :param published_version: Whether to get the published version.
        :type published_version: bool, optional
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        if version is not unset:
            kwargs["version"] = version

        if published_version is not unset:
            kwargs["published_version"] = published_version

        return self._get_form_endpoint.call_with_http_info(**kwargs)

    def list_forms(
        self,
        *,
        name: Union[str, UnsetType] = unset,
    ) -> FormsListResponse:
        """List all forms.

        Get a list of all forms.

        :param name: Filter forms by name.
        :type name: str, optional
        :rtype: FormsListResponse
        """
        kwargs: Dict[str, Any] = {}
        if name is not unset:
            kwargs["name"] = name

        return self._list_forms_endpoint.call_with_http_info(**kwargs)

    def publish_form(
        self,
        form_id: UUID,
        body: FormPublicationRequest,
    ) -> FormPublicationResponse:
        """Publish a form.

        Publish a specific version of a form.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :type body: FormPublicationRequest
        :rtype: FormPublicationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        kwargs["body"] = body

        return self._publish_form_endpoint.call_with_http_info(**kwargs)

    def submit_form(
        self,
        form_id: UUID,
        body: FormSubmissionRequest,
    ) -> FormSubmissionResponse:
        """Submit a form.

        Submit data to a form.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :type body: FormSubmissionRequest
        :rtype: FormSubmissionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        kwargs["body"] = body

        return self._submit_form_endpoint.call_with_http_info(**kwargs)

    def update_form(
        self,
        form_id: UUID,
        body: FormUpdateRequest,
    ) -> FormResponse:
        """Update a form.

        Update a form by ID.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :type body: FormUpdateRequest
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        kwargs["body"] = body

        return self._update_form_endpoint.call_with_http_info(**kwargs)

    def upsert_and_publish_form_version(
        self,
        form_id: UUID,
        body: FormVersionRequest,
    ) -> FormResponse:
        """Upsert and publish a form version.

        Create or update a form version and publish it immediately.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :type body: FormVersionRequest
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        kwargs["body"] = body

        return self._upsert_and_publish_form_version_endpoint.call_with_http_info(**kwargs)

    def upsert_form_version(
        self,
        form_id: UUID,
        body: FormVersionRequest,
    ) -> FormVersionResponse:
        """Create a form version.

        Create or update a form version.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :type body: FormVersionRequest
        :rtype: FormVersionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        kwargs["body"] = body

        return self._upsert_form_version_endpoint.call_with_http_info(**kwargs)
