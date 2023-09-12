# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CustomDestinationFallbackDestination(ModelComposed):
    def __init__(self, **kwargs):
        """
        The archiving destination to fall back to.

        :param container: The container where the archive will be stored.
        :type container: str

        :param integration: The Azure archive's integration destination.
        :type integration: AzureFallbackDestinationIntegration

        :param path: The archive path.
        :type path: str, optional

        :param region: The region where the archive will be stored.
        :type region: str, optional

        :param storage_account: The associated storage account.
        :type storage_account: str

        :param type: Type of the Azure archive destination.
        :type type: AzureFallbackDestinationType

        :param bucket: The bucket where the archive will be stored.
        :type bucket: str
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.azure_fallback_destination import AzureFallbackDestination
        from datadog_api_client.v2.model.gcs_fallback_destination import GCSFallbackDestination
        from datadog_api_client.v2.model.s3_fallback_destination import S3FallbackDestination

        return {
            "oneOf": [
                AzureFallbackDestination,
                GCSFallbackDestination,
                S3FallbackDestination,
            ],
        }
