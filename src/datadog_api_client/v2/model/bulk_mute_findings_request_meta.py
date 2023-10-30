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
    from datadog_api_client.v2.model.bulk_mute_findings_request_meta_findings import BulkMuteFindingsRequestMetaFindings


class BulkMuteFindingsRequestMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.bulk_mute_findings_request_meta_findings import (
            BulkMuteFindingsRequestMetaFindings,
        )

        return {
            "findings": ([BulkMuteFindingsRequestMetaFindings],),
        }

    attribute_map = {
        "findings": "findings",
    }

    def __init__(self_, findings: Union[List[BulkMuteFindingsRequestMetaFindings], UnsetType] = unset, **kwargs):
        """
        Meta object containing the findings to be updated.

        :param findings: Array of findings.
        :type findings: [BulkMuteFindingsRequestMetaFindings], optional
        """
        if findings is not unset:
            kwargs["findings"] = findings
        super().__init__(kwargs)
