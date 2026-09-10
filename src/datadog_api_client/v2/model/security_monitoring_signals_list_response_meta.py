# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_signals_list_response_meta_page import (
        SecurityMonitoringSignalsListResponseMetaPage,
    )


class SecurityMonitoringSignalsListResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signals_list_response_meta_page import (
            SecurityMonitoringSignalsListResponseMetaPage,
        )

        return {
            "elapsed": (int,),
            "page": (SecurityMonitoringSignalsListResponseMetaPage,),
            "request_id": (str,),
            "status": (str,),
        }

    attribute_map = {
        "elapsed": "elapsed",
        "page": "page",
        "request_id": "request_id",
        "status": "status",
    }

    def __init__(
        self_,
        elapsed: Union[int, UnsetType] = unset,
        page: Union[SecurityMonitoringSignalsListResponseMetaPage, UnsetType] = unset,
        request_id: Union[str, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Meta attributes.

        :param elapsed: The time elapsed in milliseconds.
        :type elapsed: int, optional

        :param page: Paging attributes.
        :type page: SecurityMonitoringSignalsListResponseMetaPage, optional

        :param request_id: The unique identifier of the request.
        :type request_id: str, optional

        :param status: The status of the response.
        :type status: str, optional
        """
        if elapsed is not unset:
            kwargs["elapsed"] = elapsed
        if page is not unset:
            kwargs["page"] = page
        if request_id is not unset:
            kwargs["request_id"] = request_id
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
