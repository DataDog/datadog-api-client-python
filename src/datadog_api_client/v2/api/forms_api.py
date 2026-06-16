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
from datadog_api_client.v2.model.forms_response import FormsResponse
from datadog_api_client.v2.model.form_response import FormResponse
from datadog_api_client.v2.model.create_form_request import CreateFormRequest
from datadog_api_client.v2.model.delete_form_response import DeleteFormResponse
from datadog_api_client.v2.model.update_form_request import UpdateFormRequest
from datadog_api_client.v2.model.clone_form_request import CloneFormRequest
from datadog_api_client.v2.model.form_publication_response import FormPublicationResponse
from datadog_api_client.v2.model.publish_form_request import PublishFormRequest
from datadog_api_client.v2.model.form_version_response import FormVersionResponse
from datadog_api_client.v2.model.upsert_form_version_request import UpsertFormVersionRequest
from datadog_api_client.v2.model.upsert_and_publish_form_version_request import UpsertAndPublishFormVersionRequest


class FormsApi:
    """
    The Datadog Forms API lets you create and manage forms within the App Builder platform.
    You can configure form settings, manage versions, and publish forms.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._clone_form_endpoint = _Endpoint(
            settings={
                "response_type": (FormResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms/{form_id}/clone",
                "operation_id": "clone_form",
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
                    "openapi_types": (CloneFormRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

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
                    "openapi_types": (CreateFormRequest,),
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
                    "openapi_types": (CreateFormRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_form_endpoint = _Endpoint(
            settings={
                "response_type": (DeleteFormResponse,),
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
                "accept": ["application/json"],
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
                    "openapi_types": (str,),
                    "attribute": "version",
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
                "response_type": (FormsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/forms",
                "operation_id": "list_forms",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={},
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
                    "openapi_types": (PublishFormRequest,),
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
                    "openapi_types": (UpdateFormRequest,),
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
                    "openapi_types": (UpsertAndPublishFormVersionRequest,),
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
                    "openapi_types": (UpsertFormVersionRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def clone_form(
        self,
        form_id: UUID,
        body: CloneFormRequest,
    ) -> FormResponse:
        """Clone a form.

        Clone an existing form. The clone is created in draft mode using the source form's latest version.

        :param form_id: The ID of the form to clone.
        :type form_id: UUID
        :type body: CloneFormRequest
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        kwargs["body"] = body

        return self._clone_form_endpoint.call_with_http_info(**kwargs)

    def create_and_publish_form(
        self,
        body: CreateFormRequest,
    ) -> FormResponse:
        """Create and publish a form.

        Creates a new form and immediately publishes its initial version. This also creates a new datastore for form responses and links it to the form.

        :type body: CreateFormRequest
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_and_publish_form_endpoint.call_with_http_info(**kwargs)

    def create_form(
        self,
        body: CreateFormRequest,
    ) -> FormResponse:
        """Create a form.

        Create a new form. The form is created in draft mode and must be published before it can be used. This also creates a new datastore for form responses and links it to the form.

        :type body: CreateFormRequest
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_form_endpoint.call_with_http_info(**kwargs)

    def delete_form(
        self,
        form_id: UUID,
    ) -> DeleteFormResponse:
        """Delete a form.

        Delete a form by its ID. This will also try to delete the associated datastore.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :rtype: DeleteFormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        return self._delete_form_endpoint.call_with_http_info(**kwargs)

    def get_form(
        self,
        form_id: UUID,
        *,
        version: Union[str, UnsetType] = unset,
    ) -> FormResponse:
        """Get a form.

        Get a form definition by its ID.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :param version: The version of the form to retrieve. Use 'latest' for the most recent draft, 'published' for the last published version, or a specific version number.
        :type version: str, optional
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        if version is not unset:
            kwargs["version"] = version

        return self._get_form_endpoint.call_with_http_info(**kwargs)

    def list_forms(
        self,
    ) -> FormsResponse:
        """List forms.

        Get all forms for the authenticated user's organization.

        :rtype: FormsResponse
        """
        kwargs: Dict[str, Any] = {}
        return self._list_forms_endpoint.call_with_http_info(**kwargs)

    def publish_form(
        self,
        form_id: UUID,
        body: PublishFormRequest,
    ) -> FormPublicationResponse:
        """Publish a form version.

        Publish a specific version of a form, making it available for submissions.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :type body: PublishFormRequest
        :rtype: FormPublicationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        kwargs["body"] = body

        return self._publish_form_endpoint.call_with_http_info(**kwargs)

    def update_form(
        self,
        form_id: UUID,
        body: UpdateFormRequest,
    ) -> FormResponse:
        """Update a form.

        Update a form's properties such as its name, description, or datastore configuration.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :type body: UpdateFormRequest
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        kwargs["body"] = body

        return self._update_form_endpoint.call_with_http_info(**kwargs)

    def upsert_and_publish_form_version(
        self,
        form_id: UUID,
        body: UpsertAndPublishFormVersionRequest,
    ) -> FormResponse:
        """Upsert and publish a form version.

        Upsert the latest form version and publish it in a single atomic transaction.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :type body: UpsertAndPublishFormVersionRequest
        :rtype: FormResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        kwargs["body"] = body

        return self._upsert_and_publish_form_version_endpoint.call_with_http_info(**kwargs)

    def upsert_form_version(
        self,
        form_id: UUID,
        body: UpsertFormVersionRequest,
    ) -> FormVersionResponse:
        """Create or update a form version.

        Create or update the latest draft version of a form. The ``upsert_params`` field controls
        optimistic concurrency behavior.

        :param form_id: The ID of the form.
        :type form_id: UUID
        :type body: UpsertFormVersionRequest
        :rtype: FormVersionResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["form_id"] = form_id

        kwargs["body"] = body

        return self._upsert_form_version_endpoint.call_with_http_info(**kwargs)
