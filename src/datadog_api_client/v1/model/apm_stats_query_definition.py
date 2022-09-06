# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ApmStatsQueryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.apm_stats_query_column_type import ApmStatsQueryColumnType
        from datadog_api_client.v1.model.apm_stats_query_row_type import ApmStatsQueryRowType

        return {
            "columns": ([ApmStatsQueryColumnType],),
            "env": (str,),
            "name": (str,),
            "primary_tag": (str,),
            "resource": (str,),
            "row_type": (ApmStatsQueryRowType,),
            "service": (str,),
        }

    attribute_map = {
        "columns": "columns",
        "env": "env",
        "name": "name",
        "primary_tag": "primary_tag",
        "resource": "resource",
        "row_type": "row_type",
        "service": "service",
    }

    def __init__(self_, env, name, primary_tag, row_type, service, *args, **kwargs):
        """
        The APM stats query for table and distributions widgets.

        :param columns: Column properties used by the front end for display.
        :type columns: [ApmStatsQueryColumnType], optional

        :param env: Environment name.
        :type env: str

        :param name: Operation name associated with service.
        :type name: str

        :param primary_tag: The organization's host group name and value.
        :type primary_tag: str

        :param resource: Resource name.
        :type resource: str, optional

        :param row_type: The level of detail for the request.
        :type row_type: ApmStatsQueryRowType

        :param service: Service name.
        :type service: str
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.env = env
        self_.name = name
        self_.primary_tag = primary_tag
        self_.row_type = row_type
        self_.service = service
