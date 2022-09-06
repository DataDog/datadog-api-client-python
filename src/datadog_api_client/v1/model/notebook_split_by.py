# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookSplitBy(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "keys": ([str],),
            "tags": ([str],),
        }

    attribute_map = {
        "keys": "keys",
        "tags": "tags",
    }

    def __init__(self_, keys, tags, *args, **kwargs):
        """
        Object describing how to split the graph to display multiple visualizations per request.

        :param keys: Keys to split on.
        :type keys: [str]

        :param tags: Tags to split on.
        :type tags: [str]
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.keys = keys
        self_.tags = tags
