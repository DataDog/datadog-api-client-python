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
    from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_one_of_access_details_aws_detail import (
        TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAwsDetail,
    )
    from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_one_of_access_details_azure_detail import (
        TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAzureDetail,
    )
    from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_one_of_access_details_gcp_detail import (
        TableResultV2DataAttributesFileMetadataOneOfAccessDetailsGcpDetail,
    )


class TableResultV2DataAttributesFileMetadataOneOfAccessDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_one_of_access_details_aws_detail import (
            TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAwsDetail,
        )
        from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_one_of_access_details_azure_detail import (
            TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAzureDetail,
        )
        from datadog_api_client.v2.model.table_result_v2_data_attributes_file_metadata_one_of_access_details_gcp_detail import (
            TableResultV2DataAttributesFileMetadataOneOfAccessDetailsGcpDetail,
        )

        return {
            "aws_detail": (TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAwsDetail,),
            "azure_detail": (TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAzureDetail,),
            "gcp_detail": (TableResultV2DataAttributesFileMetadataOneOfAccessDetailsGcpDetail,),
        }

    attribute_map = {
        "aws_detail": "aws_detail",
        "azure_detail": "azure_detail",
        "gcp_detail": "gcp_detail",
    }

    def __init__(
        self_,
        aws_detail: Union[TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAwsDetail, UnsetType] = unset,
        azure_detail: Union[TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAzureDetail, UnsetType] = unset,
        gcp_detail: Union[TableResultV2DataAttributesFileMetadataOneOfAccessDetailsGcpDetail, UnsetType] = unset,
        **kwargs,
    ):
        """
        Cloud storage access configuration for the reference table data file.

        :param aws_detail: Amazon Web Services S3 storage access configuration.
        :type aws_detail: TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAwsDetail, optional

        :param azure_detail: Azure Blob Storage access configuration.
        :type azure_detail: TableResultV2DataAttributesFileMetadataOneOfAccessDetailsAzureDetail, optional

        :param gcp_detail: Google Cloud Platform storage access configuration.
        :type gcp_detail: TableResultV2DataAttributesFileMetadataOneOfAccessDetailsGcpDetail, optional
        """
        if aws_detail is not unset:
            kwargs["aws_detail"] = aws_detail
        if azure_detail is not unset:
            kwargs["azure_detail"] = azure_detail
        if gcp_detail is not unset:
            kwargs["gcp_detail"] = gcp_detail
        super().__init__(kwargs)
