# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.series import Series

    globals()["Series"] = Series


class MetricsPayload(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "series": ([Series],),
        }

    attribute_map = {
        "series": "series",
    }

    read_only_vars = {}

    def __init__(self, series, *args, **kwargs):
        """
        The metrics' payload.

        :param series: A list of time series to submit to Datadog.
        :type series: [Series]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.series = series

    @classmethod
    def _from_openapi_data(cls, series, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricsPayload, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.series = series
        return self
