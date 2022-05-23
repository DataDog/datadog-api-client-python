# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsPipelinesOrder(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "pipeline_ids": ([str],),
        }

    attribute_map = {
        "pipeline_ids": "pipeline_ids",
    }

    def __init__(self, pipeline_ids, *args, **kwargs):
        """
        Object containing the ordered list of pipeline IDs.

        :param pipeline_ids: Ordered Array of ``<PIPELINE_ID>`` strings, the order of pipeline IDs in the array
            define the overall Pipelines order for Datadog.
        :type pipeline_ids: [str]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.pipeline_ids = pipeline_ids

    @classmethod
    def _from_openapi_data(cls, pipeline_ids, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsPipelinesOrder, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.pipeline_ids = pipeline_ids
        return self
