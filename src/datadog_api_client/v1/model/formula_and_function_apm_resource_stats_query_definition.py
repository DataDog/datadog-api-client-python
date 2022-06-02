# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FormulaAndFunctionApmResourceStatsQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.formula_and_function_apm_resource_stats_data_source import (
            FormulaAndFunctionApmResourceStatsDataSource,
        )
        from datadog_api_client.v1.model.formula_and_function_apm_resource_stat_name import (
            FormulaAndFunctionApmResourceStatName,
        )

        return {
            "data_source": (FormulaAndFunctionApmResourceStatsDataSource,),
            "env": (str,),
            "group_by": ([str],),
            "name": (str,),
            "operation_name": (str,),
            "primary_tag_name": (str,),
            "primary_tag_value": (str,),
            "resource_name": (str,),
            "service": (str,),
            "stat": (FormulaAndFunctionApmResourceStatName,),
        }

    attribute_map = {
        "data_source": "data_source",
        "env": "env",
        "group_by": "group_by",
        "name": "name",
        "operation_name": "operation_name",
        "primary_tag_name": "primary_tag_name",
        "primary_tag_value": "primary_tag_value",
        "resource_name": "resource_name",
        "service": "service",
        "stat": "stat",
    }

    def __init__(self, data_source, env, name, service, stat, *args, **kwargs):
        """
        APM resource stats query using formulas and functions.

        :param data_source: Data source for APM resource stats queries.
        :type data_source: FormulaAndFunctionApmResourceStatsDataSource

        :param env: APM environment.
        :type env: str

        :param group_by: Array of fields to group results by.
        :type group_by: [str], optional

        :param name: Name of this query to use in formulas.
        :type name: str

        :param operation_name: Name of operation on service.
        :type operation_name: str, optional

        :param primary_tag_name: Name of the second primary tag used within APM. Required when ``primary_tag_value`` is specified. See https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog
        :type primary_tag_name: str, optional

        :param primary_tag_value: Value of the second primary tag by which to filter APM data. ``primary_tag_name`` must also be specified.
        :type primary_tag_value: str, optional

        :param resource_name: APM resource name.
        :type resource_name: str, optional

        :param service: APM service name.
        :type service: str

        :param stat: APM resource stat name.
        :type stat: FormulaAndFunctionApmResourceStatName
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data_source = data_source
        self.env = env
        self.name = name
        self.service = service
        self.stat = stat

    @classmethod
    def _from_openapi_data(cls, data_source, env, name, service, stat, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FormulaAndFunctionApmResourceStatsQueryDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data_source = data_source
        self.env = env
        self.name = name
        self.service = service
        self.stat = stat
        return self
