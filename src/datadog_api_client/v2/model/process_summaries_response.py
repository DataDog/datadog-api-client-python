# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProcessSummariesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.process_summary import ProcessSummary
        from datadog_api_client.v2.model.process_summaries_meta import ProcessSummariesMeta

        return {
            "data": ([ProcessSummary],),
            "meta": (ProcessSummariesMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        List of process summaries.

        :param data: Array of process summary objects.
        :type data: [ProcessSummary], optional

        :param meta: Response metadata object.
        :type meta: ProcessSummariesMeta, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ProcessSummariesResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
