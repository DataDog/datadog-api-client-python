# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union

from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import (
    datetime,
    UnsetType,
    unset,
    UUID,
)
from datadog_api_client.v2.model.experiments_experiment_v2_list_dto_array import ExperimentsExperimentV2ListDTOArray
from datadog_api_client.v2.model.experiments_experiment_v2_dto import ExperimentsExperimentV2DTO
from datadog_api_client.v2.model.experiments_create_experiment_v2_request import ExperimentsCreateExperimentV2Request
from datadog_api_client.v2.model.experiments_exposure_sql_model_v2_dto_array import (
    ExperimentsExposureSQLModelV2DTOArray,
)
from datadog_api_client.v2.model.experiments_exposure_sql_model_v2_dto import ExperimentsExposureSQLModelV2DTO
from datadog_api_client.v2.model.experiments_create_exposure_sql_model_v2_request import (
    ExperimentsCreateExposureSQLModelV2Request,
)
from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_response import (
    ExperimentsUpdateExposureSQLModelV2Response,
)
from datadog_api_client.v2.model.experiments_metric_collection_v2_dto_array import ExperimentsMetricCollectionV2DTOArray
from datadog_api_client.v2.model.experiments_metric_collection_v2_dto import ExperimentsMetricCollectionV2DTO
from datadog_api_client.v2.model.experiments_create_metric_collection_v2_request import (
    ExperimentsCreateMetricCollectionV2Request,
)
from datadog_api_client.v2.model.experiments_patch_metric_collection_v2_request import (
    ExperimentsPatchMetricCollectionV2Request,
)
from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto_array import ExperimentsMetricSQLModelV2DTOArray
from datadog_api_client.v2.model.experiments_metric_sql_model_v2_dto import ExperimentsMetricSQLModelV2DTO
from datadog_api_client.v2.model.experiments_create_metric_sql_model_v2_request import (
    ExperimentsCreateMetricSQLModelV2Request,
)
from datadog_api_client.v2.model.experiments_update_metric_sql_model_v2_response import (
    ExperimentsUpdateMetricSQLModelV2Response,
)
from datadog_api_client.v2.model.experiments_metric_v2_dto_array import ExperimentsMetricV2DTOArray
from datadog_api_client.v2.model.experiments_metric_v2_dto import ExperimentsMetricV2DTO
from datadog_api_client.v2.model.experiments_create_metric_v2_request import ExperimentsCreateMetricV2Request
from datadog_api_client.v2.model.experiments_update_metric_v2_request import ExperimentsUpdateMetricV2Request
from datadog_api_client.v2.model.experiments_public_protocol_list_response_array import (
    ExperimentsPublicProtocolListResponseArray,
)
from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_status import (
    ExperimentsPublicProtocolResponseDataAttributesStatus,
)
from datadog_api_client.v2.model.experiments_public_protocol_response import ExperimentsPublicProtocolResponse
from datadog_api_client.v2.model.experiments_refresh_experiment_results_v2_dto_array import (
    ExperimentsRefreshExperimentResultsV2DTOArray,
)
from datadog_api_client.v2.model.experiments_subject_type_v2_dto_array import ExperimentsSubjectTypeV2DTOArray
from datadog_api_client.v2.model.experiments_subject_type_v2_dto import ExperimentsSubjectTypeV2DTO
from datadog_api_client.v2.model.experiments_create_subject_type_v2_request import ExperimentsCreateSubjectTypeV2Request
from datadog_api_client.v2.model.experiments_patch_subject_type_v2_request import ExperimentsPatchSubjectTypeV2Request
from datadog_api_client.v2.model.experiments_patch_experiment_v2_response import ExperimentsPatchExperimentV2Response
from datadog_api_client.v2.model.experiments_patch_experiment_v2_request import ExperimentsPatchExperimentV2Request
from datadog_api_client.v2.model.experiments_analysis_plan_v2_dto import ExperimentsAnalysisPlanV2DTO
from datadog_api_client.v2.model.experiments_analysis_plan_v2_mutation_response import (
    ExperimentsAnalysisPlanV2MutationResponse,
)
from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request import ExperimentsAnalysisPlanWriteV2Request
from datadog_api_client.v2.model.experiments_cancel_experiment_v2_request import ExperimentsCancelExperimentV2Request
from datadog_api_client.v2.model.experiments_conclude_experiment_v2_request import (
    ExperimentsConcludeExperimentV2Request,
)
from datadog_api_client.v2.model.experiments_experiment_diagnostics_v2_dto import ExperimentsExperimentDiagnosticsV2DTO
from datadog_api_client.v2.model.experiments_experiment_metric_group_v2_dto_array import (
    ExperimentsExperimentMetricGroupV2DTOArray,
)
from datadog_api_client.v2.model.experiments_experiment_metric_group_mutation_v2 import (
    ExperimentsExperimentMetricGroupMutationV2,
)
from datadog_api_client.v2.model.experiments_create_experiment_metric_group_v2_request import (
    ExperimentsCreateExperimentMetricGroupV2Request,
)
from datadog_api_client.v2.model.experiments_patch_experiment_metric_group_v2_request import (
    ExperimentsPatchExperimentMetricGroupV2Request,
)
from datadog_api_client.v2.model.experiments_variant_results_v2_dto_array import ExperimentsVariantResultsV2DTOArray
from datadog_api_client.v2.model.experiments_refresh_experiment_results_v2_dto import (
    ExperimentsRefreshExperimentResultsV2DTO,
)
from datadog_api_client.v2.model.experiments_start_experiment_v2_request import ExperimentsStartExperimentV2Request
from datadog_api_client.v2.model.experiments_traffic_summary_v2_dto import ExperimentsTrafficSummaryV2DTO


