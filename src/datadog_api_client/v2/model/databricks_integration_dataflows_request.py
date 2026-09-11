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
    from datadog_api_client.v2.model.databricks_cloud_cost_metrics_integration_dataflow_request import (
        DatabricksCloudCostMetricsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.databricks_data_observability_jobs_monitoring_integration_dataflow_request import (
        DatabricksDataObservabilityJobsMonitoringIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.databricks_data_observability_quality_monitoring_integration_dataflow_request import (
        DatabricksDataObservabilityQualityMonitoringIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.databricks_model_serving_metrics_integration_dataflow_request import (
        DatabricksModelServingMetricsIntegrationDataflowRequest,
    )


class DatabricksIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_cloud_cost_metrics_integration_dataflow_request import (
            DatabricksCloudCostMetricsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.databricks_data_observability_jobs_monitoring_integration_dataflow_request import (
            DatabricksDataObservabilityJobsMonitoringIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.databricks_data_observability_quality_monitoring_integration_dataflow_request import (
            DatabricksDataObservabilityQualityMonitoringIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.databricks_model_serving_metrics_integration_dataflow_request import (
            DatabricksModelServingMetricsIntegrationDataflowRequest,
        )

        return {
            "databricks_cloud_cost_metrics": (DatabricksCloudCostMetricsIntegrationDataflowRequest,),
            "databricks_data_observability_jobs_monitoring": (
                DatabricksDataObservabilityJobsMonitoringIntegrationDataflowRequest,
            ),
            "databricks_data_observability_quality_monitoring": (
                DatabricksDataObservabilityQualityMonitoringIntegrationDataflowRequest,
            ),
            "databricks_model_serving_metrics": (DatabricksModelServingMetricsIntegrationDataflowRequest,),
        }

    attribute_map = {
        "databricks_cloud_cost_metrics": "databricks-cloud-cost-metrics",
        "databricks_data_observability_jobs_monitoring": "databricks-data-observability-jobs-monitoring",
        "databricks_data_observability_quality_monitoring": "databricks-data-observability-quality-monitoring",
        "databricks_model_serving_metrics": "databricks-model-serving-metrics",
    }

    def __init__(
        self_,
        databricks_cloud_cost_metrics: Union[DatabricksCloudCostMetricsIntegrationDataflowRequest, UnsetType] = unset,
        databricks_data_observability_jobs_monitoring: Union[
            DatabricksDataObservabilityJobsMonitoringIntegrationDataflowRequest, UnsetType
        ] = unset,
        databricks_data_observability_quality_monitoring: Union[
            DatabricksDataObservabilityQualityMonitoringIntegrationDataflowRequest, UnsetType
        ] = unset,
        databricks_model_serving_metrics: Union[
            DatabricksModelServingMetricsIntegrationDataflowRequest, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Databricks, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it, and use ``settings`` to tune what it gathers. The defaults noted below apply when the account is created; on update, anything left out keeps its current value. Some dataflows have prerequisites, noted on each; unless one is documented as rejecting the request, it is not verified, so a dataflow enabled without it is stored but collects no data.

        :param databricks_cloud_cost_metrics: Cost data collected from your Databricks system tables. `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_ must be enabled for your organization while this dataflow is on; any request that leaves it enabled without that is rejected with a ``422`` response.
        :type databricks_cloud_cost_metrics: DatabricksCloudCostMetricsIntegrationDataflowRequest, optional

        :param databricks_data_observability_jobs_monitoring: Data Jobs Monitoring, which collects performance, reliability, and cost data for your Databricks jobs.
        :type databricks_data_observability_jobs_monitoring: DatabricksDataObservabilityJobsMonitoringIntegrationDataflowRequest, optional

        :param databricks_data_observability_quality_monitoring: Data Observability, which collects lineage and data quality information from your Databricks catalogs so you can explore how data flows and detect, resolve, and prevent quality issues.
        :type databricks_data_observability_quality_monitoring: DatabricksDataObservabilityQualityMonitoringIntegrationDataflowRequest, optional

        :param databricks_model_serving_metrics: Health and usage metrics for your Databricks model serving endpoints. Not supported on accounts that authenticate with ``private-action-runner`` ; on those accounts this dataflow collects no data even when enabled.
        :type databricks_model_serving_metrics: DatabricksModelServingMetricsIntegrationDataflowRequest, optional
        """
        if databricks_cloud_cost_metrics is not unset:
            kwargs["databricks_cloud_cost_metrics"] = databricks_cloud_cost_metrics
        if databricks_data_observability_jobs_monitoring is not unset:
            kwargs["databricks_data_observability_jobs_monitoring"] = databricks_data_observability_jobs_monitoring
        if databricks_data_observability_quality_monitoring is not unset:
            kwargs[
                "databricks_data_observability_quality_monitoring"
            ] = databricks_data_observability_quality_monitoring
        if databricks_model_serving_metrics is not unset:
            kwargs["databricks_model_serving_metrics"] = databricks_model_serving_metrics
        super().__init__(kwargs)
