# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DdsqlTabularQueryResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "elapsed": (int,),
            "request_id": (str,),
        }

    attribute_map = {
        "elapsed": "elapsed",
        "request_id": "request_id",
    }

    def __init__(self_, elapsed: int, request_id: str, **kwargs):
        """
        Top-level JSON:API meta block accompanying every DDSQL tabular query response.
        Carries standard observability handles for client-side correlation.

        :param elapsed: Server-side time spent serving this request, in milliseconds.
        :type elapsed: int

        :param request_id: Echo of the ``DD-Request-ID`` header assigned by Datadog's edge to this request,
            for support correlation.
        :type request_id: str
        """
        super().__init__(kwargs)

        self_.elapsed = elapsed
        self_.request_id = request_id
