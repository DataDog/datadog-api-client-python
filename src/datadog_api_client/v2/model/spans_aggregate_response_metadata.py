# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.spans_aggregate_response_status import SpansAggregateResponseStatus
    from datadog_api_client.v2.model.spans_warning import SpansWarning


class SpansAggregateResponseMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_aggregate_response_status import SpansAggregateResponseStatus
        from datadog_api_client.v2.model.spans_warning import SpansWarning

        return {
            "elapsed": (int,),
            "request_id": (str,),
            "status": (SpansAggregateResponseStatus,),
            "warnings": ([SpansWarning],),
        }

    attribute_map = {
        "elapsed": "elapsed",
        "request_id": "request_id",
        "status": "status",
        "warnings": "warnings",
    }

    def __init__(
        self_,
        elapsed: Union[int, UnsetType] = unset,
        request_id: Union[str, UnsetType] = unset,
        status: Union[SpansAggregateResponseStatus, UnsetType] = unset,
        warnings: Union[List[SpansWarning], UnsetType] = unset,
        **kwargs,
    ):
        """
        The metadata associated with a request.

        :param elapsed: The time elapsed in milliseconds.
        :type elapsed: int, optional

        :param request_id: The identifier of the request.
        :type request_id: str, optional

        :param status: The status of the response.
        :type status: SpansAggregateResponseStatus, optional

        :param warnings: A list of warnings (non fatal errors) encountered, partial results might be returned if
            warnings are present in the response.
        :type warnings: [SpansWarning], optional
        """
        if elapsed is not unset:
            kwargs["elapsed"] = elapsed
        if request_id is not unset:
            kwargs["request_id"] = request_id
        if status is not unset:
            kwargs["status"] = status
        if warnings is not unset:
            kwargs["warnings"] = warnings
        super().__init__(kwargs)
