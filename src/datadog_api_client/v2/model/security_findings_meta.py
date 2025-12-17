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
    from datadog_api_client.v2.model.security_findings_page import SecurityFindingsPage
    from datadog_api_client.v2.model.security_findings_status import SecurityFindingsStatus


class SecurityFindingsMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_findings_page import SecurityFindingsPage
        from datadog_api_client.v2.model.security_findings_status import SecurityFindingsStatus

        return {
            "elapsed": (int,),
            "page": (SecurityFindingsPage,),
            "request_id": (str,),
            "status": (SecurityFindingsStatus,),
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
        page: Union[SecurityFindingsPage, UnsetType] = unset,
        request_id: Union[str, UnsetType] = unset,
        status: Union[SecurityFindingsStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the response.

        :param elapsed: The time elapsed in milliseconds.
        :type elapsed: int, optional

        :param page: Pagination information.
        :type page: SecurityFindingsPage, optional

        :param request_id: The identifier of the request.
        :type request_id: str, optional

        :param status: The status of the response.
        :type status: SecurityFindingsStatus, optional
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
