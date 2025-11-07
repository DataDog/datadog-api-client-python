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
    from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_aws_detail import (
        CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail,
    )
    from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_azure_detail import (
        CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail,
    )
    from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_gcp_detail import (
        CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail,
    )


class CreateTableRequestDataAttributesFileMetadataOneOfAccessDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_aws_detail import (
            CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail,
        )
        from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_azure_detail import (
            CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail,
        )
        from datadog_api_client.v2.model.create_table_request_data_attributes_file_metadata_one_of_access_details_gcp_detail import (
            CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail,
        )

        return {
            "aws_detail": (CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail,),
            "azure_detail": (CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail,),
            "gcp_detail": (CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail,),
        }

    attribute_map = {
        "aws_detail": "aws_detail",
        "azure_detail": "azure_detail",
        "gcp_detail": "gcp_detail",
    }

    def __init__(
        self_,
        aws_detail: Union[CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail, UnsetType] = unset,
        azure_detail: Union[
            CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail, UnsetType
        ] = unset,
        gcp_detail: Union[CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail, UnsetType] = unset,
        **kwargs,
    ):
        """
        Cloud storage access configuration for the reference table data file.

        :param aws_detail: Amazon Web Services S3 storage access configuration.
        :type aws_detail: CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAwsDetail, optional

        :param azure_detail: Azure Blob Storage access configuration.
        :type azure_detail: CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsAzureDetail, optional

        :param gcp_detail: Google Cloud Platform storage access configuration.
        :type gcp_detail: CreateTableRequestDataAttributesFileMetadataOneOfAccessDetailsGcpDetail, optional
        """
        if aws_detail is not unset:
            kwargs["aws_detail"] = aws_detail
        if azure_detail is not unset:
            kwargs["azure_detail"] = azure_detail
        if gcp_detail is not unset:
            kwargs["gcp_detail"] = gcp_detail
        super().__init__(kwargs)
