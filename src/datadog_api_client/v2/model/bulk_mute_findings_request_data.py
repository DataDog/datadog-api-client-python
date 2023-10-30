# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.bulk_mute_findings_request_attributes import BulkMuteFindingsRequestAttributes
    from datadog_api_client.v2.model.bulk_mute_findings_request_meta import BulkMuteFindingsRequestMeta
    from datadog_api_client.v2.model.finding_type import FindingType


class BulkMuteFindingsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.bulk_mute_findings_request_attributes import BulkMuteFindingsRequestAttributes
        from datadog_api_client.v2.model.bulk_mute_findings_request_meta import BulkMuteFindingsRequestMeta
        from datadog_api_client.v2.model.finding_type import FindingType

        return {
            "attributes": (BulkMuteFindingsRequestAttributes,),
            "id": (str,),
            "meta": (BulkMuteFindingsRequestMeta,),
            "type": (FindingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: BulkMuteFindingsRequestAttributes,
        id: str,
        meta: BulkMuteFindingsRequestMeta,
        type: FindingType,
        **kwargs,
    ):
        """
        Data object containing the new bulk mute properties of the finding.

        :param attributes: The mute properties to be updated.
        :type attributes: BulkMuteFindingsRequestAttributes

        :param id: UUID to identify the request
        :type id: str

        :param meta: Meta object containing the findings to be updated.
        :type meta: BulkMuteFindingsRequestMeta

        :param type: The JSON:API type for findings.
        :type type: FindingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.meta = meta
        self_.type = type
