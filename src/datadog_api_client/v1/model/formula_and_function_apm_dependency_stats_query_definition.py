# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.formula_and_function_apm_dependency_stats_data_source import (
        FormulaAndFunctionApmDependencyStatsDataSource,
    )
    from datadog_api_client.v1.model.formula_and_function_apm_dependency_stat_name import (
        FormulaAndFunctionApmDependencyStatName,
    )

    globals()["FormulaAndFunctionApmDependencyStatsDataSource"] = FormulaAndFunctionApmDependencyStatsDataSource
    globals()["FormulaAndFunctionApmDependencyStatName"] = FormulaAndFunctionApmDependencyStatName


class FormulaAndFunctionApmDependencyStatsQueryDefinition(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "data_source": (FormulaAndFunctionApmDependencyStatsDataSource,),
            "env": (str,),
            "is_upstream": (bool,),
            "name": (str,),
            "operation_name": (str,),
            "primary_tag_name": (str,),
            "primary_tag_value": (str,),
            "resource_name": (str,),
            "service": (str,),
            "stat": (FormulaAndFunctionApmDependencyStatName,),
        }

    attribute_map = {
        "data_source": "data_source",
        "env": "env",
        "is_upstream": "is_upstream",
        "name": "name",
        "operation_name": "operation_name",
        "primary_tag_name": "primary_tag_name",
        "primary_tag_value": "primary_tag_value",
        "resource_name": "resource_name",
        "service": "service",
        "stat": "stat",
    }

    read_only_vars = {}

    def __init__(self, data_source, env, name, operation_name, resource_name, service, stat, *args, **kwargs):
        """
        A formula and functions APM dependency stats query.

        :param data_source: Data source for APM dependency stats queries.
        :type data_source: FormulaAndFunctionApmDependencyStatsDataSource

        :param env: APM environment.
        :type env: str

        :param is_upstream: Determines whether stats for upstream or downstream dependencies should be queried.
        :type is_upstream: bool, optional

        :param name: Name of query to use in formulas.
        :type name: str

        :param operation_name: Name of operation on service.
        :type operation_name: str

        :param primary_tag_name: The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog.
        :type primary_tag_name: str, optional

        :param primary_tag_value: Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
        :type primary_tag_value: str, optional

        :param resource_name: APM resource.
        :type resource_name: str

        :param service: APM service.
        :type service: str

        :param stat: APM statistic.
        :type stat: FormulaAndFunctionApmDependencyStatName
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data_source = data_source
        self.env = env
        self.name = name
        self.operation_name = operation_name
        self.resource_name = resource_name
        self.service = service
        self.stat = stat

    @classmethod
    def _from_openapi_data(cls, data_source, env, name, operation_name, resource_name, service, stat, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FormulaAndFunctionApmDependencyStatsQueryDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data_source = data_source
        self.env = env
        self.name = name
        self.operation_name = operation_name
        self.resource_name = resource_name
        self.service = service
        self.stat = stat
        return self