class ExperimentsApi:
    """
    Create and manage experiments, metrics, subject types, SQL models, and protocols.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient(Configuration())
        self.api_client = api_client

        self._archive_exposure_sql_model_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/exposure-sql-models/{exposure_sql_model_id}/archive",
                "operation_id": "archive_exposure_sql_model",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "exposure_sql_model_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "exposure_sql_model_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._cancel_experiment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/cancel",
                "operation_id": "cancel_experiment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsCancelExperimentV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._conclude_experiment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/conclude",
                "operation_id": "conclude_experiment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsConcludeExperimentV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_experiment_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExperimentV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments",
                "operation_id": "create_experiment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsCreateExperimentV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_experiment_metric_group_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExperimentMetricGroupMutationV2,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/metric-groups",
                "operation_id": "create_experiment_metric_group",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsCreateExperimentMetricGroupV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_experiment_metric_group_from_collection_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExperimentMetricGroupMutationV2,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/metric-groups/from-collection/{metric_collection_id}",
                "operation_id": "create_experiment_metric_group_from_collection",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "metric_collection_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_collection_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._create_exposure_sql_model_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExposureSQLModelV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/exposure-sql-models",
                "operation_id": "create_exposure_sql_model",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsCreateExposureSQLModelV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_metric_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metrics",
                "operation_id": "create_metric",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsCreateMetricV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_metric_collection_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricCollectionV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metric-collections",
                "operation_id": "create_metric_collection",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsCreateMetricCollectionV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_metric_sql_model_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricSQLModelV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metric-sql-models",
                "operation_id": "create_metric_sql_model",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsCreateMetricSQLModelV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_subject_type_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsSubjectTypeV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/subject-types",
                "operation_id": "create_subject_type",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsCreateSubjectTypeV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._delete_experiment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}",
                "operation_id": "delete_experiment",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_experiment_metric_group_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/metric-groups/{metric_group_id}",
                "operation_id": "delete_experiment_metric_group",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "metric_group_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_group_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_metric_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metrics/{metric_id}",
                "operation_id": "delete_metric",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "metric_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_metric_collection_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metric-collections/{metric_collection_id}",
                "operation_id": "delete_metric_collection",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "metric_collection_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_collection_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._delete_subject_type_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/subject-types/{subject_type_id}",
                "operation_id": "delete_subject_type",
                "http_method": "DELETE",
                "version": "v2",
            },
            params_map={
                "subject_type_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "subject_type_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._get_experiment_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExperimentV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}",
                "operation_id": "get_experiment",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_experiment_analysis_plan_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsAnalysisPlanV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/analysis-plan",
                "operation_id": "get_experiment_analysis_plan",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_experiment_diagnostics_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExperimentDiagnosticsV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/diagnostics",
                "operation_id": "get_experiment_diagnostics",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_experiment_protocol_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsPublicProtocolResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/protocols/{protocol_id}",
                "operation_id": "get_experiment_protocol",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "protocol_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "protocol_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_experiment_results_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsVariantResultsV2DTOArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/results",
                "operation_id": "get_experiment_results",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_experiment_traffic_summary_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsTrafficSummaryV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/traffic-summary",
                "operation_id": "get_experiment_traffic_summary",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_exposure_sql_model_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExposureSQLModelV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/exposure-sql-models/{exposure_sql_model_id}",
                "operation_id": "get_exposure_sql_model",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "exposure_sql_model_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "exposure_sql_model_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([str],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_metric_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metrics/{metric_id}",
                "operation_id": "get_metric",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": ([str],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
                },
                "metric_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_metric_collection_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricCollectionV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metric-collections/{metric_collection_id}",
                "operation_id": "get_metric_collection",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "metric_collection_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_collection_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_metric_sql_model_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricSQLModelV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metric-sql-models/{metric_sql_model_id}",
                "operation_id": "get_metric_sql_model",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": ([str],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
                },
                "metric_sql_model_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_sql_model_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._get_subject_type_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsSubjectTypeV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/subject-types/{subject_type_id}",
                "operation_id": "get_subject_type",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
                },
                "subject_type_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "subject_type_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_experiment_metric_groups_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExperimentMetricGroupV2DTOArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/metric-groups",
                "operation_id": "list_experiment_metric_groups",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_experiment_protocols_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsPublicProtocolListResponseArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/protocols",
                "operation_id": "list_experiment_protocols",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "filter_status": {
                    "openapi_types": ([ExperimentsPublicProtocolResponseDataAttributesStatus],),
                    "attribute": "filter[status]",
                    "location": "query",
                    "collection_format": "multi",
                },
                "filter_primary_metric_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[primary_metric_id]",
                    "location": "query",
                },
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "filter_subject_type_id": {
                    "openapi_types": (UUID,),
                    "attribute": "filter[subject_type_id]",
                    "location": "query",
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

        self._list_experiments_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExperimentV2ListDTOArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments",
                "operation_id": "list_experiments",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "concluded_since": {
                    "openapi_types": (datetime,),
                    "attribute": "concluded_since",
                    "location": "query",
                },
                "created_since": {
                    "openapi_types": (datetime,),
                    "attribute": "created_since",
                    "location": "query",
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
                "protocol_id": {
                    "openapi_types": ([UUID],),
                    "attribute": "protocol_id",
                    "location": "query",
                    "collection_format": "multi",
                },
                "results_updated_before": {
                    "openapi_types": (datetime,),
                    "attribute": "results_updated_before",
                    "location": "query",
                },
                "results_updated_since": {
                    "openapi_types": (datetime,),
                    "attribute": "results_updated_since",
                    "location": "query",
                },
                "search": {
                    "openapi_types": (str,),
                    "attribute": "search",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (str,),
                    "attribute": "sort",
                    "location": "query",
                },
                "status": {
                    "openapi_types": ([str],),
                    "attribute": "status",
                    "location": "query",
                    "collection_format": "multi",
                },
                "tags": {
                    "openapi_types": ([str],),
                    "attribute": "tags",
                    "location": "query",
                    "collection_format": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._list_exposure_sql_models_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExposureSQLModelV2DTOArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/exposure-sql-models",
                "operation_id": "list_exposure_sql_models",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": ([str],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
                },
                "include_archived": {
                    "openapi_types": (bool,),
                    "attribute": "include_archived",
                    "location": "query",
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
                "search": {
                    "openapi_types": (str,),
                    "attribute": "search",
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

        self._list_metric_collections_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricCollectionV2DTOArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metric-collections",
                "operation_id": "list_metric_collections",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": ([str],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
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
                "search": {
                    "openapi_types": (str,),
                    "attribute": "search",
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

        self._list_metrics_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricV2DTOArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metrics",
                "operation_id": "list_metrics",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": ([str],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
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
                "search": {
                    "openapi_types": (str,),
                    "attribute": "search",
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

        self._list_metric_sql_models_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricSQLModelV2DTOArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metric-sql-models",
                "operation_id": "list_metric_sql_models",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": ([str],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
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

        self._list_subject_types_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsSubjectTypeV2DTOArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/subject-types",
                "operation_id": "list_subject_types",
                "http_method": "GET",
                "version": "v2",
            },
            params_map={
                "include": {
                    "openapi_types": (str,),
                    "attribute": "include",
                    "location": "query",
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
                "search": {
                    "openapi_types": (str,),
                    "attribute": "search",
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

        self._patch_experiment_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsPatchExperimentV2Response,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}",
                "operation_id": "patch_experiment",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsPatchExperimentV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._patch_subject_type_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsSubjectTypeV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/subject-types/{subject_type_id}",
                "operation_id": "patch_subject_type",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "subject_type_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "subject_type_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsPatchSubjectTypeV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._refresh_experiment_results_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsRefreshExperimentResultsV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/results/refresh",
                "operation_id": "refresh_experiment_results",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "full_refresh": {
                    "openapi_types": (bool,),
                    "attribute": "full_refresh",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._refresh_experiment_results_for_org_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsRefreshExperimentResultsV2DTOArray,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/results/refresh",
                "operation_id": "refresh_experiment_results_for_org",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "full_refresh": {
                    "openapi_types": (bool,),
                    "attribute": "full_refresh",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
            },
            api_client=api_client,
        )

        self._set_default_subject_type_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/subject-types/{subject_type_id}/default",
                "operation_id": "set_default_subject_type",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "subject_type_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "subject_type_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._start_experiment_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/start",
                "operation_id": "start_experiment",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "body": {
                    "openapi_types": (ExperimentsStartExperimentV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["*/*"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._unarchive_exposure_sql_model_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/exposure-sql-models/{exposure_sql_model_id}/unarchive",
                "operation_id": "unarchive_exposure_sql_model",
                "http_method": "POST",
                "version": "v2",
            },
            params_map={
                "exposure_sql_model_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "exposure_sql_model_id",
                    "location": "path",
                },
            },
            headers_map={
                "accept": ["*/*"],
            },
            api_client=api_client,
        )

        self._update_experiment_analysis_plan_attributes_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsAnalysisPlanV2MutationResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/analysis-plan",
                "operation_id": "update_experiment_analysis_plan_attributes",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsAnalysisPlanWriteV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_experiment_metric_group_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsExperimentMetricGroupMutationV2,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/{experiment_id}/metric-groups/{metric_group_id}",
                "operation_id": "update_experiment_metric_group",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "experiment_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "experiment_id",
                    "location": "path",
                },
                "metric_group_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_group_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsPatchExperimentMetricGroupV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_exposure_sql_model_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsUpdateExposureSQLModelV2Response,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/exposure-sql-models/{exposure_sql_model_id}",
                "operation_id": "update_exposure_sql_model",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "exposure_sql_model_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "exposure_sql_model_id",
                    "location": "path",
                },
                "include": {
                    "openapi_types": ([str],),
                    "attribute": "include",
                    "location": "query",
                    "collection_format": "multi",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsCreateExposureSQLModelV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_metric_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metrics/{metric_id}",
                "operation_id": "update_metric",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "metric_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsUpdateMetricV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_metric_collection_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsMetricCollectionV2DTO,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metric-collections/{metric_collection_id}",
                "operation_id": "update_metric_collection",
                "http_method": "PATCH",
                "version": "v2",
            },
            params_map={
                "metric_collection_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_collection_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsPatchMetricCollectionV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_metric_sql_model_endpoint = _Endpoint(
            settings={
                "response_type": (ExperimentsUpdateMetricSQLModelV2Response,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/experiments/metric-sql-models/{metric_sql_model_id}",
                "operation_id": "update_metric_sql_model",
                "http_method": "PUT",
                "version": "v2",
            },
            params_map={
                "metric_sql_model_id": {
                    "required": True,
                    "openapi_types": (UUID,),
                    "attribute": "metric_sql_model_id",
                    "location": "path",
                },
                "body": {
                    "required": True,
                    "openapi_types": (ExperimentsCreateMetricSQLModelV2Request,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def archive_exposure_sql_model(
        self,
        exposure_sql_model_id: UUID,
    ) -> None:
        """Archive exposure SQL model.

        Archive an exposure SQL model. Archived models are hidden from the default list and are no longer refreshed for new feature flags. Experiments already reading from the model keep working. Archiving is how a model that is in use by an experiment, and therefore cannot be deleted, is retired.

        :param exposure_sql_model_id: The UUID of the exposure SQL model.
        :type exposure_sql_model_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exposure_sql_model_id"] = exposure_sql_model_id

        return self._archive_exposure_sql_model_endpoint.call_with_http_info(**kwargs)

    def cancel_experiment(
        self,
        experiment_id: UUID,
        body: ExperimentsCancelExperimentV2Request,
    ) -> None:
        """Cancel experiment.

        Cancel an experiment, ending it without a winning variant. The experiment moves to CANCELLED status, the
        supplied reason is recorded in its conclusion as the decision reason, and the experiment is unlinked from the
        feature flag allocations that exposed it, which stops its exposure. An experiment that has already completed
        its rollout, had its code removed, or been canceled cannot be canceled again. Canceling is not reversible: an
        experiment cannot be returned to a running state afterward. It is also not idempotent: canceling an
        already-canceled experiment returns 409, so a retry after a timeout cannot be distinguished from a
        cancellation made by someone else.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :type body: ExperimentsCancelExperimentV2Request
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        kwargs["body"] = body

        return self._cancel_experiment_endpoint.call_with_http_info(**kwargs)

    def conclude_experiment(
        self,
        experiment_id: UUID,
        body: ExperimentsConcludeExperimentV2Request,
    ) -> None:
        """Conclude experiment.

        Conclude an experiment on a winning variant. The experiment moves to DECISION_MADE status, the outcome is recorded in its conclusion, and for a flag-backed experiment the winning variant is rolled out to 100% of the linked feature flag allocation. ``decision_variant_key`` must match a variant in the experiment. Only an experiment that is currently running or ready for a decision can be concluded. Concluding is not reversible and is not idempotent: concluding an already-concluded experiment returns 409.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :type body: ExperimentsConcludeExperimentV2Request
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        kwargs["body"] = body

        return self._conclude_experiment_endpoint.call_with_http_info(**kwargs)

    def create_experiment(
        self,
        body: ExperimentsCreateExperimentV2Request,
    ) -> ExperimentsExperimentV2DTO:
        """Create experiment.

        Create a draft experiment. ``name`` is required. ``structured_metadata`` identifies each metadata field by ``field_key`` ; use ``freetext_value`` for free-text fields and ``enum_values`` for enum fields. When this attribute is present, the request must include a value for every required metadata field. When ``protocol_id`` is present, the published protocol supplies the subject type, decision metrics, analysis-plan defaults, and configuration and enforcement baselines. The request may also include hypothesis, tags, teams, related links, and assignment or event date overrides that satisfy the protocol's duration rules; omit subject_type_id, decision_metrics, variants, warehouse_exposure_configuration, datadog_flag_configuration, traffic_exposure, split_by_properties, and structured_metadata. The protocol association cannot be changed after creation. Without ``protocol_id`` , a complete Warehouse or Datadog configuration saves the experiment and its configuration in one transaction. For Datadog flag configuration, send ``name`` , ``subject_type_id`` , ``decision_metrics`` , ``variants`` , ``traffic_exposure`` , ``assignments_start_date`` , ``assignments_end_date`` , ``events_start_date`` , and ``events_end_date``. The four date fields can be null. Inside ``datadog_flag_configuration`` , send ``feature_flag_id`` , ``environment_id`` , ``targeting_rules`` , and ``entry_point``. Use ``targeting_rules: []`` and ``entry_point: null`` when unused. This creates one saved draft allocation that does not serve traffic. Omit all configuration fields to create an experiment without an allocation. This endpoint is not idempotent.

        :type body: ExperimentsCreateExperimentV2Request
        :rtype: ExperimentsExperimentV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_experiment_endpoint.call_with_http_info(**kwargs)

    def create_experiment_metric_group(
        self,
        experiment_id: UUID,
        body: ExperimentsCreateExperimentMetricGroupV2Request,
    ) -> ExperimentsExperimentMetricGroupMutationV2:
        """Create experiment metric group.

        Create a non-decision metric group. The optional metrics array is ordered. Decision groups remain managed through decision_metrics on the experiment resource. This operation does not synchronously recompute results.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :type body: ExperimentsCreateExperimentMetricGroupV2Request
        :rtype: ExperimentsExperimentMetricGroupMutationV2
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        kwargs["body"] = body

        return self._create_experiment_metric_group_endpoint.call_with_http_info(**kwargs)

    def create_experiment_metric_group_from_collection(
        self,
        experiment_id: UUID,
        metric_collection_id: UUID,
    ) -> ExperimentsExperimentMetricGroupMutationV2:
        """Create experiment metric group from collection.

        Copy a metric collection into a new non-decision metric group. The group is a request-time snapshot: later changes to the collection do not affect the experiment. Metric order is preserved. The operation is not idempotent, and incompatible or empty collections are rejected without creating a group.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :param metric_collection_id: The UUID of the metric collection.
        :type metric_collection_id: UUID
        :rtype: ExperimentsExperimentMetricGroupMutationV2
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        kwargs["metric_collection_id"] = metric_collection_id

        return self._create_experiment_metric_group_from_collection_endpoint.call_with_http_info(**kwargs)

    def create_exposure_sql_model(
        self,
        body: ExperimentsCreateExposureSQLModelV2Request,
    ) -> ExperimentsExposureSQLModelV2DTO:
        """Create exposure SQL model.

        Create an exposure SQL model. Requires at least one subject type. The warehouse connection is resolved from the organization, which has exactly one.

        :type body: ExperimentsCreateExposureSQLModelV2Request
        :rtype: ExperimentsExposureSQLModelV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_exposure_sql_model_endpoint.call_with_http_info(**kwargs)

    def create_metric(
        self,
        body: ExperimentsCreateMetricV2Request,
    ) -> ExperimentsMetricV2DTO:
        """Create metric.

        Create a metric. The metric's type is derived from the aggregation shape: a numerator alone is SIMPLE, a numerator with a denominator is RATIO, and a percentile aggregation is PERCENTILE. Warehouse aggregations reference measures by UUID. Property filters use property_id or measure_id UUIDs returned by the same metric SQL model; every reference must belong to the aggregation's data source. The is_certified attribute is rejected. Certification cannot be changed through this endpoint.

        :type body: ExperimentsCreateMetricV2Request
        :rtype: ExperimentsMetricV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_metric_endpoint.call_with_http_info(**kwargs)

    def create_metric_collection(
        self,
        body: ExperimentsCreateMetricCollectionV2Request,
    ) -> ExperimentsMetricCollectionV2DTO:
        """Create metric collection.

        Create metric collection.

        :type body: ExperimentsCreateMetricCollectionV2Request
        :rtype: ExperimentsMetricCollectionV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_metric_collection_endpoint.call_with_http_info(**kwargs)

    def create_metric_sql_model(
        self,
        body: ExperimentsCreateMetricSQLModelV2Request,
    ) -> ExperimentsMetricSQLModelV2DTO:
        """Create metric SQL model.

        Create a metric SQL model. Requires at least one subject type, whose subject_type_id must already exist for the organization (list them with GET /api/v2/experiments/subject-types). The model is created against the organization's warehouse connection, which is resolved server-side. Only customer-defined measures belong in measures. The response provides unique_subject_count_measure_id for each subject type and event_count_measure_id for use in metric aggregations. column_type is required for every measure and property. Certification is read-only and cannot be changed through this endpoint.

        :type body: ExperimentsCreateMetricSQLModelV2Request
        :rtype: ExperimentsMetricSQLModelV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_metric_sql_model_endpoint.call_with_http_info(**kwargs)

    def create_subject_type(
        self,
        body: ExperimentsCreateSubjectTypeV2Request,
    ) -> ExperimentsSubjectTypeV2DTO:
        """Create subject type.

        Create a subject type for the organization.

        :type body: ExperimentsCreateSubjectTypeV2Request
        :rtype: ExperimentsSubjectTypeV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["body"] = body

        return self._create_subject_type_endpoint.call_with_http_info(**kwargs)

    def delete_experiment(
        self,
        experiment_id: UUID,
    ) -> None:
        """Delete experiment.

        Delete an experiment and its linked feature flag allocations in one database transaction. After deletion, the experiment is no longer returned by the API. If the transaction fails, neither the experiment nor its allocations are deleted. Deleting an experiment cannot be undone.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        return self._delete_experiment_endpoint.call_with_http_info(**kwargs)

    def delete_experiment_metric_group(
        self,
        experiment_id: UUID,
        metric_group_id: UUID,
    ) -> None:
        """Delete experiment metric group.

        Delete a non-decision metric group and its memberships. Decision groups remain managed through the experiment resource. This operation does not start a pipeline. Read experiment results after deletion to check stale metadata, then explicitly refresh results when required.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :param metric_group_id: The UUID of the metric group.
        :type metric_group_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        kwargs["metric_group_id"] = metric_group_id

        return self._delete_experiment_metric_group_endpoint.call_with_http_info(**kwargs)

    def delete_metric(
        self,
        metric_id: UUID,
    ) -> None:
        """Delete metric.

        Delete a metric. Certified metrics are read-only through this endpoint. The record is soft-deleted and stops appearing in reads. A metric still referenced by an experiment cannot be deleted; detach it from those experiments first.

        :param metric_id: The UUID of the metric.
        :type metric_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_id"] = metric_id

        return self._delete_metric_endpoint.call_with_http_info(**kwargs)

    def delete_metric_collection(
        self,
        metric_collection_id: UUID,
    ) -> None:
        """Delete metric collection.

        Delete metric collection.

        :param metric_collection_id: The UUID of the metric collection.
        :type metric_collection_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_collection_id"] = metric_collection_id

        return self._delete_metric_collection_endpoint.call_with_http_info(**kwargs)

    def delete_subject_type(
        self,
        subject_type_id: UUID,
    ) -> None:
        """Delete subject type.

        Delete a subject type. The record is soft-deleted and stops appearing in reads. The call is idempotent: deleting the same subject type again also returns 204. The organization's default subject type cannot be deleted; make another one the default first. A subject type that experiments, exposure SQL models, metric SQL models or protocols still reference cannot be deleted either; the refusal names the blockers.

        :param subject_type_id: The UUID of the subject type.
        :type subject_type_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["subject_type_id"] = subject_type_id

        return self._delete_subject_type_endpoint.call_with_http_info(**kwargs)

    def get_experiment(
        self,
        experiment_id: UUID,
    ) -> ExperimentsExperimentV2DTO:
        """Get experiment.

        Get a complete experiment by ID. The response includes structured metadata, related links, and, when a complete setup exists, decision metrics, variants, ``warehouse_exposure_configuration`` , ``datadog_flag_configuration`` , STATIC or STEPS traffic exposure, and assignment and event dates. STEPS describes the configured plan rather than wall-clock history; Datadog step durations exclude pauses. The list endpoint omits these setup details.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :rtype: ExperimentsExperimentV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        return self._get_experiment_endpoint.call_with_http_info(**kwargs)

    def get_experiment_analysis_plan(
        self,
        experiment_id: UUID,
    ) -> ExperimentsAnalysisPlanV2DTO:
        """Get experiment analysis plan.

        Get the effective public statistical analysis settings for an experiment. has_custom_analysis_settings compares only settings the caller can edit; protocol-required differences from company defaults do not make the plan custom.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :rtype: ExperimentsAnalysisPlanV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        return self._get_experiment_analysis_plan_endpoint.call_with_http_info(**kwargs)

    def get_experiment_diagnostics(
        self,
        experiment_id: UUID,
    ) -> ExperimentsExperimentDiagnosticsV2DTO:
        """Get experiment diagnostics.

        Get the diagnostics produced by an experiment's latest analysis run. Each diagnostic includes its category, and the response includes an overall diagnostic or pipeline lifecycle status.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :rtype: ExperimentsExperimentDiagnosticsV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        return self._get_experiment_diagnostics_endpoint.call_with_http_info(**kwargs)

    def get_experiment_protocol(
        self,
        protocol_id: UUID,
    ) -> ExperimentsPublicProtocolResponse:
        """Get experiment protocol.

        Get a draft, published, or archived experiment protocol by ID.

        :param protocol_id: The UUID of the protocol.
        :type protocol_id: UUID
        :rtype: ExperimentsPublicProtocolResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["protocol_id"] = protocol_id

        return self._get_experiment_protocol_endpoint.call_with_http_info(**kwargs)

    def get_experiment_results(
        self,
        experiment_id: UUID,
    ) -> ExperimentsVariantResultsV2DTOArray:
        """Get experiment results.

        Get an experiment's computed results: per-variant statistical analysis for the latest successful run. A historical run cannot be selected. Unavailable analysis statistics, including ``p_value`` and ``confidence_interval`` , are omitted. The ``numerator`` , ``denominator`` , and ``variant_metric_value`` fields can be null when their values are unavailable. Do not treat an omitted or null value as zero.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :rtype: ExperimentsVariantResultsV2DTOArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        return self._get_experiment_results_endpoint.call_with_http_info(**kwargs)

    def get_experiment_traffic_summary(
        self,
        experiment_id: UUID,
    ) -> ExperimentsTrafficSummaryV2DTO:
        """Get experiment traffic summary.

        Get an experiment's traffic summary: per-variant exposure counts and a sample-ratio-mismatch flag (is_traffic_imbalanced). SRM statistics live on the diagnostics endpoint.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :rtype: ExperimentsTrafficSummaryV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        return self._get_experiment_traffic_summary_endpoint.call_with_http_info(**kwargs)

    def get_exposure_sql_model(
        self,
        exposure_sql_model_id: UUID,
        *,
        include: Union[List[str], UnsetType] = unset,
    ) -> ExperimentsExposureSQLModelV2DTO:
        """Get exposure SQL model.

        Get an exposure SQL model. Returns a single model by its ID for the organization, including its subject types and properties.

        :param exposure_sql_model_id: The UUID of the exposure SQL model.
        :type exposure_sql_model_id: UUID
        :param include: Optional fields to include. Repeat this parameter to request several fields. ``counts`` adds
            experiment_count.
        :type include: [str], optional
        :rtype: ExperimentsExposureSQLModelV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exposure_sql_model_id"] = exposure_sql_model_id

        if include is not unset:
            kwargs["include"] = include

        return self._get_exposure_sql_model_endpoint.call_with_http_info(**kwargs)

    def get_metric(
        self,
        metric_id: UUID,
        *,
        include: Union[List[str], UnsetType] = unset,
    ) -> ExperimentsMetricV2DTO:
        """Get metric.

        Get a metric. Returns a single experiment metric by its ID for the organization.

        :param metric_id: The UUID of the metric.
        :type metric_id: UUID
        :param include: Optional fields to include. Repeat this parameter to request several fields. ``counts`` adds
            experiment_count: how many experiments currently reference this metric.
        :type include: [str], optional
        :rtype: ExperimentsMetricV2DTO
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["metric_id"] = metric_id

        return self._get_metric_endpoint.call_with_http_info(**kwargs)

    def get_metric_collection(
        self,
        metric_collection_id: UUID,
    ) -> ExperimentsMetricCollectionV2DTO:
        """Get metric collection.

        Get metric collection.

        :param metric_collection_id: The UUID of the metric collection.
        :type metric_collection_id: UUID
        :rtype: ExperimentsMetricCollectionV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_collection_id"] = metric_collection_id

        return self._get_metric_collection_endpoint.call_with_http_info(**kwargs)

    def get_metric_sql_model(
        self,
        metric_sql_model_id: UUID,
        *,
        include: Union[List[str], UnsetType] = unset,
    ) -> ExperimentsMetricSQLModelV2DTO:
        """Get metric SQL model.

        Get a metric SQL model. Returns a single model by its ID for the organization, including its subject types, measures and properties.

        :param metric_sql_model_id: The UUID of the metric SQL model.
        :type metric_sql_model_id: UUID
        :param include: Optional fields to include. Repeat this parameter to request several fields. ``counts`` adds metric_count
            and experiment_count.
        :type include: [str], optional
        :rtype: ExperimentsMetricSQLModelV2DTO
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["metric_sql_model_id"] = metric_sql_model_id

        return self._get_metric_sql_model_endpoint.call_with_http_info(**kwargs)

    def get_subject_type(
        self,
        subject_type_id: UUID,
        *,
        include: Union[str, UnsetType] = unset,
    ) -> ExperimentsSubjectTypeV2DTO:
        """Get subject type.

        Get a subject type. Returns a single subject type by its ID for the organization.

        :param subject_type_id: The UUID of the subject type.
        :type subject_type_id: UUID
        :param include: Set to ``counts`` to add experiment_count, exposure_source_count, metric_sql_model_count and protocol_count.
        :type include: str, optional
        :rtype: ExperimentsSubjectTypeV2DTO
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        kwargs["subject_type_id"] = subject_type_id

        return self._get_subject_type_endpoint.call_with_http_info(**kwargs)

    def list_experiment_metric_groups(
        self,
        experiment_id: UUID,
    ) -> ExperimentsExperimentMetricGroupV2DTOArray:
        """List experiment metric groups.

        List every decision and non-decision metric group attached to an experiment. Metric references are returned in their stored order. An incomplete draft can have no decision group and returns only the groups that exist.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :rtype: ExperimentsExperimentMetricGroupV2DTOArray
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        return self._list_experiment_metric_groups_endpoint.call_with_http_info(**kwargs)

    def list_experiment_protocols(
        self,
        *,
        filter_status: Union[List[ExperimentsPublicProtocolResponseDataAttributesStatus], UnsetType] = unset,
        filter_primary_metric_id: Union[UUID, UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
        filter_subject_type_id: Union[UUID, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
    ) -> ExperimentsPublicProtocolListResponseArray:
        """List experiment protocols.

        List draft, published, and archived experiment protocols. Omit filter[status] to return all statuses. Only published protocols can be used to create experiments.

        :param filter_status: Filter by protocol status. Repeat this parameter to select more than one status.
        :type filter_status: [ExperimentsPublicProtocolResponseDataAttributesStatus], optional
        :param filter_primary_metric_id: Filter by the UUID of the primary metric in the protocol template.
        :type filter_primary_metric_id: UUID, optional
        :param filter_query: Find protocols whose names contain the search text, regardless of case. Leading and trailing spaces are
            ignored. Blank values apply no filter. The maximum length is 1024 UTF-8 bytes.
        :type filter_query: str, optional
        :param filter_subject_type_id: Filter by the UUID of the subject type in the protocol template.
        :type filter_subject_type_id: UUID, optional
        :param page_limit: Number of results per page. The default is 25. Values above 50 are reduced to 50.
        :type page_limit: int, optional
        :param page_offset: Number of results to skip before returning this page.
        :type page_offset: int, optional
        :param sort: Sort by ``name`` , ``subject_type_name`` , ``primary_metric_name`` , or ``updated_at``. Prefix with ``-`` for
            descending order. The default is ``-updated_at``.
        :type sort: str, optional
        :rtype: ExperimentsPublicProtocolListResponseArray
        """
        kwargs: Dict[str, Any] = {}
        if filter_status is not unset:
            kwargs["filter_status"] = filter_status

        if filter_primary_metric_id is not unset:
            kwargs["filter_primary_metric_id"] = filter_primary_metric_id

        if filter_query is not unset:
            kwargs["filter_query"] = filter_query

        if filter_subject_type_id is not unset:
            kwargs["filter_subject_type_id"] = filter_subject_type_id

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_experiment_protocols_endpoint.call_with_http_info(**kwargs)

    def list_experiments(
        self,
        *,
        concluded_since: Union[datetime, UnsetType] = unset,
        created_since: Union[datetime, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        protocol_id: Union[List[UUID], UnsetType] = unset,
        results_updated_before: Union[datetime, UnsetType] = unset,
        results_updated_since: Union[datetime, UnsetType] = unset,
        search: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        status: Union[List[str], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
    ) -> ExperimentsExperimentV2ListDTOArray:
        """List experiments.

        List experiments. Returns a paginated list of experiments and their structured metadata for the organization. Supports filtering and pagination. Use Get experiment for variants, decision metrics, traffic exposure, and assignment configuration.

        :param concluded_since: Return only experiments concluded at or after this RFC3339 timestamp. Inclusive, and excludes experiments that have not concluded.
        :type concluded_since: datetime, optional
        :param created_since: Return only experiments created at or after this RFC3339 timestamp. Inclusive.
        :type created_since: datetime, optional
        :param page_limit: Maximum number of results to return. Defaults to 25 when omitted, and is capped at 50 (larger values are clamped to 50). The response includes meta.page (with total) and pagination links.
        :type page_limit: int, optional
        :param page_offset: Number of results to skip for pagination. Defaults to 0 when omitted.
        :type page_offset: int, optional
        :param protocol_id: Filter by protocol UUID. Repeat this parameter to supply several IDs. An experiment matches if it uses any
            listed protocol.
        :type protocol_id: [UUID], optional
        :param results_updated_before: Return only experiments whose results_last_updated is before this RFC3339 timestamp. results_last_updated is the later of the latest successful run completion and the latest stored result refresh. Exclusive, and excludes experiments without successful results.
        :type results_updated_before: datetime, optional
        :param results_updated_since: Return only experiments whose results_last_updated is at or after this RFC3339 timestamp. results_last_updated is the later of the latest successful run completion and the latest stored result refresh. Inclusive, and excludes experiments without successful results. This filter does not include all metadata edits or deletions.
        :type results_updated_since: datetime, optional
        :param search: Find experiments whose names contain the search text, regardless of case.
        :type search: str, optional
        :param sort: Sort fields: name, created_at, or updated_at. Use a comma-separated list in priority order, for example name,-created_at. Prefix each field with ``-`` for descending. Defaults to created_at descending.
        :type sort: str, optional
        :param status: Filter by experiment status. Accepted values are DRAFT, SCHEDULED, IN_PROGRESS, READY_FOR_DECISION,
            DECISION_MADE, and CANCELLED. Repeat this parameter to select several statuses, for example
            ``status=IN_PROGRESS&status=READY_FOR_DECISION``.
        :type status: [str], optional
        :param tags: Filter by tag name. Repeat this parameter to supply several tags. An experiment matches if it has at least
            one listed tag.
        :type tags: [str], optional
        :rtype: ExperimentsExperimentV2ListDTOArray
        """
        kwargs: Dict[str, Any] = {}
        if concluded_since is not unset:
            kwargs["concluded_since"] = concluded_since

        if created_since is not unset:
            kwargs["created_since"] = created_since

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if protocol_id is not unset:
            kwargs["protocol_id"] = protocol_id

        if results_updated_before is not unset:
            kwargs["results_updated_before"] = results_updated_before

        if results_updated_since is not unset:
            kwargs["results_updated_since"] = results_updated_since

        if search is not unset:
            kwargs["search"] = search

        if sort is not unset:
            kwargs["sort"] = sort

        if status is not unset:
            kwargs["status"] = status

        if tags is not unset:
            kwargs["tags"] = tags

        return self._list_experiments_endpoint.call_with_http_info(**kwargs)

    def list_exposure_sql_models(
        self,
        *,
        include: Union[List[str], UnsetType] = unset,
        include_archived: Union[bool, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        search: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
    ) -> ExperimentsExposureSQLModelV2DTOArray:
        """List exposure SQL models.

        List exposure SQL models. Returns a paginated list of the SQL models that experiment exposures are read from for the organization. Models maintained by Datadog are not included: they cannot be modified and cannot be used as an experiment's assignment source.

        :param include: Optional fields to include. Repeat this parameter to request several fields. ``counts`` adds
            experiment_count, which costs an extra aggregate query.
        :type include: [str], optional
        :param include_archived: When true, archived models are included in the result. Defaults to false, so archived models are hidden.
        :type include_archived: bool, optional
        :param page_limit: Maximum number of results to return. Defaults to 25 when omitted, and is capped at 50 (larger values are clamped to 50). The response includes meta.page (with total) and pagination links.
        :type page_limit: int, optional
        :param page_offset: Number of results to skip for pagination. Defaults to 0 when omitted.
        :type page_offset: int, optional
        :param search: Find exposure SQL models whose names contain the search text, regardless of case.
        :type search: str, optional
        :param sort: Sort field: name, created_at, or updated_at. Prefix with ``-`` for descending (for example, ``-created_at`` ).
            Defaults to created_at descending.
        :type sort: str, optional
        :rtype: ExperimentsExposureSQLModelV2DTOArray
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        if include_archived is not unset:
            kwargs["include_archived"] = include_archived

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if search is not unset:
            kwargs["search"] = search

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_exposure_sql_models_endpoint.call_with_http_info(**kwargs)

    def list_metric_collections(
        self,
        *,
        include: Union[List[str], UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        search: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
    ) -> ExperimentsMetricCollectionV2DTOArray:
        """List metric collections.

        List metric collections for the organization. Collections are reusable ordered metric sets; attaching one to an experiment creates an independent snapshot.

        :param include: Optional fields to include. Repeat this parameter to request several fields. ``counts`` adds metric_count.
        :type include: [str], optional
        :param page_limit: Number of results per page. The default is 25. Values above 50 are reduced to 50.
        :type page_limit: int, optional
        :param page_offset: Number of results to skip before returning this page.
        :type page_offset: int, optional
        :param search: Find collections whose names contain the search text, regardless of case. Leading and trailing spaces are
            ignored. Blank values apply no filter. The maximum length is 1024 UTF-8 bytes.
        :type search: str, optional
        :param sort: Sort by one field: ``name`` , ``created_at`` , or ``updated_at``. Prefix with ``-`` for descending order. The
            default is ``-created_at``.
        :type sort: str, optional
        :rtype: ExperimentsMetricCollectionV2DTOArray
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if search is not unset:
            kwargs["search"] = search

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_metric_collections_endpoint.call_with_http_info(**kwargs)

    def list_metrics(
        self,
        *,
        include: Union[List[str], UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        search: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
    ) -> ExperimentsMetricV2DTOArray:
        """List metrics.

        List metrics. Returns a paginated list of the experiment metrics defined for the organization.

        :param include: Optional fields to include. Repeat this parameter to request several fields. ``counts`` adds
            experiment_count on each metric, which costs an extra aggregate query.
        :type include: [str], optional
        :param page_limit: Maximum number of results to return. Defaults to 25 when omitted, and is capped at 50 (larger values are clamped to 50). The response includes meta.page (with total) and pagination links.
        :type page_limit: int, optional
        :param page_offset: Number of results to skip for pagination. Defaults to 0 when omitted.
        :type page_offset: int, optional
        :param search: Find metrics whose names contain the search text, regardless of case.
        :type search: str, optional
        :param sort: Sort field: name, created_at, or updated_at. Prefix with ``-`` for descending (for example, ``-created_at`` ).
            A single field only; a comma-separated list is rejected. Defaults to created_at descending.
        :type sort: str, optional
        :rtype: ExperimentsMetricV2DTOArray
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if search is not unset:
            kwargs["search"] = search

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_metrics_endpoint.call_with_http_info(**kwargs)

    def list_metric_sql_models(
        self,
        *,
        include: Union[List[str], UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
    ) -> ExperimentsMetricSQLModelV2DTOArray:
        """List metric SQL models.

        List metric SQL models. Returns a paginated list of the SQL models that metrics are defined on for the organization.

        :param include: Optional fields to include. Repeat this parameter to request several fields. ``counts`` adds metric_count
            and experiment_count, which cost an extra aggregate query.
        :type include: [str], optional
        :param page_limit: Maximum number of results to return. Defaults to 25 when omitted, and is capped at 50 (larger values are clamped to 50). The response includes meta.page (with total) and pagination links.
        :type page_limit: int, optional
        :param page_offset: Number of results to skip for pagination. Defaults to 0 when omitted.
        :type page_offset: int, optional
        :param sort: Sort field: name, created_at, updated_at, metric_count, or experiment_count. A single field only; a
            comma-separated list is rejected. Prefix with ``-`` for descending (for example, ``-created_at`` ). Defaults to
            created_at descending.
        :type sort: str, optional
        :rtype: ExperimentsMetricSQLModelV2DTOArray
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_metric_sql_models_endpoint.call_with_http_info(**kwargs)

    def list_subject_types(
        self,
        *,
        include: Union[str, UnsetType] = unset,
        page_limit: Union[int, UnsetType] = unset,
        page_offset: Union[int, UnsetType] = unset,
        search: Union[str, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
    ) -> ExperimentsSubjectTypeV2DTOArray:
        """List subject types.

        List subject types. Returns a paginated list of the subject types defined for the organization.

        :param include: Set to ``counts`` to add experiment_count, exposure_source_count, metric_sql_model_count and protocol_count to each subject type. Each costs an extra query, so they are omitted unless asked for.
        :type include: str, optional
        :param page_limit: Maximum number of results to return. Defaults to 25 when omitted, and is capped at 50 (larger values are clamped to 50). The response includes meta.page (with total) and pagination links.
        :type page_limit: int, optional
        :param page_offset: Number of results to skip for pagination. Defaults to 0 when omitted.
        :type page_offset: int, optional
        :param search: Find subject types whose names contain the search text, regardless of case.
        :type search: str, optional
        :param sort: Sort fields: name, created_at, or updated_at. Use a comma-separated list in priority order, for example name,-created_at. Prefix each field with ``-`` for descending. Defaults to created_at descending.
        :type sort: str, optional
        :rtype: ExperimentsSubjectTypeV2DTOArray
        """
        kwargs: Dict[str, Any] = {}
        if include is not unset:
            kwargs["include"] = include

        if page_limit is not unset:
            kwargs["page_limit"] = page_limit

        if page_offset is not unset:
            kwargs["page_offset"] = page_offset

        if search is not unset:
            kwargs["search"] = search

        if sort is not unset:
            kwargs["sort"] = sort

        return self._list_subject_types_endpoint.call_with_http_info(**kwargs)

    def patch_experiment(
        self,
        experiment_id: UUID,
        body: ExperimentsPatchExperimentV2Request,
    ) -> ExperimentsPatchExperimentV2Response:
        """Patch experiment.

        Update mutable experiment fields. State and protocol restrictions apply.

        **PATCH behavior**

        * Omitted fields stay unchanged, including fields inside ``datadog_flag_configuration``.
        * Supplied ``tags`` , ``teams`` , ``related_links`` , ``decision_metrics`` , and ``variants`` replace their stored lists.
        * Validation can return several field errors before saving any changes. The response is HTTP 400 if any error
          concerns invalid input. It is HTTP 409 if all errors concern state or protocol conflicts.

        **Result refreshes**

        This endpoint does not start a pipeline run. ``meta.needs_pipeline_refresh`` states whether the edit requires a
        run. When true, POST to ``meta.refresh_endpoint`` after finishing your edits. Its ``full_refresh`` query parameter
        selects the run type.

        Keep refresh requirements across edits. A later false value does not clear an earlier requirement. Any
        ``full_refresh=true`` requirement takes priority.

        After start, STATIC and STEPS exposure changes for warehouse experiments without a Datadog flag attempt to
        recalculate stored results. Changes to decision metrics or the control variant also attempt recalculation when
        results exist. If stored data is insufficient or recalculation fails, the edit stays saved and
        ``meta.needs_pipeline_refresh`` is true.

        **Exposure rules**

        * Draft experiments can replace the full STATIC or STEPS plan through ``traffic_exposure``.
        * Warehouse steps start at ``assignments_start_date`` and can have different durations.
        * Running warehouse experiments can replace step fractions, durations, and exposure mode. Retained variant
          weights cannot change through this API. You can send unchanged values again.
        * After a warehouse experiment ends, configuration replacement supports only STATIC fraction changes.
        * New Datadog plans have at most five steps. The first fraction must be positive. All steps except the last
          have equal durations. Durations exclude pauses.
        * The last step has a null duration. Its fraction stays in effect until assignment ends.
        * After start, use the experiment UI to change traffic exposure for experiments linked to a Datadog flag.

        **Metadata**

        ``structured_metadata`` updates fields by ``field_key``. Use ``freetext_value: ""`` or ``enum_values: []`` to clear an
        optional field. Omitted fields stay unchanged. A null or empty ``structured_metadata`` attribute makes no
        change.

        **Flag changes**

        Before start, a Datadog update creates or edits the saved draft allocation. To add or replace a flag, send
        ``variants`` and ``traffic_exposure``. Inside ``datadog_flag_configuration`` , send ``feature_flag_id`` ,
        ``environment_id`` , ``targeting_rules`` , and ``entry_point``. Use ``targeting_rules: []`` and ``entry_point: null`` when
        unused.

        To replace a flag, also set ``reset_on_feature_flag_change: true`` inside that object. The server deletes the
        old draft and creates a new one in the same transaction. The response includes a
        ``datadog_flag_configuration_reset`` warning in ``meta.warnings``.

        Set ``datadog_flag_configuration: null`` to delete the draft allocation. This also clears the experiment's flag
        association, variants, assignment sources, and entry point. The experiment remains.

        Flag replacement and removal require a draft experiment without warehouse exposure. These actions do not
        convert hybrid experiments.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :type body: ExperimentsPatchExperimentV2Request
        :rtype: ExperimentsPatchExperimentV2Response
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        kwargs["body"] = body

        return self._patch_experiment_endpoint.call_with_http_info(**kwargs)

    def patch_subject_type(
        self,
        subject_type_id: UUID,
        body: ExperimentsPatchSubjectTypeV2Request,
    ) -> ExperimentsSubjectTypeV2DTO:
        """Patch subject type.

        Update mutable fields on a subject type. Only the fields present in the body are changed. Any subject type can be updated, including the organization's default one, but the is_default flag itself is read-only here: which subject type is the default cannot be changed through this endpoint.

        :param subject_type_id: The UUID of the subject type.
        :type subject_type_id: UUID
        :type body: ExperimentsPatchSubjectTypeV2Request
        :rtype: ExperimentsSubjectTypeV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["subject_type_id"] = subject_type_id

        kwargs["body"] = body

        return self._patch_subject_type_endpoint.call_with_http_info(**kwargs)

    def refresh_experiment_results(
        self,
        experiment_id: UUID,
        *,
        full_refresh: Union[bool, UnsetType] = unset,
    ) -> ExperimentsRefreshExperimentResultsV2DTO:
        """Refresh experiment results.

        Request a results refresh for one experiment. HTTP 202 confirms acceptance, not completed results. The response identifies the experiment and does not include a job ID. Read experiment results to check freshness. A request while a refresh is queued or running returns 409. After completion, another request can start another refresh.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :param full_refresh: Force a full warehouse rebuild. Defaults to false when omitted.
        :type full_refresh: bool, optional
        :rtype: ExperimentsRefreshExperimentResultsV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        if full_refresh is not unset:
            kwargs["full_refresh"] = full_refresh

        return self._refresh_experiment_results_endpoint.call_with_http_info(**kwargs)

    def refresh_experiment_results_for_org(
        self,
        *,
        full_refresh: Union[bool, UnsetType] = unset,
    ) -> ExperimentsRefreshExperimentResultsV2DTOArray:
        """Refresh experiment results for org.

        Trigger a results refresh across the organization's active experiments. Returns the count of experiments whose refresh was triggered (meta.experiments_updated) plus a per-experiment breakdown of what happened to each (meta.results).

        :param full_refresh: Force a full warehouse rebuild. Defaults to false when omitted.
        :type full_refresh: bool, optional
        :rtype: ExperimentsRefreshExperimentResultsV2DTOArray
        """
        kwargs: Dict[str, Any] = {}
        if full_refresh is not unset:
            kwargs["full_refresh"] = full_refresh

        return self._refresh_experiment_results_for_org_endpoint.call_with_http_info(**kwargs)

    def set_default_subject_type(
        self,
        subject_type_id: UUID,
    ) -> None:
        """Set default subject type.

        Make this subject type the organization's default. Experiment creation uses the default when the request names no subject type. Promoting one subject type demotes the previous default in the same transaction, so the organization always has exactly one. The call is idempotent: promoting the current default succeeds and changes nothing. There is no matching demote, because an organization cannot have no default; promote a different subject type instead.

        :param subject_type_id: The UUID of the subject type.
        :type subject_type_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["subject_type_id"] = subject_type_id

        return self._set_default_subject_type_endpoint.call_with_http_info(**kwargs)

    def start_experiment(
        self,
        experiment_id: UUID,
        *,
        body: Union[ExperimentsStartExperimentV2Request, UnsetType] = unset,
    ) -> None:
        """Start experiment.

        Start an experiment. The experiment is started exactly as it is configured; this endpoint accepts no attributes, and a request body carrying any is rejected rather than ignored. Set the run window, duration, or variants with PATCH /api/v2/experiments/{experiment_id} before starting. An unconfigured draft returns HTTP 409. Configure either warehouse_exposure_configuration or datadog_flag_configuration, plus the required experiment fields, before starting. Start validation errors can include meta.configuration_pointer to identify a field on the experiment to correct. For a flag-backed experiment this enables the linked feature flag's environment, clears any stored variant override on it, and starts the allocation's rollout. The request is idempotent: an experiment that is already running or ready for a decision still returns 204, so a retry after a timeout is safe. One exception: an experiment scheduled to start is accepted only when it is backed by your own feature flag; a Datadog-flag experiment in that state returns 409 because its stored state and flag allocation disagree. Cancel and conclude are not idempotent and return 409 when repeated.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :type body: ExperimentsStartExperimentV2Request, optional
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        if body is not unset:
            kwargs["body"] = body

        return self._start_experiment_endpoint.call_with_http_info(**kwargs)

    def unarchive_exposure_sql_model(
        self,
        exposure_sql_model_id: UUID,
    ) -> None:
        """Unarchive exposure SQL model.

        Unarchive an exposure SQL model. Restores an archived model to the default list.

        :param exposure_sql_model_id: The UUID of the exposure SQL model.
        :type exposure_sql_model_id: UUID
        :rtype: None
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exposure_sql_model_id"] = exposure_sql_model_id

        return self._unarchive_exposure_sql_model_endpoint.call_with_http_info(**kwargs)

    def update_experiment_analysis_plan_attributes(
        self,
        experiment_id: UUID,
        body: ExperimentsAnalysisPlanWriteV2Request,
    ) -> ExperimentsAnalysisPlanV2MutationResponse:
        """Update experiment analysis plan attributes.

        Update selected statistical analysis settings. Omitted attributes remain unchanged and nullable attributes can be cleared with null. Protocol-locked settings cannot be changed.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :type body: ExperimentsAnalysisPlanWriteV2Request
        :rtype: ExperimentsAnalysisPlanV2MutationResponse
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        kwargs["body"] = body

        return self._update_experiment_analysis_plan_attributes_endpoint.call_with_http_info(**kwargs)

    def update_experiment_metric_group(
        self,
        experiment_id: UUID,
        metric_group_id: UUID,
        body: ExperimentsPatchExperimentMetricGroupV2Request,
    ) -> ExperimentsExperimentMetricGroupMutationV2:
        """Update experiment metric group.

        Update a non-decision metric group. Omitted attributes are unchanged; a supplied metrics array is the complete ordered replacement. Decision groups remain managed through the experiment resource. This operation does not synchronously recompute results.

        :param experiment_id: The UUID of the experiment.
        :type experiment_id: UUID
        :param metric_group_id: The UUID of the metric group.
        :type metric_group_id: UUID
        :type body: ExperimentsPatchExperimentMetricGroupV2Request
        :rtype: ExperimentsExperimentMetricGroupMutationV2
        """
        kwargs: Dict[str, Any] = {}
        kwargs["experiment_id"] = experiment_id

        kwargs["metric_group_id"] = metric_group_id

        kwargs["body"] = body

        return self._update_experiment_metric_group_endpoint.call_with_http_info(**kwargs)

    def update_exposure_sql_model(
        self,
        exposure_sql_model_id: UUID,
        body: ExperimentsCreateExposureSQLModelV2Request,
        *,
        include: Union[List[str], UnsetType] = unset,
    ) -> ExperimentsUpdateExposureSQLModelV2Response:
        """Update exposure SQL model.

        Replace an exposure SQL model. This is a full replacement and is destructive: any subject type or property not present in the body is deleted, and properties are matched on name, column_name and column_type together, so changing one of those replaces the property rather than editing it. Send the complete set you want to keep. Anything removed is listed under meta.removed_subject_type_ids and meta.removed_property_names in the response. The warehouse connection is not settable and is left as stored.

        :param exposure_sql_model_id: The UUID of the exposure SQL model.
        :type exposure_sql_model_id: UUID
        :type body: ExperimentsCreateExposureSQLModelV2Request
        :param include: Optional fields to include. Repeat this parameter to request several fields. ``counts`` adds
            experiment_count to the updated model.
        :type include: [str], optional
        :rtype: ExperimentsUpdateExposureSQLModelV2Response
        """
        kwargs: Dict[str, Any] = {}
        kwargs["exposure_sql_model_id"] = exposure_sql_model_id

        if include is not unset:
            kwargs["include"] = include

        kwargs["body"] = body

        return self._update_exposure_sql_model_endpoint.call_with_http_info(**kwargs)

    def update_metric(
        self,
        metric_id: UUID,
        body: ExperimentsUpdateMetricV2Request,
    ) -> ExperimentsMetricV2DTO:
        """Update metric.

        Update a metric. Certified metrics are read-only through this endpoint. This is a partial update: every attribute is optional and an omitted attribute keeps its stored value, so a body carrying only the fields being changed is enough. ``guardrail_cutoff_threshold`` is nullable -- send null to clear it, omit it to leave it alone. Omitting the aggregation leaves the metric's definition untouched; supplying one replaces it wholesale, and the metric's type is re-derived from the shape supplied. Property filters use property_id or measure_id UUIDs from the aggregation's data source. Attributes that are computed rather than stored (short_id, metric_type, certified_at, experiment_count, created_at, updated_at) are rejected rather than ignored, so a body copied from GET must have them removed. The is_certified attribute is rejected. Certification cannot be changed through this endpoint.

        :param metric_id: The UUID of the metric.
        :type metric_id: UUID
        :type body: ExperimentsUpdateMetricV2Request
        :rtype: ExperimentsMetricV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_id"] = metric_id

        kwargs["body"] = body

        return self._update_metric_endpoint.call_with_http_info(**kwargs)

    def update_metric_collection(
        self,
        metric_collection_id: UUID,
        body: ExperimentsPatchMetricCollectionV2Request,
    ) -> ExperimentsMetricCollectionV2DTO:
        """Update metric collection.

        Update metric collection.

        :param metric_collection_id: The UUID of the metric collection.
        :type metric_collection_id: UUID
        :type body: ExperimentsPatchMetricCollectionV2Request
        :rtype: ExperimentsMetricCollectionV2DTO
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_collection_id"] = metric_collection_id

        kwargs["body"] = body

        return self._update_metric_collection_endpoint.call_with_http_info(**kwargs)

    def update_metric_sql_model(
        self,
        metric_sql_model_id: UUID,
        body: ExperimentsCreateMetricSQLModelV2Request,
    ) -> ExperimentsUpdateMetricSQLModelV2Response:
        """Update metric SQL model.

        Replace a metric SQL model. This is a destructive full replace: subject types, customer-defined measures, and properties absent from the body are deleted, so send the complete set. Properties are matched by name; changing a property's column, type, or description preserves its ID. column_type is required for every measure and property. Removing a measure or property that an active metric references returns 409 Conflict. Server-generated IDs returned by GET are read-only and can be left in a replayed body. The response reports removals in meta.deleted_subject_types, meta.deleted_measures, and meta.deleted_properties. Certification is read-only. Certified models cannot be replaced through this endpoint.

        :param metric_sql_model_id: The UUID of the metric SQL model.
        :type metric_sql_model_id: UUID
        :type body: ExperimentsCreateMetricSQLModelV2Request
        :rtype: ExperimentsUpdateMetricSQLModelV2Response
        """
        kwargs: Dict[str, Any] = {}
        kwargs["metric_sql_model_id"] = metric_sql_model_id

        kwargs["body"] = body

        return self._update_metric_sql_model_endpoint.call_with_http_info(**kwargs)
