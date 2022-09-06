# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricVolumesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_volumes import MetricVolumes

        return {
            "data": (MetricVolumes,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, *args, **kwargs):
        """
        Response object which includes a single metric's volume.

        :param data: Possible response objects for a metric's volume.
        :type data: MetricVolumes, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
