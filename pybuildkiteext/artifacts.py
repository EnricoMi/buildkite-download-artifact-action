#  Copyright 2020 G-Research
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from pybuildkite.artifacts import Artifacts
from pybuildkiteext import client


def download_artifact(self, organization, pipeline, build, job, artifact):
    """
    Returns a URL for downloading an artifact.

    :param organization: organization slug
    :param pipeline: pipeline slug
    :param build: build number
    :param job: job id
    :param artifact: artifact id
    :return: Returns the content of an artifact.
    """
    url = self.path + "jobs/{}/artifacts/{}/download/"
    headers = dict(Accept='application/octet-stream')
    return self.client.get(url.format(organization, pipeline, build, job, artifact), headers=headers)


Artifacts.download_artifact = download_artifact