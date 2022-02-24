# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_ci_batch_metadata_ci import SyntheticsCIBatchMetadataCI
    from datadog_api_client.v1.model.synthetics_ci_batch_metadata_git import SyntheticsCIBatchMetadataGit

    globals()["SyntheticsCIBatchMetadataCI"] = SyntheticsCIBatchMetadataCI
    globals()["SyntheticsCIBatchMetadataGit"] = SyntheticsCIBatchMetadataGit


class SyntheticsCIBatchMetadata(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "ci": (SyntheticsCIBatchMetadataCI,),
            "git": (SyntheticsCIBatchMetadataGit,),
        }

    attribute_map = {
        "ci": "ci",
        "git": "git",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Metadata for the Synthetics tests run.

        :param ci: Description of the CI provider.
        :type ci: SyntheticsCIBatchMetadataCI, optional

        :param git: Git information.
        :type git: SyntheticsCIBatchMetadataGit, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsCIBatchMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
