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
    from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details_aws_detail import (
        PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail,
    )
    from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details_azure_detail import (
        PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail,
    )
    from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details_gcp_detail import (
        PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail,
    )


class PatchTableRequestDataAttributesFileMetadataOneOfAccessDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details_aws_detail import (
            PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail,
        )
        from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details_azure_detail import (
            PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail,
        )
        from datadog_api_client.v2.model.patch_table_request_data_attributes_file_metadata_one_of_access_details_gcp_detail import (
            PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail,
        )

        return {
            "aws_detail": (PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail,),
            "azure_detail": (PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail,),
            "gcp_detail": (PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail,),
        }

    attribute_map = {
        "aws_detail": "aws_detail",
        "azure_detail": "azure_detail",
        "gcp_detail": "gcp_detail",
    }

    def __init__(
        self_,
        aws_detail: Union[PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail, UnsetType] = unset,
        azure_detail: Union[
            PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail, UnsetType
        ] = unset,
        gcp_detail: Union[PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the access details object.

        :param aws_detail: The definition of the AWS access details object.
        :type aws_detail: PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail, optional

        :param azure_detail: The definition of the Azure access details object.
        :type azure_detail: PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail, optional

        :param gcp_detail: The definition of the GCP access details object.
        :type gcp_detail: PatchTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail, optional
        """
        if aws_detail is not unset:
            kwargs["aws_detail"] = aws_detail
        if azure_detail is not unset:
            kwargs["azure_detail"] = azure_detail
        if gcp_detail is not unset:
            kwargs["gcp_detail"] = gcp_detail
        super().__init__(kwargs)
