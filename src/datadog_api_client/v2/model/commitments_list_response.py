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
    from datadog_api_client.v2.model.commitments_list_item import CommitmentsListItem
    from datadog_api_client.v2.model.commitments_list_meta import CommitmentsListMeta
    from datadog_api_client.v2.model.commitments_aws_ec2_ri_commitment import CommitmentsAwsEC2RICommitment
    from datadog_api_client.v2.model.commitments_aws_rdsri_commitment import CommitmentsAwsRDSRICommitment
    from datadog_api_client.v2.model.commitments_aws_elasticache_ri_commitment import (
        CommitmentsAwsElasticacheRICommitment,
    )
    from datadog_api_client.v2.model.commitments_aws_sp_commitment import CommitmentsAwsSPCommitment
    from datadog_api_client.v2.model.commitments_azure_vmri_commitment import CommitmentsAzureVMRICommitment
    from datadog_api_client.v2.model.commitments_azure_compute_sp_commitment import CommitmentsAzureComputeSPCommitment


class CommitmentsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_list_item import CommitmentsListItem
        from datadog_api_client.v2.model.commitments_list_meta import CommitmentsListMeta

        return {
            "commitments": ([CommitmentsListItem],),
            "meta": (CommitmentsListMeta,),
        }

    attribute_map = {
        "commitments": "commitments",
        "meta": "meta",
    }

    def __init__(
        self_,
        commitments: List[
            Union[
                CommitmentsListItem,
                CommitmentsAwsEC2RICommitment,
                CommitmentsAwsRDSRICommitment,
                CommitmentsAwsElasticacheRICommitment,
                CommitmentsAwsSPCommitment,
                CommitmentsAzureVMRICommitment,
                CommitmentsAzureComputeSPCommitment,
            ]
        ],
        meta: Union[CommitmentsListMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a list of cloud commitment details.

        :param commitments: Array of commitment items.
        :type commitments: [CommitmentsListItem]

        :param meta: Metadata for a commitments list response.
        :type meta: CommitmentsListMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.commitments = commitments
