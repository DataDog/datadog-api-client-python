# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsCIBatchMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_ci_batch_metadata_ci import SyntheticsCIBatchMetadataCI
        from datadog_api_client.v1.model.synthetics_ci_batch_metadata_git import SyntheticsCIBatchMetadataGit

        return {
            "ci": (SyntheticsCIBatchMetadataCI,),
            "git": (SyntheticsCIBatchMetadataGit,),
        }

    attribute_map = {
        "ci": "ci",
        "git": "git",
    }

    def __init__(self_, *args, **kwargs):
        """
        Metadata for the Synthetics tests run.

        :param ci: Description of the CI provider.
        :type ci: SyntheticsCIBatchMetadataCI, optional

        :param git: Git information.
        :type git: SyntheticsCIBatchMetadataGit, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
