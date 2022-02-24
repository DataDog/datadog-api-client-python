# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_volumes import MetricVolumes

    globals()["MetricVolumes"] = MetricVolumes


class MetricVolumesResponse(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "data": (MetricVolumes,),
        }

    attribute_map = {
        "data": "data",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Response object which includes a single metric's volume.

        :param data: Possible response objects for a metric's volume.
        :type data: MetricVolumes, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricVolumesResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
