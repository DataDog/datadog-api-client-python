# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AssignmentResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "detail": (str,),
            "finding_id": (str,),
            "status": (int,),
            "title": (str,),
        }

    attribute_map = {
        "detail": "detail",
        "finding_id": "finding_id",
        "status": "status",
        "title": "title",
    }

    def __init__(self_, detail: str, finding_id: str, status: int, title: str, **kwargs):
        """
        Per-finding outcome of an assign or unassign operation.

        :param detail: Human-readable explanation of the outcome.
        :type detail: str

        :param finding_id: Unique identifier of the security finding.
        :type finding_id: str

        :param status: HTTP-like status code describing the outcome for this finding.
        :type status: int

        :param title: Short label describing the outcome for this finding.
        :type title: str
        """
        super().__init__(kwargs)

        self_.detail = detail
        self_.finding_id = finding_id
        self_.status = status
        self_.title = title
