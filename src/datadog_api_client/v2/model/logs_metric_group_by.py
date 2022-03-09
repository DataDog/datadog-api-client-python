# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsMetricGroupBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "path": (str,),
            "tag_name": (str,),
        }

    attribute_map = {
        "path": "path",
        "tag_name": "tag_name",
    }

    def __init__(self, path, *args, **kwargs):
        """
        A group by rule.

        :param path: The path to the value the log-based metric will be aggregated over.
        :type path: str

        :param tag_name: Eventual name of the tag that gets created. By default, the path attribute is used as the tag name.
        :type tag_name: str, optional
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
