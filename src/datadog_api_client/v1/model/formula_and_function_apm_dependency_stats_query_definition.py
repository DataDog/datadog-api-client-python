# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.formula_and_function_apm_dependency_stat_name import (
        FormulaAndFunctionApmDependencyStatName,
    )
    from datadog_api_client.v1.model.formula_and_function_apm_dependency_stats_data_source import (
        FormulaAndFunctionApmDependencyStatsDataSource,
    )

    globals()["FormulaAndFunctionApmDependencyStatName"] = FormulaAndFunctionApmDependencyStatName
    globals()["FormulaAndFunctionApmDependencyStatsDataSource"] = FormulaAndFunctionApmDependencyStatsDataSource


class FormulaAndFunctionApmDependencyStatsQueryDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

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
        "name": "name",
        "operation_name": "operation_name",
        "resource_name": "resource_name",
        "service": "service",
        "stat": "stat",
        "is_upstream": "is_upstream",
        "primary_tag_name": "primary_tag_name",
        "primary_tag_value": "primary_tag_value",
    }

    read_only_vars = {}

    def __init__(self, data_source, env, name, operation_name, resource_name, service, stat, *args, **kwargs):
        """FormulaAndFunctionApmDependencyStatsQueryDefinition - a model defined in OpenAPI

        Args:
            data_source (FormulaAndFunctionApmDependencyStatsDataSource):
            env (str): APM environment.
            name (str): Name of query to use in formulas.
            operation_name (str): Name of operation on service.
            resource_name (str): APM resource.
            service (str): APM service.
            stat (FormulaAndFunctionApmDependencyStatName):

        Keyword Args:
            is_upstream (bool): [optional] Determines whether stats for upstream or downstream dependencies should be queried.
            primary_tag_name (str): [optional] The name of the second primary tag used within APM; required when `primary_tag_value` is specified. See https://docs.datadoghq.com/tracing/guide/setting_primary_tags_to_scope/#add-a-second-primary-tag-in-datadog.
            primary_tag_value (str): [optional] Filter APM data by the second primary tag. `primary_tag_name` must also be specified.
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
