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
    from datadog_api_client.v1.model.monitor_formula_and_function_data_jobs_monitor_options import (
        MonitorFormulaAndFunctionDataJobsMonitorOptions,
    )


class MonitorFormulaAndFunctionDataJobsQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_data_jobs_monitor_options import (
            MonitorFormulaAndFunctionDataJobsMonitorOptions,
        )

        return {
            "job_type": (str,),
            "jobs_query": (str,),
            "monitor_options": (MonitorFormulaAndFunctionDataJobsMonitorOptions,),
            "name": (str,),
            "query_dialect": (str,),
            "run_filter": (str,),
        }

    attribute_map = {
        "job_type": "job_type",
        "jobs_query": "jobs_query",
        "monitor_options": "monitor_options",
        "name": "name",
        "query_dialect": "query_dialect",
        "run_filter": "run_filter",
    }

    def __init__(
        self_,
        job_type: str,
        jobs_query: str,
        name: str,
        query_dialect: str,
        monitor_options: Union[MonitorFormulaAndFunctionDataJobsMonitorOptions, UnsetType] = unset,
        run_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A formula and functions data jobs query.

        :param job_type: The type of job being monitored. Valid values include:
            ``databricks.job`` , ``spark.application`` , ``airflow.dag`` , ``dbt.job`` , ``glue.job`` , ``adf.pipeline``.
            The ``aastra`` dialect also accepts ``airflow.job`` , ``dbt.model`` , and ``dbt.test``.
            Custom job types are supported with the ``custom.ol.`` prefix.
        :type job_type: str

        :param jobs_query: Filter expression used to select the jobs to monitor. Its syntax depends on ``query_dialect`` :
            a metric tag filter such as ``job_name:smoke*`` for ``metric`` , or an Aastra entity search
            such as ``search for databricks_job where `@team:data-eng` `` for ``aastra``.
        :type jobs_query: str

        :param monitor_options: Monitor configuration options for data jobs queries.
        :type monitor_options: MonitorFormulaAndFunctionDataJobsMonitorOptions, optional

        :param name: Name of the query for use in formulas. Must be ``run_query``.
        :type name: str

        :param query_dialect: Query dialect for data jobs queries. Valid values are ``metric`` and ``aastra``.
        :type query_dialect: str

        :param run_filter: Optional filter on individual runs, using metrics filter syntax.
            Only supported with the ``aastra`` query dialect.
        :type run_filter: str, optional
        """
        if monitor_options is not unset:
            kwargs["monitor_options"] = monitor_options
        if run_filter is not unset:
            kwargs["run_filter"] = run_filter
        super().__init__(kwargs)

        self_.job_type = job_type
        self_.jobs_query = jobs_query
        self_.name = name
        self_.query_dialect = query_dialect
