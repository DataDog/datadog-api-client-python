# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsMetricGroupBy(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "path": (str,),
            "tag_name": (str,),
        }

    attribute_map = {
        "path": "path",
        "tag_name": "tag_name",
    }

    read_only_vars = {}

    def __init__(self, path, *args, **kwargs):
        """LogsMetricGroupBy - a model defined in OpenAPI

        Args:
            path (str): The path to the value the log-based metric will be aggregated over.

        Keyword Args:
            tag_name (str): [optional] Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.path = path

    @classmethod
    def _from_openapi_data(cls, path, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsMetricGroupBy, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.path = path
        return self
