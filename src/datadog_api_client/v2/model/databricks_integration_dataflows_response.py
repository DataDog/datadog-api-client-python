# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.databricks_cloud_cost_metrics_integration_dataflow_response import (
        DatabricksCloudCostMetricsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.databricks_data_job_monitoring_integration_dataflow_response import (
        DatabricksDataJobMonitoringIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.databricks_data_observability_integration_dataflow_response import (
        DatabricksDataObservabilityIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.databricks_model_serving_metrics_integration_dataflow_response import (
        DatabricksModelServingMetricsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.databricks_serverless_jobs_integration_dataflow_response import (
        DatabricksServerlessJobsIntegrationDataflowResponse,
    )


class DatabricksIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_cloud_cost_metrics_integration_dataflow_response import (
            DatabricksCloudCostMetricsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.databricks_data_job_monitoring_integration_dataflow_response import (
            DatabricksDataJobMonitoringIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.databricks_data_observability_integration_dataflow_response import (
            DatabricksDataObservabilityIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.databricks_model_serving_metrics_integration_dataflow_response import (
            DatabricksModelServingMetricsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.databricks_serverless_jobs_integration_dataflow_response import (
            DatabricksServerlessJobsIntegrationDataflowResponse,
        )

        return {
            "databricks_cloud_cost_metrics": (DatabricksCloudCostMetricsIntegrationDataflowResponse,),
            "databricks_data_job_monitoring": (DatabricksDataJobMonitoringIntegrationDataflowResponse,),
            "databricks_data_observability": (DatabricksDataObservabilityIntegrationDataflowResponse,),
            "databricks_model_serving_metrics": (DatabricksModelServingMetricsIntegrationDataflowResponse,),
            "databricks_serverless_jobs": (DatabricksServerlessJobsIntegrationDataflowResponse,),
        }

    attribute_map = {
        "databricks_cloud_cost_metrics": "databricks-cloud-cost-metrics",
        "databricks_data_job_monitoring": "databricks-data-job-monitoring",
        "databricks_data_observability": "databricks-data-observability",
        "databricks_model_serving_metrics": "databricks-model-serving-metrics",
        "databricks_serverless_jobs": "databricks-serverless-jobs",
    }

    def __init__(
        self_,
        databricks_cloud_cost_metrics: Union[DatabricksCloudCostMetricsIntegrationDataflowResponse, UnsetType] = unset,
        databricks_data_job_monitoring: Union[
            DatabricksDataJobMonitoringIntegrationDataflowResponse, UnsetType
        ] = unset,
        databricks_data_observability: Union[DatabricksDataObservabilityIntegrationDataflowResponse, UnsetType] = unset,
        databricks_model_serving_metrics: Union[
            DatabricksModelServingMetricsIntegrationDataflowResponse, UnsetType
        ] = unset,
        databricks_serverless_jobs: Union[DatabricksServerlessJobsIntegrationDataflowResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Dataflows configured on the Databricks integration account, keyed by dataflow id.

        :param databricks_cloud_cost_metrics: The Databricks cloud cost metrics dataflow.
        :type databricks_cloud_cost_metrics: DatabricksCloudCostMetricsIntegrationDataflowResponse, optional

        :param databricks_data_job_monitoring: The Databricks Data Jobs Monitoring dataflow.
        :type databricks_data_job_monitoring: DatabricksDataJobMonitoringIntegrationDataflowResponse, optional

        :param databricks_data_observability: The Databricks data observability dataflow.
        :type databricks_data_observability: DatabricksDataObservabilityIntegrationDataflowResponse, optional

        :param databricks_model_serving_metrics: The Databricks model serving metrics dataflow. Not supported on accounts that authenticate with ``private-action-runner`` ; on those accounts this dataflow collects no data even when enabled.
        :type databricks_model_serving_metrics: DatabricksModelServingMetricsIntegrationDataflowResponse, optional

        :param databricks_serverless_jobs: The Databricks serverless jobs dataflow.
        :type databricks_serverless_jobs: DatabricksServerlessJobsIntegrationDataflowResponse, optional
        """
        if databricks_cloud_cost_metrics is not unset:
            kwargs["databricks_cloud_cost_metrics"] = databricks_cloud_cost_metrics
        if databricks_data_job_monitoring is not unset:
            kwargs["databricks_data_job_monitoring"] = databricks_data_job_monitoring
        if databricks_data_observability is not unset:
            kwargs["databricks_data_observability"] = databricks_data_observability
        if databricks_model_serving_metrics is not unset:
            kwargs["databricks_model_serving_metrics"] = databricks_model_serving_metrics
        if databricks_serverless_jobs is not unset:
            kwargs["databricks_serverless_jobs"] = databricks_serverless_jobs
        super().__init__(kwargs)
