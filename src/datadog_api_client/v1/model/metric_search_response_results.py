# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricSearchResponseResults(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "metrics": ([str],),
        }

    attribute_map = {
        "metrics": "metrics",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Search result.

        :param metrics: List of metrics that match the search query.
        :type metrics: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricSearchResponseResults, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
