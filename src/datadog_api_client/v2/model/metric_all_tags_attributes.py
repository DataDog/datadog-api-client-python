# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricAllTagsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "tags": ([str],),
        }

    attribute_map = {
        "tags": "tags",
    }

    def __init__(self_, *args, **kwargs):
        """
        Object containing the definition of a metric's tags.

        :param tags: List of indexed tag value pairs.
        :type tags: [str], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
