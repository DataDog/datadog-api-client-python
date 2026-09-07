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
)
from datadog_api_client.v2.model.dem_journey_response import DemJourneyResponse
from datadog_api_client.v2.model.dem_journey_create_request import DemJourneyCreateRequest
from datadog_api_client.v2.model.dem_search_inferred_journeys_response import DemSearchInferredJourneysResponse
from datadog_api_client.v2.model.dem_inferred_journey_status import DemInferredJourneyStatus
from datadog_api_client.v2.model.dem_journeys_list_response import DemJourneysListResponse
from datadog_api_client.v2.model.dem_batch_get_journeys_request import DemBatchGetJourneysRequest
from datadog_api_client.v2.model.dem_variant_response import DemVariantResponse
from datadog_api_client.v2.model.dem_variant_request import DemVariantRequest
from datadog_api_client.v2.model.dem_recommended_tests_response import DemRecommendedTestsResponse
from datadog_api_client.v2.model.dem_journey_test_suite_response import DemJourneyTestSuiteResponse
from datadog_api_client.v2.model.dem_create_journey_test_suite_request import DemCreateJourneyTestSuiteRequest


class DEMApi:
    """
    Manage Digital Experience Monitoring journeys.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._batch_get_journeys_by_test_suite_i_ds_endpoint = _Endpoint(
            settings={
                "response_type": (DemJourneysListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/suites/batch",
                "operation_id": "batch_get_journeys_by_test_suite_i_ds",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DemBatchGetJourneysRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_journey_endpoint = _Endpoint(
            settings={
                "response_type": (DemJourneyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys",
                "operation_id": "create_journey",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (DemJourneyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_journey_variant_endpoint = _Endpoint(
            settings={
                "response_type": (DemVariantResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/{journey_id}/variants",
                "operation_id": "create_journey_variant",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "journey_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "journey_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DemVariantRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_test_suite_for_journey_endpoint = _Endpoint(
            settings={
                "response_type": (DemJourneyTestSuiteResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/{public_journey_id}/suite",
                "operation_id": "create_test_suite_for_journey",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "public_journey_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "public_journey_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DemCreateJourneyTestSuiteRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_ignored_inferred_journey_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/inferred/ignored/{journey_id}",
                "operation_id": "delete_ignored_inferred_journey",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "journey_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "journey_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_journey_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/{journey_id}",
                "operation_id": "delete_journey",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "journey_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "journey_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_journey_variant_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/variants/{variant_id}",
                "operation_id": "delete_journey_variant",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "variant_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "variant_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_journey_endpoint = _Endpoint(
            settings={
                "response_type": (DemJourneyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/{journey_id}",
                "operation_id": "get_journey",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "journey_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "journey_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_journey_recommended_tests_endpoint = _Endpoint(
            settings={
                "response_type": (DemRecommendedTestsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/{journey_id}/recommended-tests",
                "operation_id": "get_journey_recommended_tests",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "journey_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "journey_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._ignore_inferred_journey_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/inferred/{journey_id}/ignore",
                "operation_id": "ignore_inferred_journey",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "journey_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "journey_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._search_inferred_journeys_endpoint = _Endpoint(
            settings={
                "response_type": (DemSearchInferredJourneysResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/inferred/search",
                "operation_id": "search_inferred_journeys",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "status": {
                    "openapi_types": (DemInferredJourneyStatus,),
                    "attribute": "status",
                    "location": "query",
                },
                "q": {
                    "openapi_types": (str,),
                    "attribute": "q",
                    "location": "query",
                },
                "app_id": {
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._search_journeys_endpoint = _Endpoint(
            settings={
                "response_type": (DemJourneysListResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/search",
                "operation_id": "search_journeys",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "query": {
                    "openapi_types": (str,),
                    "attribute": "query",
                    "location": "query",
                },
                "page_offset": {
                    "openapi_types": (int,),
                    "attribute": "page[offset]",
                    "location": "query",
                },
                "page_limit": {
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
                "creator": {
                    "openapi_types": (str,),
                    "attribute": "creator",
                    "location": "query",
                },
                "team": {
                    "openapi_types": (str,),
                    "attribute": "team",
                    "location": "query",
                },
                "app_id": {
                    "openapi_types": (str,),
                    "attribute": "app_id",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._update_journey_endpoint = _Endpoint(
            settings={
                "response_type": (DemJourneyResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/{journey_id}",
                "operation_id": "update_journey",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "journey_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "journey_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DemJourneyCreateRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_journey_variant_endpoint = _Endpoint(
            settings={
                "response_type": (DemVariantResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/dem/journeys/variants/{variant_id}",
                "operation_id": "update_journey_variant",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "variant_id": {
                    "required": True,
                    "openapi_types": (str,),
                    "attribute": "variant_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (DemVariantRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def batch_get_journeys_by_test_suite_i_ds(
        self,
        body: DemBatchGetJourneysRequest,
    ) -> DemJourneysListResponse:
        """Batch get DEM journeys by test suite IDs.

        Return DEM journeys associated with multiple given test suite IDs.

        :type body: DemBatchGetJourneysRequest
        :rtype: DemJourneysListResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._batch_get_journeys_by_test_suite_i_ds_endpoint.call_with_http_info(**kwargs)

    def create_journey(
        self,
        body: DemJourneyCreateRequest,
    ) -> DemJourneyResponse:
        """Create a DEM journey.

        Create a DEM journey.

        :type body: DemJourneyCreateRequest
        :rtype: DemJourneyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_journey_endpoint.call_with_http_info(**kwargs)

    def create_journey_variant(
        self,
        journey_id: str,
        body: DemVariantRequest,
    ) -> DemVariantResponse:
        """Create a DEM journey variant.

        Create a variant for a DEM journey.

        :param journey_id: The unique identifier of the journey that owns the variant.
        :type journey_id: str
        :type body: DemVariantRequest
        :rtype: DemVariantResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["journey_id"] = journey_id

        kwargs["body"] = body

        return self._create_journey_variant_endpoint.call_with_http_info(**kwargs)

    def create_test_suite_for_journey(
        self,
        public_journey_id: str,
        body: DemCreateJourneyTestSuiteRequest,
    ) -> DemJourneyTestSuiteResponse:
        """Create a test suite for a DEM journey.

        Trigger test suite creation for a given DEM journey.

        :param public_journey_id: The public identifier of the DEM journey for which to create a test suite.
        :type public_journey_id: str
        :type body: DemCreateJourneyTestSuiteRequest
        :rtype: DemJourneyTestSuiteResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["public_journey_id"] = public_journey_id

        kwargs["body"] = body

        return self._create_test_suite_for_journey_endpoint.call_with_http_info(**kwargs)

    def delete_ignored_inferred_journey(
        self,
        journey_id: str,
    ) -> None:
        """Delete an ignored inferred DEM journey.

        Remove an ignored inferred DEM journey, making it eligible to appear as a candidate again.

        :param journey_id: The unique identifier of the ignored inferred journey to delete.
        :type journey_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["journey_id"] = journey_id

        return self._delete_ignored_inferred_journey_endpoint.call_with_http_info(**kwargs)

    def delete_journey(
        self,
        journey_id: str,
    ) -> None:
        """Delete a DEM journey.

        Delete a DEM journey by its ID.

        :param journey_id: The unique identifier of the DEM journey to delete.
        :type journey_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["journey_id"] = journey_id

        return self._delete_journey_endpoint.call_with_http_info(**kwargs)

    def delete_journey_variant(
        self,
        variant_id: str,
    ) -> None:
        """Delete a DEM journey variant.

        Delete a variant from a DEM journey.

        :param variant_id: The unique identifier of the variant to delete.
        :type variant_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["variant_id"] = variant_id

        return self._delete_journey_variant_endpoint.call_with_http_info(**kwargs)

    def get_journey(
        self,
        journey_id: str,
    ) -> DemJourneyResponse:
        """Get a DEM journey.

        Retrieve a single DEM journey by its ID.

        :param journey_id: The unique identifier of the DEM journey.
        :type journey_id: str
        :rtype: DemJourneyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["journey_id"] = journey_id

        return self._get_journey_endpoint.call_with_http_info(**kwargs)

    def get_journey_recommended_tests(
        self,
        journey_id: str,
    ) -> DemRecommendedTestsResponse:
        """Get recommended tests for a DEM journey.

        Retrieve AI-recommended synthetic tests for a DEM journey. Returns an empty list when no recommendation is available.

        :param journey_id: The unique identifier of the journey.
        :type journey_id: str
        :rtype: DemRecommendedTestsResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["journey_id"] = journey_id

        return self._get_journey_recommended_tests_endpoint.call_with_http_info(**kwargs)

    def ignore_inferred_journey(
        self,
        journey_id: str,
    ) -> None:
        """Ignore an inferred DEM journey.

        Mark an inferred DEM journey as ignored so it no longer appears in the candidate list.

        :param journey_id: The unique identifier of the inferred journey to ignore.
        :type journey_id: str
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["journey_id"] = journey_id

        return self._ignore_inferred_journey_endpoint.call_with_http_info(**kwargs)

    def search_inferred_journeys(
        self,
        *,
        status: Union[DemInferredJourneyStatus, UnsetType] = unset,
        q: Union[str, UnsetType] = unset,
        app_id: Union[str, UnsetType] = unset,
    ) -> DemSearchInferredJourneysResponse:
        """Search inferred DEM journeys.

        Search for inferred DEM journeys by status. Returns candidates (status=candidate, the default) or ignored journeys (status=ignored). Supports optional fuzzy name filtering and app ID filtering.

        :param status: Filter by inferred journey status. Use ``candidate`` (default) to retrieve journeys suggested for promotion, or ``ignored`` to retrieve journeys that have been dismissed.
        :type status: DemInferredJourneyStatus, optional
        :param q: Fuzzy search query to filter inferred journeys by name.
        :type q: str, optional
        :param app_id: Filter inferred journeys by application ID.
        :type app_id: str, optional
        :rtype: DemSearchInferredJourneysResponse
        """
        kwargs: Dict[str, Any] = {}
        if status is not unset:
            kwargs["status"] = status

        if q is not unset:
            kwargs["q"] = q

        if app_id is not unset:
            kwargs["app_id"] = app_id

        return self._search_inferred_journeys_endpoint.call_with_http_info(**kwargs)

    def search_journeys(
        self,
        *,
        query: Union[str, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        creator: Union[str, UnsetType] = unset,
        team: Union[str, UnsetType] = unset,
        app_id: Union[str, UnsetType] = unset,
    ) -> DemJourneysListResponse:
        """Search DEM journeys.

        Search for DEM journeys with optional filtering by query, creator, team, and app.

        :param query: A search query string to filter journeys by name.
        :type query: str, optional
        :param page_offset: The offset for pagination.
        :type page_offset: int, optional
        :param page_limit: The maximum number of results to return.
        :type page_limit: int, optional
        :param creator: Filter journeys by creator handle.
        :type creator: str, optional
        :param team: Filter journeys by team tag.
        :type team: str, optional
        :param app_id: Filter journeys by application ID.
        :type app_id: str, optional
        :rtype: DemJourneysListResponse
        """
        kwargs: Dict[str, Any] = {}
        if query is not unset:
            kwargs["query"] = query

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if creator is not unset:
            kwargs["creator"] = creator

        if team is not unset:
            kwargs["team"] = team

        if app_id is not unset:
            kwargs["app_id"] = app_id

        return self._search_journeys_endpoint.call_with_http_info(**kwargs)

    def update_journey(
        self,
        journey_id: str,
        body: DemJourneyCreateRequest,
    ) -> DemJourneyResponse:
        """Update a DEM journey.

        Update an existing DEM journey by its ID.

        :param journey_id: The unique identifier of the DEM journey to update.
        :type journey_id: str
        :type body: DemJourneyCreateRequest
        :rtype: DemJourneyResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["journey_id"] = journey_id

        kwargs["body"] = body

        return self._update_journey_endpoint.call_with_http_info(**kwargs)

    def update_journey_variant(
        self,
        variant_id: str,
        body: DemVariantRequest,
    ) -> DemVariantResponse:
        """Update a DEM journey variant.

        Update an existing variant of a DEM journey.

        :param variant_id: The unique identifier of the variant to update.
        :type variant_id: str
        :type body: DemVariantRequest
        :rtype: DemVariantResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["variant_id"] = variant_id

        kwargs["body"] = body

        return self._update_journey_variant_endpoint.call_with_http_info(**kwargs)
