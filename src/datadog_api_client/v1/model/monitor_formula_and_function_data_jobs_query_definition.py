# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorFormulaAndFunctionDataJobsQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "job_type": (str,),
            "jobs_query": (str,),
            "name": (str,),
            "query_dialect": (str,),
        }

    attribute_map = {
        "job_type": "job_type",
        "jobs_query": "jobs_query",
        "name": "name",
        "query_dialect": "query_dialect",
    }

    def __init__(self_, job_type: str, jobs_query: str, name: str, query_dialect: str, **kwargs):
        """
        A formula and functions data jobs query.

        :param job_type: The type of job being monitored. Valid values include:
            ``databricks.job`` , ``spark.application`` , ``airflow.dag`` ,
            ``dbt.job`` , ``dbt.model`` , ``dbt.test`` , ``glue.job``.
            Custom job types are supported with the ``custom.ol.`` prefix.
        :type job_type: str

        :param jobs_query: Filter expression used to select the jobs to monitor.
        :type jobs_query: str

        :param name: Name of the query for use in formulas. Must be ``run_query``.
        :type name: str

        :param query_dialect: Query dialect for data jobs queries. Currently only ``metric`` is supported.
        :type query_dialect: str
        """
        super().__init__(kwargs)

        self_.job_type = job_type
        self_.jobs_query = jobs_query
        self_.name = name
        self_.query_dialect = query_dialect
